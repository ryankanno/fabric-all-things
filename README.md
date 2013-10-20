# fabric-all-things

Just open-sourcing a bunch of utilities I've written over the years.  I'll be
pushing to this repo as I clean them up.

# installation

To test these scripts, I've included a test Vagrantfile w/ 
[ansible](https://github.com/ansible/ansible) playbooks to 
provision the Vagrant instance.

 - `vagrant up`
 - `vagrant provision`
 - Create a **environment.py** file (here's an [example](https://github.com/ryankanno/fabric-all-things/blob/master/environment.py.example))
 - Create a **fabfile.py** (here's an [example](https://github.com/ryankanno/fabric-all-things/blob/master/fabfile.py.example))

## usage

List available tasks:

`fab -l`

Run tasks:

`fab test system.uname`
