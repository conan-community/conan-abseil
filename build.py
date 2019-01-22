#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import os
import shutil
from conans import tools
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    temp_dir = tempfile.mkdtemp()
    target_dir = os.path.join(temp_dir, "abseil-cpp-master")
    print("temp_dir: %s" % temp_dir)
    tools.get("https://github.com/abseil/abseil-cpp/archive/master.zip", destination=temp_dir)
    files = os.listdir(target_dir)
    for index in files:
        shutil.move(os.path.join(target_dir, index), os.getcwd())

    #builder = ConanMultiPackager()
    #builder.add_common_builds(shared_option_name="abseil:shared")
    #builder.run()
