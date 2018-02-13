import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pip_package(host):
    host.pip_package.get_packages(pip_path='/usr/bin/pip')


@pytest.mark.parametrize("name,version", [
    ("curl", "7"),
    ("unzip", "6.0"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)
