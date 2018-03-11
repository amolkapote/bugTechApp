'''
    @author: AK
    @summary: faker class to create initial random users
    
'''


from models import db, Contact
from faker import Factory

# create a factor object
fake = Factory.create()

# Reload tables
db.drop_all()
db.create_all()
''''

year = random.choice(range(1950, 2001))
month = random.choice(range(1, 13))
day = random.choice(range(1, 29))
birth_date = datetime(year, month, day)
'''
# Make 5 fake contacts
for num in range(5):
    fullname = fake.name().split()
    name = fullname[0]
    surname = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    mi_contacto = Contact(name=name, surname=surname, email=email, phone=phone)
    db.session.add(mi_contacto)
    db.session.commit()
'''
# Make 5 fake bugs
for num in range(5):
    title = 'title1'
    desc = 'desc1'
    date = datetime(year, month, day).strftime('%m/%d/%Y')
    user = '1'
    status = 'open'
    # Save in database
    mi_bug = Bug(title=title, desc=desc, date=date, user=user, status=status)
    db.session.add(mi_bug)
    db.session.commit()
'''
