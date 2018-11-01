#!/bin/bash

# This script assumes we start our container with a mount at /aws that contains our .aws and .ssh folders.
# This means it is convenient to start our container with a mount of this form:

# docker run -v ${HOME}/my-aws:/aws --interactive --tty awscli:1.0 bash

# NOTE: the ${HOME} variable works for *nix types of systems where our .ssh and .aws folders are expected to be off ~/

# In our containers, we run as root.  HUZZAH.
mkdir -p /root/.aws
mkdir -p /root/.ssh

# Explicitly copy each file one-by-one and avoid wildcards
cp -f /aws/.aws/config /root/.aws/config
cp -f /aws/.aws/credentials /root/.aws/credentials
cp -f /aws/.ssh/config /root/.ssh/config

