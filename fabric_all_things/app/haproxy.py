#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fabric_all_things.service as service


class HaproxyCommand(service.ServiceCommand):
    def run(self):
        return super(HaproxyCommand, self).run('haproxy')


start = HaproxyCommand('start', 'Starts haproxy', roles=['proxy-haproxy'])
stop = HaproxyCommand('stop', 'Stops haproxy', roles=['proxy-haproxy'])
reload = HaproxyCommand('reload', 'Reload haproxy', roles=['proxy-haproxy'])
restart = HaproxyCommand('restart', 'Restart haproxy', roles=['proxy-haproxy'])
status = HaproxyCommand('status', 'Display haproxy status', roles=['proxy-haproxy'])


# vim: filetype=python
