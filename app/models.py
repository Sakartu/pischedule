from app import db


class WeekSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    commandline = db.Column(db.String())
    runs = db.relationship('Run', lazy='dynamic', cascade="delete, delete-orphan")


class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer())
    start = db.Column(db.Time())
    stop = db.Column(db.Time())
    schedule_id = db.Column(db.Integer, db.ForeignKey('week_schedule.id'))
