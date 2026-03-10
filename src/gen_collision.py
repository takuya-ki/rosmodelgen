#!/usr/bin/env python3

import argparse
import glob
import os
import os.path as osp
import sys

import open3d as o3d


def process_mesh(stlpath: str, outdirpath: str, n_points: int, visualize: bool) -> None:
    """Generate a convex hull collision mesh from a visual STL mesh.

    Args:
        stlpath: Path to the input STL file.
        outdirpath: Path to the output directory.
        n_points: Number of points for Poisson disk sampling.
        visualize: Whether to open an interactive visualization window.
    """
    print(f"Generating for {osp.basename(stlpath)}")
    mesh = o3d.io.read_triangle_mesh(stlpath)
    if not mesh.has_triangles():
        print(f"  Warning: {osp.basename(stlpath)} has no triangles, skipping.")
        return
    mesh.compute_vertex_normals()
    pcl = mesh.sample_points_poisson_disk(number_of_points=n_points)
    hull, _ = pcl.compute_convex_hull()
    hull.orient_triangles()
    if visualize:
        o3d.visualization.draw_geometries([hull])
    hull.compute_vertex_normals()
    outpath = osp.join(outdirpath, osp.basename(stlpath))
    o3d.io.write_triangle_mesh(outpath, hull)
    print(f"  Saved to {outpath}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate lightweight collision STL models from visual STL meshes."
    )
    parser.add_argument(
        "--indir",
        default="meshes/visual",
        help="Input directory containing visual STL files (default: meshes/visual)",
    )
    parser.add_argument(
        "--outdir",
        default="meshes/collision",
        help="Output directory for collision STL files (default: meshes/collision)",
    )
    parser.add_argument(
        "--n-points",
        type=int,
        default=5000,
        help="Number of points for Poisson disk sampling (default: 5000)",
    )
    parser.add_argument(
        "--no-viz",
        action="store_true",
        help="Disable the interactive visualization window",
    )
    args = parser.parse_args()

    repo_root = osp.join(osp.dirname(__file__), "..")
    indirpath = osp.join(repo_root, args.indir)
    outdirpath = osp.join(repo_root, args.outdir)

    stlpaths = glob.glob(osp.join(indirpath, "*.stl")) + glob.glob(
        osp.join(indirpath, "*.STL")
    )
    if not stlpaths:
        print(f"No STL files found in {indirpath}")
        sys.exit(0)

    os.makedirs(outdirpath, exist_ok=True)

    for stlpath in stlpaths:
        try:
            process_mesh(stlpath, outdirpath, args.n_points, not args.no_viz)
        except Exception as e:
            print(f"  Error processing {osp.basename(stlpath)}: {e}")


if __name__ == "__main__":
    main()
