#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import roles
from fabric.api import task
from ..service import restart as start_command
from ..service import restart as stop_command
from ..service import restart as restart_command


@task
@roles('app-uwsgi')
def start():
    """ Starts uwsgi """
    start_command('uwsgi')


@task
@roles('app-uwsgi')
def stop():
    """ Stops uwsgi """
    stop_command('uwsgi')


@task
@roles('app-uwsgi')
def restart():
    """ Restarts uwsgi """
    restart_command('uwsgi')

# vim: filetype=python
