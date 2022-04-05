import os
import open3d as o3d
import numpy as np

gripper_type = 'vg10'
unit = 'mm'
model_name = 'suction_cups'

mesh = o3d.io.read_triangle_mesh('mesh/'+gripper_type+'/'+unit+'/'+model_name+'.stl')
mesh.compute_vertex_normals()
pcl = mesh.sample_points_poisson_disk(number_of_points=5000)
hull, _ = pcl.compute_convex_hull()
hull.orient_triangles()
o3d.visualization.draw_geometries([hull])
hull.compute_vertex_normals()
o3d.io.write_triangle_mesh('mesh/'+gripper_type+'/'+unit+'/out/'+model_name+'.stl', hull)
