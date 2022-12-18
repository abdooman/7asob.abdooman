import os, shutil, re
from pathlib import Path

date = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((20|19)\d\d)(.*?)$"

for file in os.listdir(Path.home() / Path('OneDrive','Desktop','folder')):
    print(file)
