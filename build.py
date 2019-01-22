#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import datetime
import os
import shutil
from conans import tools
from cpt.packager import ConanMultiPackager


class CPTHelper(object):
    @property
    def username(self):
        return os.getenv("CONAN_USERNAME", "conan")

    @property
    def channel(self):
        return os.getenv("CONAN_CHANNEL", "testing")

    @property
    def version(self):
        now = datetime.datetime.now()
        return now.strftime("%Y%m%d")

    @property
    def reference(self):
        namespace = "{}/{}".format(self.username, self.channel)
        return "abseil/{}@{}".format(self.version, namespace)

    def download_abseil(self):
        print("Downloading abseil project ...")
        temp_dir = tempfile.mkdtemp()
        target_dir = os.path.join(temp_dir, "abseil-cpp-master")
        tools.get("https://github.com/abseil/abseil-cpp/archive/master.zip", destination=temp_dir)
        files = os.listdir(target_dir)
        for index in files:
            if "README" in index: continue
            shutil.move(os.path.join(target_dir, index), os.getcwd())


if __name__ == "__main__":
    cpt_helper = CPTHelper()
    cpt_helper.download_abseil()
    builder = ConanMultiPackager(
        reference=cpt_helper.reference,
        username=cpt_helper.username,
        channel=cpt_helper.channel)
    builder.add_common_builds(pure_c=False)
    builder.run()
