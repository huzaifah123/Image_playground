from PIL import Image, ImageFilter #importing the library

img = Image.open('./astro.jpg') #file path
img.thumbnail((400,400))
img.save('thumbnail.jpg')

print(img.size)