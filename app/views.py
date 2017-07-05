import calendar
import datetime

from flask import render_template, redirect, url_for, request, flash

from app import app, db
from app.forms import WeekScheduleForm

from app.models import WeekSchedule, Run


@app.route('/', methods=['GET'])
def show_schedules():
    schedules = WeekSchedule.query.all()
    return render_template('index.html', schedules=schedules)


@app.route('/add', methods=['GET', 'POST'])
def add_schedule():
    form = WeekScheduleForm()
    runs_modified = handle_run_deletion(form) or handle_run_addition(form)
    # If the form is correct (has a name, commandline and one or more Run's, we save it
    if not runs_modified and form.validate_on_submit():
        update_schedule(form)
        return redirect(url_for('show_schedules'))
    else:
        return render_template('show.html', add_schedule=True, form=form)


@app.route('/edit/<int:schedule_id>', methods=['GET', 'POST'])
def edit_schedule(schedule_id):
    schedule = WeekSchedule.query.filter_by(id=schedule_id).first()
    form = WeekScheduleForm(obj=schedule)
    runs_modified = handle_run_deletion(form) or handle_run_addition(form)
    if not runs_modified and form.validate_on_submit():
        update_schedule(form, schedule)
        return redirect('/edit/{0}'.format(schedule.id))
    return render_template('show.html', add_schedule=False, form=form)


def handle_run_deletion(form):
    # Yes this is slightly ugly, but due to the queue-like nature of FieldList there's no cleaner way
    modified = False
    new_runs = []
    try:
        while True:
            r = form.runs.pop_entry()
            if not r.del_run.data:
                new_runs.append(r.data)
            else:
                modified = True
    except IndexError:
        # no more runs
        pass
    if not new_runs:
        form.runs.append_entry()
        flash('A schedule needs to have at least one run!')
    else:
        for r in reversed(new_runs):
            form.runs.append_entry(r)
    return modified


def handle_run_addition(form):
    # Add an empty run if the user clicked Add Run
    if form.add_run.data:
        form.runs.append_entry()
        return True
    else:
        return False


def update_schedule(form, schedule=WeekSchedule()):
    schedule.name = form.name.data
    schedule.commandline = form.commandline.data
    for r in schedule.runs:
        db.session.delete(r)
    for r in form.runs:
        start = datetime.datetime.strptime(r.start.data, '%H:%M').time()
        stop = datetime.datetime.strptime(r.stop.data, '%H:%M').time()
        run = Run(day=r.day.data, start=start, stop=stop)
        schedule.runs.append(run)
        db.session.add(run)
    db.session.add(schedule)
    db.session.commit()
    return schedule


if __name__ == '__main__':
    app.run()
