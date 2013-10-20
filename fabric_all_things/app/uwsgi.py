#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fabric_all_things.service as service


class UwsgiCommand(service.ServiceCommand):
    def run(self):
        return super(UwsgiCommand, self).run('uwsgi')


start = UwsgiCommand('start', 'Starts uwsgi', roles=['app-uwsgi'])
stop = UwsgiCommand('stop', 'Stops uwsgi', roles=['app-uwsgi'])
reload = UwsgiCommand('reload', 'Reload uwsgi', roles=['app-uwsgi'])
restart = UwsgiCommand('restart', 'Restart uwsgi', roles=['app-uwsgi'])

# vim: filetype=python
