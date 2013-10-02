#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

def wait_for_instance_state(instance, state, num_secs_to_sleep=20, max_num_times=5):
    num_times = 0;
    while True and num_times < max_num_times:
        instance.update()
        if state == instance.state: 
            return
        else:
            num_times += 1
            sleep(num_secs_to_sleep)
    raise Exception

# vim: filetype=python
