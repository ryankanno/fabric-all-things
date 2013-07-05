#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings
from fabric.api import sudo


def service(name, action, warn_only=False):
    """ Generic service function """
    with settings(warn_only=warn_only):
        return sudo("/etc/init.d/{service} {action}".format(
            service=name, action=action))

# vim: filetype=python
