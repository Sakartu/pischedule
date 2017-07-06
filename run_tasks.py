#!/usr/bin/env python3
# -*- coding: utf8 -*-

from app import models, app
import subprocess

__author__ = 'peter'

CRONTAB = '/usr/bin/crontab'


def main():
    schedules = models.WeekSchedule.query.all()
    orig_crontab = subprocess.check_output([CRONTAB, '-l'])
    sep = app.config.get('CRONTAB_SEPARATOR').encode('utf8')
    if sep in orig_crontab:
        pieces = orig_crontab.split(b'# ' + sep + b'\n')
    else:
        pieces = (orig_crontab, b'', b'')
    orig_head = pieces[0]
    orig_tail = pieces[2]

    for schedule in schedules:
        jobs = b'# ' + app.config.get('CRONTAB_SEPARATOR').encode('utf8') + b'\n'
        for run in schedule.runs:
            cronspec = '\t'.join((str(run.start.minute), str(run.start.hour), '*', '*', str(run.day), schedule.start_cmd))
            jobs += cronspec.encode('utf8') + b'\n'
        jobs += b'# ' + app.config.get('CRONTAB_SEPARATOR').encode('utf8') + b'\n'
        full_tab = orig_head + jobs + orig_tail
        process = subprocess.Popen([CRONTAB, '-'], stdin=subprocess.PIPE)
        process.communicate(full_tab)


if __name__ == '__main__':
    main()