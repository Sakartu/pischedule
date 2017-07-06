#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Usage:
run_tasks.py [-d]

Options:
-d      Delete all tasks from the crontab
"""

from app import models, app
import subprocess
from docopt import docopt

__author__ = 'peter'

CRONTAB = '/usr/bin/crontab'


def define_cronspec(time, day, cmd):
    return '\t'.join((str(time.minute), str(time.hour), '*', '*', str(day), cmd)) + '\n'


def main():
    args = docopt(__doc__)
    schedules = models.WeekSchedule.query.all()
    orig_crontab = subprocess.check_output([CRONTAB, '-l'])
    sep = app.config.get('CRONTAB_SEPARATOR').encode('utf8')
    if sep in orig_crontab:
        pieces = orig_crontab.split(b'# ' + sep + b'\n')
    else:
        pieces = (orig_crontab, b'', b'')
    orig_head = pieces[0]
    orig_tail = pieces[2]

    jobs = b''
    if not args['-d']:
        for schedule in schedules:
            jobs += b'# ' + app.config.get('CRONTAB_SEPARATOR').encode('utf8') + b'\n'
            for run in schedule.runs:
                cronspec = define_cronspec(run.start, run.day, schedule.start_cmd)
                cronspec += define_cronspec(run.stop, run.day, schedule.stop_cmd)
                jobs += cronspec.encode('utf8')
            jobs += b'# ' + app.config.get('CRONTAB_SEPARATOR').encode('utf8') + b'\n'
    full_tab = orig_head + jobs + orig_tail
    process = subprocess.Popen([CRONTAB, '-'], stdin=subprocess.PIPE)
    process.communicate(full_tab)


if __name__ == '__main__':
    main()

