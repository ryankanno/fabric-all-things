#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import sudo
from fabric.api import task
import fabric_all_things.service as service
import fabric_all_things.system as system


class NginxCommand(service.ServiceCommand):
    def run(self):
        return super(NginxCommand, self).run('nginx')


start = NginxCommand('start', 'Starts nginx', roles=['www-nginx'])
stop = NginxCommand('stop', 'Stops nginx', roles=['www-nginx'])
reload = NginxCommand('reload', 'Reload nginx', roles=['www-nginx'])
restart = NginxCommand('restart', 'Restart nginx', roles=['www-nginx'])


@task
def sites():
    """Display nginx enabled sites"""
    command = 'ls -la /etc/nginx/sites-enabled'
    system.system_command(command, sudo)


@task
def enable(site):
    """ Creates symlink from sites-available to sites-enabled """
    available = "/etc/nginx/sites-available/{site}".format(site=site)
    enabled = "/etc/nginx/sites-enabled/{site}".format(site=site)
    command = "ln -s {available} {enabled}".format(
        available=available, enabled=enabled)
    system.system_command(command, sudo)


@task
def disable(site):
    """ Removes symlink from sites-enabled """
    enabled = "/etc/nginx/sites-enabled/{site}".format(site=site)
    command = "rm {enabled}".format(enabled=enabled)
    system.system_command(command, sudo)


# vim: filetype=python
