from flask_wtf import FlaskForm, validators
from wtforms import StringField, BooleanField, FieldList, FormField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class RunForm(FlaskForm):
    day = SelectField('Day', choices=((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')))
    start = StringField('Start', validators=[DataRequired()], default='00:00')
    stop = StringField('Stop', validators=[DataRequired()], default='00:00')
    del_run = SubmitField('Delete')


class WeekScheduleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    commandline = StringField('Commandline', validators=[DataRequired()])
    runs = FieldList(FormField(RunForm), min_entries=1, max_entries=10)
    add_run = SubmitField()

