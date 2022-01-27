# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Problem 1
# %% [markdown]
# ## (a) 

# %%
import numpy as np
from utils import load_obj, load_ply, load_binvox

# STUDENT CODE START
obj = "chair_example"
# load obj: chair_example.obj
mesh = load_obj('./' + obj + '.obj')

# load ply: chair_example.ply
point_cloud = load_ply('./' + obj + '.ply')

# load binvox: chair_example.binvox
voxel = load_binvox('./' + obj + '.binvox')

print('Mesh', mesh, len(mesh), mesh[0].shape, mesh[1].shape, np.amax(mesh[1]))
print('point_cloud', point_cloud, point_cloud.shape)
print('voxel', np.sum(voxel), voxel.shape)
# STUDENT CODE END

# %% [markdown]
# ## (b)

# %%
get_ipython().run_line_magic('matplotlib', 'notebook')

import matplotlib
from utils import load_obj, load_ply, load_binvox
from utils import viz_mesh, viz_pc, viz_bv


# %%
# STUDENT CODE START
# viz mesh: chair_example.obj
viz_mesh(np.array(mesh[0]), np.array(mesh[1]))
# STUDENT CODE END


# %%
# STUDENT CODE START
# viz pc: chair_example.ply
viz_pc(point_cloud)
# STUDENT CODE END


# %%
# STUDENT CODE START
# viz binvox: chair_example.binvox
viz_bv(voxel)
# STUDENT CODE END

# %% [markdown]
# ## (c)

# %%
import trimesh
from utils import load_obj

# STUDENT CODE START
# load chair_example2.obj and sample point cloud shapes using trimesh.sample.sample_surface_even

# STUDENT CODE END

# %% [markdown]
# ## (d)

# %%
import numpy as np
from utils import load_obj, viz_mesh

# STUDENT CODE START
# load chair_example.obj

# viz the original mesh

# STUDENT CODE END


# %%
# STUDENT CODE START
# now rotate 45 degree along the up-direction (the y-axis)

# viz the rotated mesh

# STUDENT CODE END


# %%
# STUDENT CODE START
# re-load chair_example.obj

# now double the scales along the x/z-axis 

# viz the scaled mesh

# STUDENT CODE END


# %%
import numpy as np
from utils import load_ply, viz_pc

# STUDENT CODE START
# load chair_example.ply

# viz the original pc

# STUDENT CODE END


# %%
# STUDENT CODE START
# now rotate 45 degree along the up-direction (the y-axis)

# viz the rotated pc

# STUDENT CODE END


# %%
# STUDENT CODE START
# re-load chair_example.ply

# now double the scales along the x/z-axis

# viz the scaled pc

# STUDENT CODE END

# %% [markdown]
# ## (e)

# %%
import numpy as np
from utils import load_binvox

# STUDENT CODE START
# load chair_example.bv and chair_example2.bv, both of resolution 32^3

# compute the percentage of voxels have different values (the code should be easy)

# STUDENT CODE END


# %%
import numpy as np
from utils import load_ply

# STUDENT CODE START
# load chair_example.ply and chair_example2.ply, both of point size 2000

# compute the chamfer distance (a useful utility function: scipy.spatial.distance.cdist)

# STUDENT CODE END


# %%



