from flask_wtf import FlaskForm, validators
from wtforms import StringField, BooleanField, FieldList, FormField, SelectField, IntegerField, SubmitField, Form, \
    HiddenField
from wtforms.validators import DataRequired, Length, NumberRange


class RunForm(Form):
    id = HiddenField()
    day = SelectField('Day', choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], validators=[NumberRange(0, 6)], coerce=int, default=0)
    start = StringField('Start', validators=[DataRequired()], default='00:00')
    stop = StringField('Stop', validators=[DataRequired()], default='00:00')
    del_run = SubmitField('Delete')


class WeekScheduleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], default='foo')
    commandline = StringField('Commandline', validators=[DataRequired()], default='bar')
    runs = FieldList(FormField(RunForm), min_entries=1, max_entries=10)
    add_run = SubmitField()

