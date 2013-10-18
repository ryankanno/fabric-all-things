#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings
from fabric.api import sudo
from fabric.api import task


@task
def service_command(service, command, warn_only=False):
    """ Run an init.d SysV service command"""
    with settings(warn_only=warn_only):
        return sudo("/etc/init.d/{service} {command}".format(
            service=service, command=command))


@task
def start(service, warn_only=False):
    """ Start an init.d SysV service"""
    return service_command(service, 'start', warn_only)


@task
def stop(service, warn_only=False):
    """ Stop an init.d SysV service"""
    return service_command(service, 'stop', warn_only)


@task
def restart(service, warn_only=False):
    """ Restart an init.d SysV service"""
    return service_command(service, 'restart', warn_only)

# vim: filetype=python
