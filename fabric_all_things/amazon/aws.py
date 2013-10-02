#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto.ec2 import connect_to_region
from boto.ec2.blockdevicemapping import BlockDeviceMapping
from boto.ec2.blockdevicemapping import BlockDeviceType
from ..config import config

from fabric.api import task
from fabric.colors import green

from utilities import wait_for_instance_state

import os

@task
def run_instances(ami_id, aws_region=config.AWS_AWS_REGION, instance_type=None, key_name=None,
        availability_zone=None, security_groups=None, user_data=None):
    """
    Creates and runs AWS ami in a specified region 
    """

    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    instance_type = instance_type or 'm1.small'
    security_groups = security_groups.split(',')

    reservation = conn.run_instances(
        image_id=ami_id,
        key_name=key_name,
        security_groups=security_groups,
        instance_type=instance_type,
        user_data=user_data, 
        placement=availability_zone).instances[0]

    wait_for_instance_state(reservation, 'running')

    print "... Instance IP: {0}".format(reservation.ip_address)
    print "... Instance Hostname: {0}".format(reservation.public_dns_name)
    print "..."

    return reservation


@task
def images(
    aws_region=config.AWS_AWS_REGION,
    architecture='x86_64',
    image_type='machine',
    root_device_type='ebs', **kwargs):
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

    path_to_public_key = os.path.expanduser(path_to_public_key)

    with open(path_to_public_key, "rb") as public_key_file:
        encoded_public_key = public_key_file.read()
        keypair = conn.import_key_pair(key_name, encoded_public_key)

        print "Successfully uploaded keypair {0} ({1})".format(
            keypair.name,
            keypair.fingerprint)


@task
def instances(aws_region=config.AWS_AWS_REGION):
    """
    Returns all EC2 instances available to your account in a particular region
    """
    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID,
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    reservations = conn.get_all_instances()

    if reservations:
        for index, reservation in enumerate(reservations):
            idx = index + 1
            print "{0}. Id: {1} ({2}), Instances: {3}".format(
                idx, reservation.id, reservation.region.name, len(reservation.instances))
            print "{0}  Name: {1} | IP: {2}".format(
                "".rjust(len(str(idx))),
                reservation.instances[0].public_dns_name, 
                reservation.instances[0].ip_address)
    else:
        print "You have {0} instances in {1}".format(green("0",bold=True),
                aws_region)
        

@task
def keypairs(
    aws_region=config.AWS_AWS_REGION):
    """
    Returns all keypairs
    """
    conn = _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID, 
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    keypairs = conn.get_all_key_pairs()

    for index, keypair in enumerate(keypairs):
        idx = index + 1
        print "{0}. Name: {1} ({2})".format(
            idx, keypair.name, keypair.fingerprint)


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


# vim: filetype=python
