'''
    @author: AK
    @summary: form object for User & Bug 
'''


from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email, Length
from models import Contact

class NonValidatingSelectField(SelectField):
    """
    Attempt to make an open ended select multiple field that can accept dynamic
    choices added by the browser.
    """
    def pre_validate(self, form):
        pass
    
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    surname = StringField('Surname', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    email = StringField('E-Mail', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    phone = StringField('Phone', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])
    
class BugForm(FlaskForm):
    # loading user list
    def __init__(self,obj=None):
        super(BugForm,self).__init__(obj=obj)
        contacts = Contact.query.order_by(Contact.name).all()
        allUsers =[(contact.id,contact.name) for contact in contacts]
        self.user.choices = allUsers
        
    title = StringField('Title', validators=[DataRequired(), Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    desc = StringField('Description', validators=[Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    status = SelectField('Status', choices=[('open','Open'),('close','Closed')])
    user = NonValidatingSelectField('User')
