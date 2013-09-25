#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('fabric-all-things.cfg')

AWS_ACCESS_KEY_ID = config.get('Credentials', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config.get('Credentials', 'aws_secret_access_key')
AWS_REGION = config.get('AWS', 'aws_region')

import aws

# vim: filetype=python
