#!/usr/bin/env sh
docker build --tag vi-fileserver
docker run --mount src=$HOME,target=/host,type=bind vi-fileserver
