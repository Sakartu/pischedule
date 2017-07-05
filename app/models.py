from app import db


class WeekSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    commandline = db.Column(db.String())
    runs = db.relationship('Run', backref='schedule', lazy='dynamic')


class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer())
    time = db.Column(db.Time())
    run_for = db.Column(db.Interval())
    schedule_id = db.Column(db.Integer, db.ForeignKey('week_schedule.id'))
