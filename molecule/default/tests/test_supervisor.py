import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_supervisor_log_dir(host):
    host.file('/var/log/supervisor').is_directory
    host.file('/var/log/supervisor').mode == 0o644


def test_supervisor_binaries(host):
    host.file('/usr/bin/supervisorctl').exists
    host.file('/usr/bin/supervisord').exists


def test_supervisor_config(host):
    host.file('/etc/supervisord.conf').exists
    host.file('/etc/supervisord.conf').mode == 0o644
