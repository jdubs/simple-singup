import sys
import logging, sys
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, "/var/www/signup")
from flaskapp import app as application
