#!/usr/bin/env bash

set -eux;

INSTALL_PKGS="highlight nss_wrapper gettext python python-pip";

# Setup necessary packages
useradd -u 1001 python_user
yum -y install epel-release && yum -y install ${INSTALL_PKGS} &&  yum clean all;
pip install -r requirements.txt

# Fix the permissions
for item in "/app"; do
    . /opt/scripts/fix-permissions.sh ${item} 1001;
done
