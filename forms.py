"""Forms for adoption-agency"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Email,URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = SelectField("Species",
                choices=[("cat","Cat"),("dog","Dog"),("porcupine","Porcupine")],)
    photourl = StringField("Photo URL",
                            validators=[Optional(),URL()],)
    age = IntegerField("Age",
                        validators=[Optional(),NumberRange(min=0,max=30)],)
    notes = TextAreaField( "Notes",
                         validators=[Optional(), Length(min=10)],
    )
    

class EditPetForm(FlaskForm):
    """Form to edit pet"""

    photourl = StringField("Photo URL",
                            validators=[Optional(),URL()],)
    notes = TextAreaField("Notes",
                          validators=[Optional(), Length(min=10)],)
    available = BooleanField("Available?")