Role Name
=========

Ansible role to install docker

Requirements
------------



Role Variables
--------------

docker_prerequisites_packages
docker_main_packages
docker_users
docker_apt_arch
docker_apt_repository

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: acme.docker_ansible_role }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
