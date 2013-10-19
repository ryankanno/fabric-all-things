#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import roles
from fabric.api import task
from ..service import restart as start_command
from ..service import restart as stop_command
from ..service import restart as restart_command


@task
@roles('www-nginx')
def start():
    """ Starts nginx """
    start_command('nginx')


@task
@roles('www-nginx')
def stop():
    """ Stops nginx """
    stop_command('nginx')


@task
@roles('www-nginx')
def restart():
    """ Restarts nginx """
    restart_command('nginx')

# vim: filetype=python
