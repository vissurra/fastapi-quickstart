#!/bin/bash

env=$1
image_tag=$2

config=${env}
image_name=fastapi-quickstart

echo "Building docker image, tag: ${image_tag}"
docker build --build-arg CONFIG=$config -t ${image_name}:${image_tag} --platform linux/amd64 . || ! echo 'Building docker image failed' || exit
