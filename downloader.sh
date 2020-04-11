#!/usr/bin/env bash
# check if local webserver is already up to download local version
if [[ $(lsof -Pi :8000 -sTCP:LISTEN) ]]; then
    echo "Local site is up! start to download."
else
    echo "localhost:8000 is down! Aborting"
    exit 1
fi

# download website from localhost:8000
wget -mkEpnp localhost:8000

