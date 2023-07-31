from PIL import Image
image=Image.open("download.jpg")
print(image.size)
naya_img=image.resize((1200,1200))
naya_img.save("nikhil2.jpg")
print(naya_img.size)


