#!/bin/bash

# Install snapd
sudo apt install -y snapd

# Enable Snap services
sudo systemctl enable --now snapd apparmor

# Update system path
echo 'export PATH=$PATH:/snap/bin' >> ~/.bashrc
source ~/.bashrc

# Install Postman using snap
sudo snap install postman
