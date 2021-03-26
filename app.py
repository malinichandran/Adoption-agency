from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm
from forms import EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show Homepage"""

    pets =  Pet.query.all()
    return render_template("home.html",pets=pets)

@app.route("/add", methods=["GET", "POST"])
def addpetpage():
    """Add Pet Form; Handle the form data"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photourl = form.photourl.data
        age = form.age.data
        notes = form.notes.data
        
        db.session.add(Pet(name=name,species=species,
                        photo_url=photourl,age=age,
                        notes=notes))
        db.session.commit()
        flash(f"Added new pet {name}")
        return redirect("/")
    
    else:
        return render_template("add_pet_form.html",form=form)


@app.route("/pets/<int:pid>/edit", methods=["GET","POST"])
def display_edit_pet(pid):
    """Display information about a pet. Edit pet info"""

    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photourl.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect(f"/pets/{pid}/edit")

    else:
        return render_template("edit_pet_form.html",form=form)
