#!/usr/bin/env bash
# Prepare my webservers (web-01 & web-02)

# Install nginx if not present
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get update -y -qq && \
         sudo apt-get install -y nginx
    sudo service nginx restart
fi

# Create directories...
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# Create index.html for the test directory
echo "<h1>skynet</h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# Backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up the content of /data/web_static/current/ to redirect to domain.tech/hbnb_static
sudo sed -i '/server {/a \        location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart the nginx service.
sudo service nginx restart
