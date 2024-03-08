#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content of /data/web_static/current/ to hbnb_static
CONFIG_FILE="/etc/nginx/sites-available/default"
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$CONFIG_FILE"

# Restart Nginx to apply changes
sudo service nginx restart

exit 0

