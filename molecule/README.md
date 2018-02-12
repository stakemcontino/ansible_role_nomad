# What is molecule 

https://molecule.readthedocs.io/en/latest/index.html

## Getting started

This ansible role takes the base structure from ansible galaxy and adds molecule as a testing capability

Optional step to create a Python Virtual Environment
    virtualenv -p /usr/local/bin/python2.7 venv
    source venv/bin/activate
    pip install ansible molecule 'docker<3.0.0'

Step to create the ansible module
    ansible-galaxy init ansible_role_nomad
    cd ansible_role_nomad
    molecule init scenario --scenario-name default --role-name ansible_role_nomad

N.B. The default scenario uses docker as the driver to test the ansible role. Other drivers are available.

## Molecule: lint

Out of the box molecule will lint 3 types of files
1. https://yamllint.readthedocs.io/en/latest/
2. https://github.com/willthames/ansible-lint
3. http://flake8.pycqa.org/en/latest/

All can be configured or if you really want, disabled altogether.

To lint all the relevant code, run the following
    molecule lint

## Molecule: create

This is the start of the testing process, with molecule calling docker to create a suitable container environment to test the role

    molecule create

N.B. The docker containers that are created are defined here molecule/default/molecule.yml

## Molecule: converge

Will execute the sequence necessary to converge the instances. Which means run the molecule/default/playbook.yml against the instance created above.

    molecule converge

## Molecule: idempotence

Is the ansible role idempotent, aka does its produce repeatable and consistent results. Typically, idempotence highlights usage of command, shell and script
which results in a task running even if nothing needs to be done.

    molecule idempotence

## Molecule: verify

Uses the http://testinfra.readthedocs.io/en/latest/ to unit test the ansible role.

The tests are defined in molecule/default/tests/test_default.py

    molecule verify

## Molecule: test

Will execute all of the above, and some additional steps to test the ansible role.

    molecule test
