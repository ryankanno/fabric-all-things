#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser


class Config(object):
    def __init__(self, config_name='fabric-all-things.cfg'):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(config_name)

    def __getattr__(self, name):
        idx = name.find('_') 
        section = name[0:idx]
        key = name[idx + 1:len(name)]
        return self.config.get(section, key.lower())

config = Config()

# vim: filetype=python
