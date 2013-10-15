#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.colors import green
from fabric.colors import red
from fabric.colors import yellow
from time import sleep


def wait_for_instance_state(instance, state, num_secs_to_sleep=20,
                            max_num_times=5):
    num_times = 0
    while True and num_times < max_num_times:
        instance.update()
        if state == instance.state:
            return
        else:
            num_times += 1
            sleep(num_secs_to_sleep)
    raise Exception


def state(instance_state):
    if instance_state == 'running':
        return green(instance_state)
    elif instance_state == 'terminated' or instance_state == 'stopped':
        return red(instance_state)
    elif instance_state == 'shutting-down' or instance_state == 'stopping':
        return yellow(instance_state)
    else:
        return instance_state


# vim: filetype=python
