#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto.ec2 import connect_to_region
from boto.ec2.blockdevicemapping import BlockDeviceMapping
from boto.ec2.blockdevicemapping import BlockDeviceType
from fabric.api import task
from fabric.colors import green

from config import config

@task
def create_instance(aws_region, availability_zone, key_name, security_groups):
    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)


@task
def images(aws_region=config.AWS_AWS_REGION, architecture='x86_64', image_type='machine', root_device_type='ebs', **kwargs):
    """
    Filters all EC2 images available 
    """
    filters = {'architecture': architecture, 'image_type': image_type, 'root_device_type': root_device_type}
    merged_filters = dict(kwargs.items() + filters.items())

    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    for image in conn.get_all_images(filters=merged_filters):
        print green("{0}".format(image.id)) + " - " + (image.description or "")


@task
def import_key_pair(
    key_name, 
    path_to_public_key, 
    aws_region=config.AWS_AWS_REGION):
    """
    Imports AWS key pair from local machine into region
    """
    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    with open(path_to_public_key, "rb") as public_key_file:
        encoded_public_key = public_key_file.read()
        conn.import_key_pair(key_name, encoded_public_key)


@task
def instances(aws_region=config.AWS_AWS_REGION):
    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID,
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    reservations = conn.get_all_instances()
    for idx, r in enumerate(reservations):
        print '%d. Id: %s, Region: %s, Instances count: %d, Instances: %s' % (idx, r.id, r.region.name, len(r.instances), [e.id + '/' + e.state + '/' + str(e.tags) for e in r.instances])
        print 'public_dns_name: %s | IP: %s' % (r.instances[0].public_dns_name, r.instances[0].ip_address)


def _create_ami():
    pass


def _create_image():
    pass


def _get_block_device_mapping(device_name, size):
    device_type = BlockDeviceType()
    device_type.size = size
    device_mapping = BlockDeviceMapping()
    device_mapping[device_name] = device_type
    return device_mapping


def _get_ec2_connection(aws_region, aws_access_key_id, aws_secret_access_key):
    return connect_to_region(
        aws_region, 
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key)


def _get_latest_ami_image():
    pass

# vim: filetype=python
