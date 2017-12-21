"""
Convert mesh data
=================

This example illustrate how to convert mesh data to be compatible with
visbrain.

As an example, download the Custom.npz file :
https://www.dropbox.com/s/phzptkbht4us33q/Custom.npz?dl=1

.. image:: ../../picture/picbrain/ex_convert_mesh_data.png
"""
import numpy as np
import vispy.visuals.transforms as vist

from visbrain import Brain
from visbrain.objects import BrainObj
from visbrain.utils import convert_meshdata
from visbrain.io import download_file, path_to_visbrain_data

# Define path to the template and load it :
download_file('Custom.npz')
mat = np.load(path_to_visbrain_data('Custom.npz'))

# Get vertices and faces from the archive :
vert, faces = mat['coord'], mat['tri']

# By default the template is not correctly oriented and need a 90° rotation.
# To this end, we define a rotation using VisPy :
z90_rotation = vist.MatrixTransform()
z90_rotation.rotate(90, (0, 0, 1))

# Then we extract vertices, faces and normals. By default, normals of this
# template are not correclty oriented so we the invert_normals to True :
vertices, faces, normals = convert_meshdata(vert, faces, invert_normals=True,
                                            transform=z90_rotation)

# Add the template :
b_obj = BrainObj('Custom', vertices=vertices, faces=faces, normals=normals)
b_obj.save()

vb = Brain(brain_obj=b_obj)
vb.show()

# If you want to remove the template :
b_obj.remove()
