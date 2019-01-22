#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import os
import shutil
from conans import tools
from cpt.packager import ConanMultiPackager


def download_abseil():
    print("Downloading abseil project ...")
    temp_dir = tempfile.mkdtemp()
    target_dir = os.path.join(temp_dir, "abseil-cpp-master")
    tools.get("https://github.com/abseil/abseil-cpp/archive/master.zip", destination=temp_dir)
    files = os.listdir(target_dir)
    for index in files:
        shutil.move(os.path.join(target_dir, index), os.getcwd())


if __name__ == "__main__":
    download_abseil()
    builder = ConanMultiPackager()
    builder.add_common_builds(pure_c=False)
    builder.run()
