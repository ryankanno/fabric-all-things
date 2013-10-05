#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings
from fabric.api import sudo
from fabric.api import task


@task
def service(name, action, warn_only=False):
    """ Generic function to start/stop/restart an init.d SysV service"""
    with settings(warn_only=warn_only):
        return sudo("/etc/init.d/{service} {action}".format(
            service=name, action=action))

# vim: filetype=python
