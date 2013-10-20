#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import hide
from fabric.api import puts
from fabric.api import run
from fabric.api import settings
from fabric.api import task
from .output_helpers import success
from .output_helpers import error


@task
def cpus():
    """ Returns num cpus """
    system_command("cat /proc/cpuinfo | grep processor | wc -l")


@task
def df(flags='-h'):
    """ Returns free disk space """
    system_command("df {0}".format(flags))


@task
def du(flags='-h'):
    """ Returns disk space used """
    system_command("du {0}".format(flags))


@task
def free(flags='-k'):
    """ Returns free and used memory """
    system_command("free {0}".format(flags))


@task
def groups(user=None):
    """ Returns group user is in """
    command = "groups {0}".format(user) if user else "groups"
    system_command(command)


@task
def id(user=None):
    """ Returns real and user group ids """
    command = "id {0}".format(user) if user else "id"
    system_command(command)


@task
def ps(flags='-aux'):
    """ Returns process status """
    system_command("ps {0}".format(flags))


@task
def pstree(flags='-a'):
    """ Returns a tree of processes """
    system_command("pstree {0}".format(flags))


@task
def set():
    """ Returns environment """
    system_command("set")


@task
def uname(flags='-a'):
    """ Returns operating system name """
    system_command("uname {0}".format(flags))


@task
def uptime():
    """ Returns uptime """
    system_command('uptime')


@task
def w():
    """ Returns who is logged in and what they're doing """
    system_command('w')


def system_command(cmd, hidden_output=('running', 'warnings', 'output'),
                   warn_only=True, error_msg=''):
    with settings(hide(*hidden_output), warn_only=warn_only):
        output = run(cmd)
        if output.succeeded:
            return success(output)
        else:
            return error(error_msg) if error_msg else error(output)

# vim: filetype=python
