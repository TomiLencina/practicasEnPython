from PIL import Image

im = Image.open("C:\Users\Usuario\Downloads\PLAYA-2.png")
rgb_im = im.convert("RGB")

rgb_im.save("C:\Users\Usuario\Downloads\PLAYA-2.jpg")

