##!/usr/bin/env python
## -*- coding: utf-8 -*-

from boto.ec2 import connect_to_region
from boto.ec2 import regions
from ..config import config
from fabric.api import task
from fabric.colors import green
from ..utilities import enum
from ..utilities import expanded_abspath
from formatter import InstanceFormatter
from formatter import SecurityGroupFormatter
from formatter import SecurityGroupDetailFormatter


@task
def all_instances():
    """
    Returns all instances in all regions
    """
    objects = _get_ec2_objects_across_all_regions(_get_instances)
    formatter = InstanceFormatter(objects)
    formatter.display()


@task
def all_security_groups():
    """
    Returns all security groups in all regions
    """
    objects = _get_ec2_objects_across_all_regions(_get_security_groups)
    formatter = SecurityGroupFormatter(objects)
    formatter.display()


@task
def import_key_pair(key_name, path_to_public_key,
                    aws_region=config.AWS_AWS_REGION):
    """
    Imports AWS key pair from local machine into region
    """
    conn = _get_ec2_connection_from_config(aws_region, config)
    path_to_pk = expanded_abspath(path_to_public_key)

    with open(path_to_pk, "rb") as public_key_file:
        encoded_public_key = public_key_file.read()
        key_pair = conn.import_key_pair(key_name, encoded_public_key)
        print "Successfully uploaded keypair {0} ({1})".format(
            key_pair.name,
            key_pair.fingerprint)


@task
def instances_by_region(aws_region=config.AWS_AWS_REGION):
    """
    Returns all instances in a particular region
    """
    instances = _get_instances(aws_region)
    formatter = InstanceFormatter(instances)
    formatter.display()


@task
def key_pairs_by_region(aws_region=config.AWS_AWS_REGION):
    """
    Returns all key pairs in a particular region
    """
    key_pairs = _get_key_pairs(aws_region)

    for i, kp in enum(key_pairs):
        print "{0}. {1} ({2})".format(i, green(kp.name), kp.fingerprint)


@task
def security_groups_by_region(aws_region=config.AWS_AWS_REGION):
    """
    Returns all security groups in a particular region
    """
    security_groups = _get_security_groups(aws_region)
    formatter = SecurityGroupFormatter(security_groups)
    formatter.display()


@task
def security_group_details(group_id, aws_region=config.AWS_AWS_REGION):
    """
    Returns security group details in a particular region
    """
    security_group = _get_security_groups(aws_region, group_ids=[group_id])
    formatter = SecurityGroupDetailFormatter(security_group)
    formatter.display()


def _get_ec2_objects_across_all_regions(func_get_object):
    ec2_objects = []

    aws_regions = regions(
        aws_acess_key_id=config.CREDENTIALS_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    for region in aws_regions:
        ec2_objects.extend(func_get_object(region.name))

    return ec2_objects


def _get_instances(aws_region, instance_ids=None, filters=None):
    conn = _get_ec2_connection_from_config(aws_region, config)
    try:
        return conn.get_only_instances(instance_ids, filters)
    except:
        return []


def _get_key_pairs(aws_region, keynames=None, filters=None):
    conn = _get_ec2_connection_from_config(aws_region, config)
    try:
        return conn.get_all_key_pairs(keynames, filters)
    except:
        return []


def _get_security_groups(aws_region,
                         group_names=None,
                         group_ids=None,
                         filters=None):
    conn = _get_ec2_connection_from_config(aws_region, config)
    try:
        return conn.get_all_security_groups(group_names, group_ids, filters)
    except:
        return []


def _get_ec2_connection_from_config(aws_region, config):
    return _get_ec2_connection(
        aws_region,
        config.CREDENTIALS_AWS_ACCESS_KEY_ID,
        config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)


def _get_ec2_connection(aws_region, aws_access_key_id, aws_secret_access_key):
    return connect_to_region(
        aws_region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)



#from utilities import wait_for_instance_state

#@task
#def images(aws_region=config.AWS_AWS_REGION, architecture='x86_64',
           #image_type='machine', root_device_type='ebs', **kwargs):
    #"""
    #Filters all EC2 images available
    #"""
    #filters = {'architecture': architecture, 'image_type': image_type,
               #'root_device_type': root_device_type}
    #merged_filters = dict(kwargs.items() + filters.items())

    #conn = _get_ec2_connection(
        #aws_region,
        #config.CREDENTIALS_AWS_ACCESS_KEY_ID,
        #config.CREDENTIALS_AWS_SECRET_ACCESS_KEY)

    #for image in conn.get_all_images(filters=merged_filters):
        #print green("{0} - {1}".format(image.id, image.description or ""))



#@task
#def run_instances(ami_id, aws_region=config.AWS_AWS_REGION, instance_type=None,
                  #key_name=None, availability_zone=None, security_groups=None,
                  #user_data=None):
    #"""
    #Creates and runs AWS ami in a specified region
    #"""
    #conn = _get_ec2_connection_from_config(aws_region, config)

    #instance_type = instance_type or 'm1.small'
    #security_groups = security_groups.split(',')

    #reservation = conn.run_instances(
        #image_id=ami_id,
        #key_name=key_name,
        #security_groups=security_groups,
        #instance_type=instance_type,
        #user_data=user_data,
        #placement=availability_zone).instances[0]

    #wait_for_instance_state(reservation, 'running')

    #print "... Instance IP: {0}".format(reservation.ip_address)
    #print "... Instance Hostname: {0}".format(reservation.public_dns_name)
    #print "..."

    #return reservation

## vim: filetype=python
