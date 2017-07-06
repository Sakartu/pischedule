import sys, os
sys.path.insert (0,'/var/www/pischedule/')
os.chdir("/var/www/pischedule/")
from srv import app as application
