# pischedule
## Description
A simple flask+sqlalchemy webfrontend for cron, in my case used to turn a raspi based internet radio on and off at certain 
times during the week

## Requirements
Besides the latest version of python3, a number of separate packages is required. Install these as described below. 
If you want to run pischedule using a normal webserver (Apache, lighttpd or nginx), a wsgi file and uwsgi ini file are supplied.
Refer to the many available uwsgi setup tutorials for your specific operating system flavour.

### Using pip
```pip3 install -r requirements.txt```

### Manual
Install the following packages manually:
* flask
* flask-wtf
* uwsgi
* flask-sqlalchemy
* sqlalchemy-migrate
* docopt

## Running
You can easily start a development server using:

```python3 run.py```
