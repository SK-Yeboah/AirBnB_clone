#!/usr/bin/python3
#Fab file to generate a .tzg archive from the content of a web_static

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the name for the archive
    now = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                     now.day, now.hour,
                                                     now.minute, now.second)

    # Create the archive
    result = local("tar -cvzf versions/{} web_static".format(file_name))

    # Check if the archive was created successfully
    if result.succeeded:
        return "versions/{}".format(file_name)
    else:
        return None
