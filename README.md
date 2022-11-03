# nifti_to_hdf5
nifti (or .nii) transformer to hdf5 format

nifti of .nii is a method for storing 3d objects specially in medicals. However most of the networks out there work with 
hdf5 or h5 file format which is basically a method to store big size objects. This python script helps you store nifti data
and mask objects into a hdf5 file format, so you can easily feed your own data to models out there. 
in my own example data is named raw in hdf5 and mask is named label. You can change these names accordingly.
Besides the match method that matches data with it's mask is data specific. You can change this method to meet your desires. 
More explanation is in the code.

