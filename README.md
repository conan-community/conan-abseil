# Conan Abseil

[![Download](https://api.bintray.com/packages/conan-community/conan/abseil%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/abseil%3Aconan/_latestVersion)
[![Build Status](https://travis-ci.org/conan-community/conan-abseil.svg)](https://travis-ci.org/conan-community/conan-abseil)
[![Build status](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-abseil?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-abseil)

[Conan.io](https://conan.io) **builder** for [abseil](https://github.com/abseil/abseil-cpp) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/abseil%3Aconan).

## Builder Package

Abseil has Conan supported, however its CI infrastructure is in [review](https://github.com/abseil/abseil-cpp/pull/197).
Meanwhile, Conan Community will provide a minimal infrastructure only to build Conan packages.
This project shall be **DEPRECATED** in the future, when Abseil will provide its own official package.

## Package Version

Since Abseil prefer to adopt "bleeding-edge" flavor, our releases will be created by date (YYYYMMDD).
The commit id does not help when you want to sort in a package search.

## Basic setup

    $ conan install abseil/20190122@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    abseil/20190122@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
