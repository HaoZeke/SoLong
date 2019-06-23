#!/usr/bin/env /home/haozeke/.venvs/aiFoundations/bin/python
from PIL import Image
from PIL import ImageOps
from pathlib import Path
import pandas as pd
from matplotlib import rc as graphConf

# Crop satlink images
myTestData = Path(r"/Storage/DataSets/KaggleFish/train")
satlink = (1280, 720)
for classFish in myTestData.iterdir():
    if classFish.is_dir():
        for fish in classFish.iterdir():
            if fish.suffix == ".jpg":
                im = Image.open(fish)
                if satlink == im.size:
                    watermark = (63, 20, 0, 0)
                    im = ImageOps.crop(im, watermark)
                    im.save(fish)
