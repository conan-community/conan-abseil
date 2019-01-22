#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import datetime
import os
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
        temp_dir = tempfile.mkdtemp()
        target_dir = os.path.join(temp_dir, "abseil-cpp-master")
        print("Downloading abseil project to %s" % target_dir)
        tools.get("https://github.com/abseil/abseil-cpp/archive/master.zip", destination=temp_dir)
        return target_dir


if __name__ == "__main__":
    cpt_helper = CPTHelper()
    target_dir = cpt_helper.download_abseil()
    test_folder = os.path.join(os.getcwd(), "test_package")
    with tools.chdir(target_dir):
        builder = ConanMultiPackager(
            reference=cpt_helper.reference,
            username=cpt_helper.username,
            channel=cpt_helper.channel,
            test_folder=test_folder)
        builder.add_common_builds(pure_c=False)
        builder.run()
