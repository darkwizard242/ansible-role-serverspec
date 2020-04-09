import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ruby_package_installed(host):
    assert host.package("ruby-full").is_installed or \
      host.package("ruby").is_installed


def test_ruby_binary_exists(host):
    host.file('/usr/bin/ruby').exists


def test_ruby_binary_file(host):
    host.file('/usr/bin/ruby').is_file


def test_ruby_binary_which(host):
    assert host.check_output('which ruby') == '/usr/bin/ruby'


def test_serverspec_binary_exists(host):
    host.file('/usr/local/bin/serverspec-init').exists


def test_serverspec_binary_file(host):
    host.file('/usr/local/bin/serverspec-init').is_file


def test_serverspec_binary_which(host):
    assert host.check_output('which serverspec-init') == \
     '/usr/local/bin/serverspec-init'
