#!/usr/bin/env /home/haozeke/.venvs/aiFoundations/bin/python
from PIL import Image
from pathlib import Path
import pandas as pd
from matplotlib import rc as graphConf

# Some magic matplotlib
font = {"family": "Fira Code", "weight": "bold", "size": 14}

graphConf("font", **font)

# A helper function to view images
def showFish(fish, imgid):
    "Display some training set fish! This needs the fish type and the image id"
    myTestData = Path(r"/Storage/DataSets/KaggleFish/train")
    tmpPath = "img_" + imgid + ".jpg"
    Image.open(myTestData / fish / tmpPath).show()
    return


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
                    "Fish": str(fish.parent.relative_to(myTestData)),
                    "DimsWH": im.size,
                    # "Width": w,
                    # "Height": h,
                }
                psList.append(pseudoFrame)
# Casually make a dataframe
df = pd.DataFrame(psList)

# Invaluable
# df[df.DimsWH==(1280, 720)].Fish.value_counts

# ax = df["DimsWH"].value_counts().plot(kind="bar")
# fig = ax.get_figure()
# fig.tight_layout()
# fig.set_size_inches(18.5, 6.5)
# fig.savefig("joeDim.png")

# basewidth = 300
# wpercent = basewidth / float(im.size[0])
# hsize = int((float(im.size[1]) * float(wpercent)))
# im = im.resize((basewidth, hsize), Image.ANTIALIAS)
# # im = im.crop((0, 50, 777, 686))
# # im.show()
