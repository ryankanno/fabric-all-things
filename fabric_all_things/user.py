#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import task
from fabric.colors import green
from fabric.colors import red
from fabric.context_managers import quiet


@task
def find_user(username):
    """ Returns user entries from /etc/passwd """
    with quiet():
        output = run("grep ^{0} /etc/passwd".format(username))
        print green(output) if output.succeeded else \
            red("No users like '{0}'".format(username))


# vim: filetype=python
