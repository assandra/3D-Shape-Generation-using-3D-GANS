import trimesh
mesh = trimesh.load_mesh('path2yourstlfile.stl')
assert(mesh.is_watertight) # you cannot build a solid if your volume is not tight
volume = mesh.voxelized(pitch=0.1)
mat = mesh.matrix # matrix of boolean

mesh.contains(points)