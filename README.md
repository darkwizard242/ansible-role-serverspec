[![build-test](https://github.com/darkwizard242/ansible-role-serverspec/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-serverspec/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-serverspec/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-serverspec/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47776?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47776?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47776?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-serverspec&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-serverspec) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-serverspec&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-serverspec) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-serverspec&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-serverspec) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-serverspec&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-serverspec) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-serverspec?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-serverspec?color=orange&style=flat-square)

# Ansible Role: serverspec

Role to install [serverspec](https://serverspec.org/) on **Debian/Ubuntu** and **EL** systems. Serverspec is used for infrastructure testing.

## Requirements

Serverspec is a gem and thus, it does require ruby installed. This role automatically installs ruby as well (if it's not already available).

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
ruby_app_debian_package: ruby-full
ruby_app_el_package: ruby
ruby_desired_state: present
serverspec_app: serverspec
serverspec_desired_state: present
serverspec_user_install: no
serverspec_include_dependencies: yes
```

### Variables table:

Variable                        | Description
------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
ruby_app_debian_package         | Defines the app to install on Debian based systems i.e. **ruby-full**
ruby_app_el_package             | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **ruby**
ruby_desired_state              | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
serverspec_app                  | Defines the app to install on Debian based systems i.e. **serverspec**
serverspec_desired_state        | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the gem. Defaults to `present`.
serverspec_user_install         | Defined to dynamically set whether to install serverspec gem into a user's local gems.
serverspec_include_dependencies | Defined to dynamically set whether to install relative dependencies of serverspec or not.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **serverspec** gem) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.serverspec
```

For customizing behavior of role (i.e. removal of **serverspec** gem) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.serverspec
  vars:
    serverspec_desired_state: absent
```

For customizing behavior of role (i.e. installing **serverspec** without it's required dependencies) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.serverspec
  vars:
    serverspec_include_dependencies: no
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-serverspec/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
