#!/usr/bin/env python3

import glob
import os.path as osp
import numpy as np
import open3d as o3d


if __name__ == '__main__': 
    indirpath = 'meshes/visual'
    outdirpath = 'meshes/collision'

    path = osp.join(
        osp.dirname(__file__), '../', indirpath, '*.stl')
    stlpaths = glob.glob(path)
    outdirpath = osp.join(
        osp.dirname(__file__), '../', outdirpath)

    for stlpath in stlpaths:
        print('generating for '+osp.basename(stlpath))
        mesh = o3d.io.read_triangle_mesh(stlpath)
        mesh.compute_vertex_normals()
        pcl = mesh.sample_points_poisson_disk(number_of_points=5000)
        hull, _ = pcl.compute_convex_hull()
        hull.orient_triangles()
        o3d.visualization.draw_geometries([hull])
        hull.compute_vertex_normals()
        o3d.io.write_triangle_mesh(
            osp.join(outdirpath, osp.basename(stlpath)), hull)
