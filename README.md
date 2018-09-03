# Python_scikit_Seam_Carver

Simple Seam Carver in Python 3 using the scikit image processing library skimage. It removes all the horizontal seams first,
recomputes the energy image, then removes all the vertical seams. Quality of results could be greatly improved by removing
seams one at a time, and recomputing the energy image every time, which will be updated later.
