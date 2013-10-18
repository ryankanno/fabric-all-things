#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import task


@task
def update():
    """ Update sources """
    sudo("apt-get update")


@task
def upgrade():
    """ Upgrade sources """
    update()
    sudo("apt-get upgrade -y")

# vim: filetype=python
