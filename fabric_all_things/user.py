#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import task
from .system import system_command


@task
def find_user(username):
    """ Returns user entries from /etc/passwd """
    command = "grep ^{0} /etc/passwd".format(username)
    error_msg = "No users like '{0}'".format(username)
    system_command(command, error_msg=error_msg)

# vim: filetype=python
