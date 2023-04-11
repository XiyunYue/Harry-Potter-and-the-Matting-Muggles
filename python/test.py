from read_Trimap import read_Trimap
from read_image import read_image
from Quality_Inspection import MSE_calculation, PSNR_calculation, SAD_calculation
from combining import combining
import cv2
from change_SameColorform import change_SameColorform
from Laplacian import Laplacian_matting
from change_Size import change_Size
from change_background import change_background

picture_number = 'GT01'
trimap_level = 'lowers/'
trimap_arrea = 'Trimap1'

trimap_name = trimap_level + 'trimap/' + trimap_arrea + picture_number + '.png'
# img_trimap = read_Trimap(trimap_name)
print(trimap_name)