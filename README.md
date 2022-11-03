# nifti_to_hdf5
nifti (or .nii) transformer to hdf5 format

nifti of .nii is a method for storing 3d objects specially in medicals. However most of the networks out there work with 
hdf5 or h5 file format which is basically a method to store big size objects. This python script helps you store nifti data
and mask objects into a hdf5 file format, so you can easily feed your own data to models out there. 
in my own example data is named raw in hdf5 and mask is named label. You can change these names accordingly.
Besides the match method that matches data with it's mask is data specific. You can change this method to meet your desires. 
More explanation is in the code.




special thanks to this work for preparing the data I used in my work:

A. Carass, S. Roy, A. Jog, J.L. Cuzzocreo, E. Magrath, A. Gherman, J.
Button, J. Nguyen, F. Prados, C.H. Sudre, M.J. Cardoso, N. Cawley, O.
Ciccarelli, C.A.M. Wheeler-Kingshott, S. Ourselin, L. Catanese, H.
Deshpande, P. Maurel, O. Commowick, C. Barillot, X. Tomas-Fernandez,
S.K. Warfield, S. Vaidya, A. Chunduru, R. Muthuganapathy, G.
Krishnamurthi, A. Jesson, T. Arbel, O. Maier, H. Handels, L.O. Iheme,
D. Unay, S. Jain, D.M. Sima, D. Smeets, M. Ghafoorian, B. Platel, A.
Birenbaum, H. Greenspan, P.-L. Bazin, P.A. Calabresi, C.M.
Crainiceanu, L.M. Ellingsen, D.S. Reich, J.L. Prince, and D.L. Pham,
"Longitudinal Multiple Sclerosis Lesion Segmentation: Resource and
Challenge", NeuroImage, 148(C):77-102, 2017.
