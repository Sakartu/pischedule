from flask_wtf import FlaskForm, validators
from wtforms import StringField, BooleanField, FieldList, FormField, SelectField, IntegerField, SubmitField, Form, \
    HiddenField
from wtforms.validators import DataRequired, Length, NumberRange


class RunForm(Form):
    id = HiddenField()
    day = SelectField('Day', choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], validators=[NumberRange(1, 7)], coerce=int, default=1)
    start = StringField('Start', validators=[DataRequired()], default='00:00')
    stop = StringField('Stop', validators=[DataRequired()], default='00:00')
    del_run = SubmitField('Delete')


class WeekScheduleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_cmd = StringField('Start command', validators=[DataRequired()])
    stop_cmd = StringField('Stop command', validators=[DataRequired()])
    runs = FieldList(FormField(RunForm), min_entries=1, max_entries=10)
    add_run = SubmitField()

