import os
import open3d as o3d
import numpy as np

filename = ''

mesh = o3d.io.read_triangle_mesh('mesh/'+filename+'.stl')
mesh.compute_vertex_normals()
pcl = mesh.sample_points_poisson_disk(number_of_points=5000)
hull, _ = pcl.compute_convex_hull()
hull.orient_triangles()
o3d.visualization.draw_geometries([hull])
hull.compute_vertex_normals()
o3d.io.write_triangle_mesh('mesh/'+filename+'_out.stl', hull)
