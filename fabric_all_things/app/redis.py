#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import roles
from fabric.api import sudo
from fabric.api import task
import fabric_all_things.service as service
import fabric_all_things.system as system


class RedisServerCommand(service.ServiceCommand):
    def run(self):
        return super(RedisServerCommand, self).run('redis-server')


start = RedisServerCommand('start', 'Starts redis', roles=['cache-redis'])
stop = RedisServerCommand('stop', 'Stops redis', roles=['cache-redis'])
restart = RedisServerCommand('restart', 'Restart redis', roles=['cache-redis'])


@task
@roles('cache-redis')
def flush():
    """ Flushes caches """
    command = 'redis-cli FLUSHALL'
    system.system_command(command, sudo)


@task
@roles('cache-redis')
def get(key):
    """ Get cache value stored @ key """
    command = "redis-cli GET {key}".format(key=key)
    system.system_command(command, sudo)


@task
@roles('cache-redis')
def set(key, value):
    """ Set cache value stored @ key """
    command = "redis-cli SET {key} {value}".format(key=key, value=value)
    system.system_command(command, sudo)

# vim: filetype=python
