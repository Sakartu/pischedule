from flask import render_template, redirect, url_for, request, flash

from app import app, db
from app.forms import WeekScheduleForm

from app.models import WeekSchedule


@app.route('/', methods=['GET'])
def show_schedules():
    schedules = WeekSchedule.query.all()
    return render_template('index.html', schedules=schedules)


@app.route('/show/<schedule_id>', methods=['GET', 'POST'])
def show_schedule(schedule_id=1):
    schedule = WeekSchedule.query.filter_by(id=schedule_id).first()
    form = WeekScheduleForm(obj=schedule)
    # Yes this is slightly ugly, but due to the queue-like nature of FieldList there's no cleaner way
    new_runs = []
    try:
        while True:
            r = form.runs.pop_entry()
            if not r.del_run.data:
                new_runs.append(r.data)
    except IndexError:
        # no more runs
        pass
    if not new_runs:
        flash('A schedule needs to have at least one run!')
    else:
        for r in reversed(new_runs):
            form.runs.append_entry(r)
    # Add an empty run if the user clicked Add Run
    if form.add_run.data:
        form.runs.append_entry()
    # If the form is correct (has a name, commandline and one or more Run's, we save it
    if form.validate_on_submit():
        schedule.name = form.name.data
        schedule.commandline = form.commandline.data
        db.session.add(schedule)
        db.session.commit()
        return redirect(url_for('show_schedule', schedule_id=schedule.id))
    return render_template('show.html', form=form)


@app.route('/add', methods=['GET'])
def add_schedule():
    schedule = WeekSchedule()
    db.session.add(schedule)
    db.session.commit()
    return redirect('/show/{0}'.format(schedule.id))


if __name__ == '__main__':
    app.run()
