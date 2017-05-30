#!venv/bin/python
# delete_data_db.py - delete data in database
from app import db, models
print('deleting Users:')
users = db.session.query(models.User).delete()
db.session.commit()
print("%d users deleted." %users)

print('deleting Roles:')
roles = db.session.query(models.Role).delete()
db.session.commit()
print("%d roles deleted." %roles)

print('deleting Books:')
books = db.session.query(models.Book).delete()
db.session.commit()
print("%d books deleted." %books)

