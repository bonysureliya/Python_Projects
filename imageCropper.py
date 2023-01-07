# All The Imports
from PIL import Image
import os

# Height and Width of Image  
width = 600
height = 400

# Describing the coordinates
left = 0
top = 0
right = 10
bottom = 10

# Create an Directory to save 10*10 Images
os.mkdir("New Images Test 10px")

#Image Selected To Crop
image = Image.open('012-600-400-Image.jpg')

# Cropped the Image
im_crop = image.crop((left,top,right,bottom))

# Saved The Image
im_crop.save(f"New Images Test 10px/cropped_image_{str(0)}.jpg", quality=95)

# Looping through the image (no. of pieces you want )
for loppFor10pximages in range(0,2400):
# Pushing the left and right coordinates to right -> 10px
    left = left + 10
    right = right + 10
# Cropped The Image
    im_crop = image.crop((left,top,right,bottom))

# Image has been saved to the created Directory
    im_crop.save(f"New Images Test 10px/cropped_image_{str(loppFor10pximages + 1)}.jpg", quality=95)

# If the right coordinated reaches the end go one step down
    if (right == width):
        top = top + 10
        bottom = bottom + 10
        left = 0
        right = 10
# If The image Ends break the loop
    if (bottom > height and right > width):
        break