import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dst = src + ".bak"

        #copy over permissions, modifcation times , and more
        #shutil.copy(src, dst)
        #shutil.copystat(src, dst)

        #rename og file
        #os.rename("textfile.txt", "newfile.txt")

        #put things into a zip
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()