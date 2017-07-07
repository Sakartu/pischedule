import sys, os
basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert (0,basedir)
os.chdir(basedir)
from srv import app as application
