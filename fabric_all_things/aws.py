#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import task

@task
def import_key_pair(key_name, path_to_public_key):
    """
    Imports AWS key pair from local machine into region
    """
    conn = _get_region_connection(
        AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)

    with open(path_to_public_key, "rb") as public_key_file:
        encoded_public_key = public_key_file.read()
        conn.import_key_pair(key_name, encoded_public_key)


def _get_region_connection(aws_access_key_id, aws_secret_access_key, region_name):
    return connect_to_region(
        region_name, 
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key)


# vim: filetype=python
