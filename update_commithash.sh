#!/usr/bin/env bash

set -ex

new=$(git ls-remote "$1" HEAD | awk '{print $1}')
if [[ ! -e commithash ]] || [[ $(cat commithash) != $new ]]; then
    echo $new > commithash; 
    make release; 
fi

