#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import env
from fabric.api import require
from contextlib import contextmanager 

@contextmanager
def virtualenv():
    require('virtualenv_path')
    require('virtualenv_activate')
    with cd(env.virtualenv_path):
        with prefix(env.virtualenv_activate):
            yield

# vim: filetype=python
