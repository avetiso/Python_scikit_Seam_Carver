import warnings
from skimage import transform, filters, io, color, util

print('Welcome to Python Seam Carver')
imgName = input('Please enter a valid image name including extension ')
img = io.imread(imgName)

if img is None:
    print('Failed to read image')
    exit(1)
else:
    height, width, channels = img.shape
    print('Loaded image', imgName, width, "x", height)

target_width = int(input('Please enter your desired image width between 100 and the original width '))
if target_width > width:
    print('Invalid width dimension')
    exit(2)

target_height = int(input('Please enter your desired image height between 100 and the original height '))
if target_height > height:
    print('Invalid height dimension')
    exit(3)

grayImg = color.rgb2gray(img)
magImg = filters.sobel(grayImg)
resizedImg = transform.seam_carve(img, magImg, 'horizontal', height - target_height)
grayImg = color.rgb2gray(resizedImg)
magImg = filters.sobel(grayImg)
resizedImg = transform.seam_carve(resizedImg, magImg, 'vertical', width - target_width)

# casting back from float, ignore warning about loss of accuracy
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    resizedImg = util.img_as_ubyte(resizedImg)

io.imsave('resized.png', resizedImg)









