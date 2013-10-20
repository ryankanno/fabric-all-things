#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import execute
from fabric.api import settings
from fabric.api import sudo
from fabric.api import task
from fabric.tasks import Task


__all__ = ['start', 'stop', 'restart', 'reload', 'status']


@task
def service_command(service, command, warn_only=False):
    """ Run an init.d SysV service command"""
    with settings(warn_only=warn_only):
        return sudo("/etc/init.d/{service} {command}".format(
            service=service, command=command))


class ServiceCommand(Task):
    def __init__(self, command, docstring, roles=[], *args, **kwargs):
        super(ServiceCommand, self).__init__(*args, **kwargs)
        self.name = command
        self.__doc__ = docstring
        self.roles = roles

    def run(self, service, warn_only=False):
        return execute(service_command, service, self.name, warn_only)


start = ServiceCommand('start', 'Start an init.d SysV service')
stop = ServiceCommand('stop', 'Stop an init.d SysV service')
restart = ServiceCommand('restart', 'Restart an init.d SysV service')
reload = ServiceCommand('reload', 'Reload an init.d SysV service')
status = ServiceCommand('status', 'Display the status of a SysV service')


# vim: filetype=python
