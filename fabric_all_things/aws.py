#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto.ec2 import connect_to_region
from boto.ec2.blockdevicemapping import BlockDeviceMapping
from boto.ec2.blockdevicemapping import BlockDeviceType
from fabric.api import task
from fabric.colors import green

from config import config
from utilities import wait_for_instance_state

@task
def run_instance(aws_region, ami_id, instance_type=None, key_name=None,
        availability_zone=None):
    """
    Creates and runs AWS ami in a specified region 
    """

    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    instance_type = instance_type or 't1.micro'

    reservation = conn.run(
        image_id=ami_id,
        key_name=key_name,
        security_groups=security_groups,
        instance_type=instance_type,
        user_data=user_data, 
        placement=zone_name).instances[0]

    wait_for_instance_state(reservation, 'running')
    return reservation


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
    """
    Filters all EC2 instances available to your account
    """
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
