#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import task

@task
def production():
    env.settings = 'production'
    env.hosts    = ['88.88.88.88']
    env.roledefs.update({'www': ['88.88.88.88']})


@task
def staging():
    env.settings = 'staging'


@task
def local():
    env.settings = 'local'

# vim: filetype=python
