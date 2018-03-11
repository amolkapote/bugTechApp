'''
@author: AK
@summary: 
'''
import unittest
import app

from models import db, Contact, Bug



class TestModelObjects(unittest.TestCase):


    def setup(self):
        # Connect to the database and create the schema within a transaction
        # Database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.sqlite'

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

    def teardown(self):
        # Roll back the top level transaction and disconnect from the database
        db.session.rollback()
        db.session.close()


    def testModelObjects(self):
        my_contact = Contact(name='amol11', surname='surname', email='amolkapote@my.com', phone='34342343')
        db.session.add(my_contact)
        contact = Contact.query.filter_by(name=my_contact.name).first()
        self.assertEqual(my_contact.name, contact.name)
        self.assertEqual(my_contact.surname, contact.surname)
        self.assertEqual(my_contact.email, contact.email)
        self.assertEqual(my_contact.phone, contact.phone)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()