# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:25:32 2021

@author: xiaob
"""

# import vtkmodules.all as vtk
from mayavi import mlab
import numpy as np
import nibabel as nib


img_filename = r'E:\MedicalSegmentation\DataSet\LiTs_Liver_2017\origin_train\ct\volume-20.nii'

process_imgfilename = r'E:\MedicalSegmentation\Visual\segmentation-164.nii'
img = nib.load(process_imgfilename)

assign_img = img.get_data()
print(np.unique(assign_img))
assign_img = np.rot90(assign_img, 3)

print(assign_img.shape)
print(type(assign_img))



a = [1, 2, 3] ; b = [4, 5, 6]; c = [7, 8, 9]
w2 = np.array( [ [a,b,c], [a,b,c] ] )
#自行导入你的3D图像数组
# img = load(....)
mlab.contour3d(assign_img) # img.shape = C*H*W
mlab.show()
# assign_img[:,:,5:15]