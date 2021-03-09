import shutil, os
from pathlib import Path

p = Path.home()
shutil.copy(p / "spam.txt", p / "some_folder")

shutil.copy(p / "eggs.txt", p / "some_folder/eggs2.txt")