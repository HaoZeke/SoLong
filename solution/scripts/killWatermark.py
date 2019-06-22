#!/usr/bin/env /home/haozeke/.venvs/aiFoundations/bin/python
from PIL import Image
from PIL import ImageOps

# The trick above is here https://stackoverflow.com/a/54244503/1895378

im = Image.open("joe.jpg")
border = (63, 20, 0, 0)  # left, up, right, bottom
im = ImageOps.crop(im, border)
im.save("newJoe.jpg")
