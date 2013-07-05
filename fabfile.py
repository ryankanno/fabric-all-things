#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import task

from environment import local
from environment import production
from environment import staging

@task
def makedirs(dir):
    pass

# vim: filetype=python
