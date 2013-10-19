#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import task
from fabric.colors import green
from fabric.context_managers import quiet


@task
def df(flags='-h'):
    """ Returns free disk space """
    system_command("df {0}".format(flags))


@task
def uname(flags='-a'):
    """ Returns operating system name """
    system_command("uname {0}".format(flags))


@task
def uptime():
    """ Returns uptime """
    system_command('uptime')


def system_command(command):
    with quiet():
        system_command = run(command, quiet=True)
        print(green(system_command))


# vim: filetype=python
