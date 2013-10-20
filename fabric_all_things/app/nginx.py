#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fabric_all_things.service as service


class NginxCommand(service.ServiceCommand):
    def run(self):
        return super(NginxCommand, self).run('nginx')


start = NginxCommand('start', 'Starts nginx', roles=['www-nginx'])
stop = NginxCommand('stop', 'Stops nginx', roles=['www-nginx'])
reload = NginxCommand('reload', 'Reload nginx', roles=['www-nginx'])
restart = NginxCommand('restart', 'Restart nginx', roles=['www-nginx'])

# vim: filetype=python
