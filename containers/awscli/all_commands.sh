#!/bin/bash

cd /root 

#wget https://github.com/openshift/origin/releases/download/v3.6.0/openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz -O /root/openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz 
#tar -xvf openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz 
#ln -s openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit/oc /usr/local/bin/oc 

mkdir /root/.aws
cp -f /aws/.aws/config /root/.aws/config
cp -f /aws/.aws/credentials /root/.aws/credentials

mkdir /root/.ssh
cp -f /aws/.ssh/config /root/.ssh/config
