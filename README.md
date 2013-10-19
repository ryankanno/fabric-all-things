# fabric-all-things

Just open-sourcing a bunch of utilities I've written over the years.  I'll be
pushing to this repo as I clean them up.

# installation

To test these scripts, I've included a test Vagrantfile. As a note, 
I'll include [ansible](https://github.com/ansible/ansible) playbooks to 
provision the Vagrant instance. 

(I'll get the setup.py up to speed at some point)

## usage

Create a file named environment.py

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import env
from fabric.api import task

@task
def test():
    env.settings = 'staging'
    env.hosts    = ['88.88.88.88']
    env.roledefs.update({'www-nginx': ['88.88.88.88']})
    env.user = 'vagrant'
    env.password = 'vagrant'

# vim: filetype=python
```

Create a file named fabfile.py

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from environment import test
from fabric_all_things import *

# vim: filetype=python
```

List available tasks:

`fab -l`

Run tasks:

`fab test uname`
