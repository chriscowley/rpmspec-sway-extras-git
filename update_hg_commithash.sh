#!/usr/bin/env bash

set -ex

new=$(hg identify "$1")
if [[ ! -e commithash ]] || [[ $(cat commithash) != $new ]]; then
    echo $new > commithash; 
    make release; 
fi

