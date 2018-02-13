import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nomad_group(host):
    host.group('nomad').exists


def test_nomad_user(host):
    host.user('nomad').exists


def test_nomad_directories(host):
    host.file('/opt/nomad').is_directory
