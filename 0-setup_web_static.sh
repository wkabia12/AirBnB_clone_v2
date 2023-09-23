#!/usr/bin/env bash
#install nginx and folders in server
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
echo "I am working" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
link_file="/data/web_static/current"
config="/etc/nginx/sites-enabled/default"
sudo sed -i "41i \\\\tlocation /hbnb_static/ {\n\t\talias $link_file/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart
