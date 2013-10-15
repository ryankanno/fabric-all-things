#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def enum(seq, start=1):
    for i, x in enumerate(seq):
        yield i+start, x


def expanded_abspath(dir):
    expanded = os.path.expanduser(os.path.expandvars(dir))
    return os.path.abspath(expanded)


# vim: filetype=python
