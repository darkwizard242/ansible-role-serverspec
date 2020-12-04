import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/serverspec-init'


def test_serverspec_binary_exists(host):
    """
    Tests if serverspec-init binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_serverspec_binary_file(host):
    """
    Tests if serverspec-init binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_serverspec_binary_which(host):
    """
    Tests the output to confirm serverspec-init's binary location.
    """
    assert host.check_output('which serverspec-init') == PACKAGE_BINARY
