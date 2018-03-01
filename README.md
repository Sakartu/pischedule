# pischedule
## Description
A simple flask+sqlalchemy webfrontend for cron, in my case used to turn a raspi based internet radio on and off at certain 
times during the week

## Requirements
Besides the latest version of python3, a number of separate packages is required. Install these as described below. 
If you want to run pischedule using a normal webserver (Apache, lighttpd or nginx), a wsgi file and uwsgi ini file are supplied.
Refer to the many available uwsgi setup tutorials for your specific operating system flavour.

#### Install dependencies using pip
```
pip3 install -r requirements.txt
```

#### Install dependencies manually
Install the following packages manually:
* flask
* flask-wtf
* uwsgi
* flask-sqlalchemy
* sqlalchemy-migrate
* docopt

## Setup
Before running, you should create a database using ```db_create.py``` and then ```db_migrate.py```. With that done, it's time to create a secret key
for your application. This key is used to secure sessions, etc. Open a python console and run:
```python
import os
os.urandom(24)
```
Copy the resulting (byte)string, open config.py and paste the copied value as a value for SECRET_KEY.

## Running
You can easily start a development server using:

```
python3 run.py
```

If you're ready to run the server without development settings, open up config.py once more and set ```DEBUG = False``` to disable debugging.
