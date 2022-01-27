import torch
import numpy as np
import os
import utils
import hw_utils
import trimesh
import pyvista as pv

if __name__ == "__main__":
    obj = "chair_example"
    mesh = utils.load_obj('./' + obj + '.obj')
    point_cloud = utils.load_ply('./' + obj + '.ply')
    voxel = utils.load_binvox('./' + obj + '.binvox')

    print('Mesh', mesh, len(mesh), mesh[0].shape, mesh[1].shape, np.amax(mesh[1]))
    print('point_cloud', point_cloud, point_cloud.shape)
    print('voxel', np.sum(voxel), voxel.shape)

    #utils.viz_mesh(mesh[0], mesh[1])

    #utils.viz_pc(point_cloud)

    #utils.viz_bv(voxel)

    mesh2 = utils.load_obj('./' + obj + '2'+ '.obj')
    mesh2 = trimesh.Trimesh(vertices=mesh2[0],
                       faces=mesh2[1]-1)
    #pc1000 = trimesh.sample.sample_surface_even(mesh2, count=2500)
    #pc10000 = trimesh.sample.sample_surface_even(mesh2, count=23000)

    #utils.viz_pc(pc1000[0])
    #utils.viz_pc(pc10000[0])

    voxel16 = utils.load_binvox('./' + obj + '2' + '_16.binvox')
    voxel32 = utils.load_binvox('./' + obj + '2' + '_32.binvox')
    #utils.viz_bv(voxel16)
    #utils.viz_bv(voxel32)

    '''
    # Rotate Mesh
    verts, faces = mesh
    verts = hw_utils.rotate(verts.T, [0, 45, 0])
    mesh_rotated = (verts.T, faces)
    utils.viz_mesh(mesh_rotated[0], mesh_rotated[1], params=(90, 0))

    # Scale Mesh
    verts, faces = mesh
    size = np.array([2., 1., 2.])
    verts = hw_utils.scale(verts, size)
    mesh_scaled = (verts, faces)
    utils.viz_mesh(mesh_scaled[0], mesh_scaled[1], params=(90, 0))
    utils.viz_mesh(mesh[0], mesh[1], params=(90, 0))

    # Rotate Point Cloud
    pc_rotated = hw_utils.rotate(point_cloud.T, [0, 45, 0])
    utils.viz_pc(pc_rotated.T, params=(90, 0))

    # Scale Point Cloud
    pc_scaled = hw_utils.scale(point_cloud, size)
    utils.viz_pc(pc_scaled, params=(90, 0))
    utils.viz_pc(point_cloud, params=(90, 0))
    '''

    pc2 = trimesh.sample.sample_surface_even(mesh2, count=5000)
    point_cloud2 = pc2[0]
    point_cloud2 = point_cloud2[:2000]
    diff_pc = hw_utils.compare_pcs(point_cloud2, point_cloud)
    diff_vox = hw_utils.compare_voxels(voxel32, voxel)

    print('Distance for pcs', diff_pc)
    print('Distance for vox', diff_vox)
    print(voxel.shape, voxel32.shape)