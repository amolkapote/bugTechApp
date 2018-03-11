'''
    @author: AK
    @summary: main app to handle all user requests
'''

from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Contact, Bug
from forms import ContactForm, BugForm

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('bugs'))


@app.route("/new_contact", methods=('GET', 'POST'))
def new_contact():
    '''
    Create new contact
    '''
    form = ContactForm()
    if form.validate_on_submit():
        my_contact = Contact()
        form.populate_obj(my_contact)
        db.session.add(my_contact)
        try:
            db.session.commit()
            # User info
            flash('Contact created correctly', 'success')
            return redirect(url_for('contacts'))
        except:
            db.session.rollback()
            flash('Error generating contact.', 'danger')

    return render_template('web/new_contact.html', form=form)

@app.route("/new_bug", methods=('GET', 'POST'))
def new_bug():
    '''
    Create new bug
    '''
    form = BugForm()
    if form.validate_on_submit():
        my_bug = Bug()
        form.populate_obj(my_bug)
        db.session.add(my_bug)
        try:
            db.session.commit()
            # User info
            flash('Bug created correctly', 'success')
            return redirect(url_for('bugs'))
        except:
            db.session.rollback()
            flash('Error generating bug.', 'danger')

    return render_template('web/new_bug.html', form=form,users=[])

@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    '''
    Edit contact

    :param id: Id from contact
    '''
    my_contact = Contact.query.filter_by(id=id).first()
    form = ContactForm(obj=my_contact)
    if form.validate_on_submit():
        try:
            # Update contact
            form.populate_obj(my_contact)
            db.session.add(my_contact)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update contact.', 'danger')
    return render_template(
        'web/edit_contact.html',
        form=form)

@app.route("/edit_bug/<id>", methods=('GET', 'POST'))
def edit_bug(id):
    '''
    Edit contact

    :param id: Id from bug
    '''
    my_bug = Bug.query.filter_by(id=id).first()
    form = BugForm(obj=my_bug)
    if form.validate_on_submit():
        try:
            # Update contact
            form.populate_obj(my_bug)
            db.session.add(my_bug)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update contact.', 'danger')
    return render_template('web/edit_bug.html', form=form)

@app.route("/contacts")
def contacts():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/bugs")
def bugs():
    '''
    Show alls bugs
    '''
    bugList = Bug.query.order_by(Bug.id).all()
    bugs=[]
    for bug in bugList:
        contact = Contact.query.filter_by(id=bug.user).first()
        bugs.append(dict(id=bug.id,
                         title=bug.title,
                         desc=bug.desc,
                         user=contact.name,
                         status=bug.status,
                         date=bug.date)
            )
        
    return render_template('web/bugs.html', bugs=bugs)

@app.route("/search")
def search():
    
    name_search = request.args.get('name')
    all_contacts = Contact.query.filter(
        Contact.name.contains(name_search)
        ).order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts=all_contacts)


@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    
    try:
        mi_contacto = Contact.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_contacto)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  contact.', 'danger')

    return redirect(url_for('contacts'))


if __name__ == "__main__":
    app.run()
