#!/bin/bash

echo "Init git"
git submodule init
git submodule update --remote
git submodule foreach git checkout devel

echo "Init vagrant"
vagrant up
