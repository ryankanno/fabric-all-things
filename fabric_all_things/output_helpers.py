#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import puts
from fabric.colors import blue
from fabric.colors import green
from fabric.colors import red
from fabric.colors import yellow


def info(msg):
    return puts(blue(msg))


def error(msg):
    return puts(red(msg))


def success(msg):
    return puts(green(msg))


def warn(msg):
    return puts(yellow(msg))

# vim: filetype=python
