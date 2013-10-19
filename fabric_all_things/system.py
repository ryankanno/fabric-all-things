#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import sudo
from fabric.api import task
from fabric.colors import green
from fabric.context_managers import quiet


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
def groups(user):
    """ Returns group user is in """
    system_command("groups {0}".format(user))


@task
def id(user):
    """ Returns real and user group ids """
    system_command("id {0}".format(user))


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


def system_command(command):
    with quiet():
        system_command = run(command, quiet=True)
        print(green(system_command))


# vim: filetype=python
