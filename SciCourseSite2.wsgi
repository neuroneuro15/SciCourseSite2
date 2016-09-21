#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/SciCourseSite2/")


from run import app as application
application.secret_key = 'adfoadufaofduafadfjalwquweiorwqruwqorjwefjnmafnkdjfa;lkfjakfdjafjadfjafkdjafa'

