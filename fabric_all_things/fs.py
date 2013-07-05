#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings

def symlink(src, target):
    """ See: http://blog.moertel.com/articles/2005/08/22/how-to-change-symlinks-atomically """
    pass


def makedirs(dir):
    with settings(warn_only=True):
        run("mkdir -p {dir}".format(dir=dir))

# vim: filetype=python
