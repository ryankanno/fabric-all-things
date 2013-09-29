#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto.ec2 import connect_to_region
from fabric.api import task
from .config import config


@task
def import_key_pair(key_name, path_to_public_key):
    """
    Imports AWS key pair from local machine into region
    """
    conn = _get_ec2_connection(
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY, 
        config.AWS_AWS_REGION)

    with open(path_to_public_key, "rb") as public_key_file:
        encoded_public_key = public_key_file.read()
        conn.import_key_pair(key_name, encoded_public_key)


@task
def images(architecture='x64', image_type='machine', root_device_type='ebs', **kwargs):
    """
    Imports AWS key pair from local machine into region
    """
    filters = {'architecture': architecture, 'image_type': image_type, 'root_device_type': root_device_type}
    merged_filters = dict(kwargs.items() + filters.items())
    conn = _get_ec2_connection(
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY, 
        config.AWS_AWS_REGION)
    return conn.get_all_images(filters=merged_filters)


def _get_ec2_connection(aws_access_key_id, aws_secret_access_key, aws_region):
    return connect_to_region(
        aws_region, 
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key)

# vim: filetype=python
