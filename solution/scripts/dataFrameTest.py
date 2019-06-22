#!/usr/bin/env /home/haozeke/.venvs/aiFoundations/bin/python
from PIL import Image
from pathlib import Path
import pandas as pd

# Create a dict
myTestData = Path(r"/Storage/DataSets/KaggleFish/train")
pseudoFrame = {}  # Single constantly updated list
psList = []  # List of dicts
for classFish in myTestData.iterdir():
    if classFish.is_dir():
        for fish in classFish.iterdir():
            if fish.suffix == ".jpg":
                im = Image.open(fish)
                w, h = im.size
                pseudoFrame = {
                    "Name": str(fish.name),
                    "Width": w,
                    "Height": h,
                    "Fish": str(fish.parent.relative_to(myTestData)),
                    "Dimensions": im.size,
                }
                psList.append(pseudoFrame)
# Casually make a dataframe
df = pd.DataFrame(psList)

# basewidth = 300
# wpercent = basewidth / float(im.size[0])
# hsize = int((float(im.size[1]) * float(wpercent)))
# im = im.resize((basewidth, hsize), Image.ANTIALIAS)
# # im = im.crop((0, 50, 777, 686))
# # im.show()
