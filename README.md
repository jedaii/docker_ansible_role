Role Name
=========

Ansible role to install docker

Requirements
------------



Role Variables
--------------
```
docker_prerequisites_packages
```
```
docker_main_packages
```
```
docker_users:
  - someuser
  - otheruser
```
A list of users to be added to `docker` group. The users must already exist in the system.
docker_apt_repository

Dependencies
------------


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: docker_ansible_role }

License
-------

BSD

Author Information
------------------

Alexander Ryzhov
