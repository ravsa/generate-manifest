#!/usr/bin/env bash

export USER_ID=$(id -u);
export GROUP_ID=$(id -g);
envsubst < /opt/scripts/passwd.template > /tmp/passwd;
export LD_PRELOAD=libnss_wrapper.so;
export NSS_WRAPPER_PASSWD=/tmp/passwd;
export NSS_WRAPPER_GROUP=/etc/group;
export FLASK_APP="app.py"

if [ $1 == "app" ]; then
    exec flask run;
else
    exec $@
fi
