#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings

import os


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                yield os.path.join(root, basename)


def makedirs(dir):
    with settings(warn_only=True):
        run("mkdir -p {dir}".format(dir=dir))


def symlink(src, target):
    """ http://blog.moertel.com/articles/
        2005/08/22/how-to-change-symlinks-atomically """
    pass


# vim: filetype=python
