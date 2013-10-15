#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.colors import green
from ..utilities import enum
from utilities import state


# TODO : Should probably add region logic to all of these (group by)

class InstanceFormatter(object):

    def __init__(self, instances):
        self.instances = instances

    def display(self):
        if self.instances:
            for i, inst in enum(self.instances):
                if inst.public_dns_name:
                    print "{0}. Id: {1} | {2} (Public: {3}, Private: {4}) - {5}".format(
                        i, inst.id, green(inst.public_dns_name), inst.ip_address,
                        inst.private_ip_address, state(inst.state))
                else:
                    print "{0}. Id: {1} | {2}".format(
                        i, inst.id, state(inst.state))
        else:
            print "You have {0} instances".format(green("0", bold=True))


class SecurityGroupFormatter(object):

    def __init__(self, security_groups):
        self.security_groups = security_groups

    def display(self):
        if self.security_groups:
            for i, sg in enum(self.security_groups):
                print "{0}. {1} ({2}) - {3}".format(
                    i, green(sg.name), sg.id, sg.description)
        else:
            print "You have {0} security groups".format(green("0", bold=True))


# vim: filetype=python
