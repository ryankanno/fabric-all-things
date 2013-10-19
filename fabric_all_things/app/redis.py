#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import roles
from fabric.api import run
from fabric.api import task


@task
@roles('cache-redis')
def flush():
    """ Flushes caches """
    run('redis-cli FLUSHALL')

# vim: filetype=python
