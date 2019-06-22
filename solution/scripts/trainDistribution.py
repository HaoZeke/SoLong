#!/usr/bin/env /home/haozeke/.venvs/aiFoundations/bin/python
from pathlib import Path
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# Get the number of files in a dict
myTestData = Path(r"/Storage/DataSets/KaggleFish/train")
imgCountHist = Counter()
for classFish in myTestData.iterdir():
    if classFish.is_dir():
        tmp = Counter(
            # Must explicitly cast as a string to get rid of PosixPath
            str(p.parent.relative_to(myTestData))
            for p in classFish.glob("*.j*")
        )
        dict.update(imgCountHist, tmp)

# Plot the bugger
labels, values = zip(*imgCountHist.items())
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes, labels)
plt.savefig("joeBar.png")
