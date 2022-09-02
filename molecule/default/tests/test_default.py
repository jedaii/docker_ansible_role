import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize("pkgs", [
    "ca-certificates",
    "curl",
    "gnupg",
    "lsb-release"
])
def test_prerequisites_packages(host, pkgs):
    pkg = host.package(pkgs)
    assert pkg.is_installed

@pytest.mark.parametrize("pkgs", [
    "docker-ce",
    "docker-ce-cli",
    "containerd.io"
])
def test_main_docker_packages(host, pkgs):
    pkg = host.package(pkgs)
    assert pkg.is_installed

def test_docker_service(host):
    s = host.service("docker")
    assert s.is_enabled
    assert s.is_running

def test_users_in_docker_group(host):
    docker_user = host.user("vagrant")
    assert "docker" in docker_user.groups