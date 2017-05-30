#!venv/bin/python
# read_db.py - read database
from app import db, models
users = models.User.query.all()
print('Users:')
for user in users:
    print(user.id, user.username, user.role.name)
print

print('Roles:')
roles = models.Role.query.all()
for role in roles:
    print('%r\t%r\t Default=%r\tCan Modify=%r' 
        %(role.id, role.name, role.default, role.can_modify))
print

print('Books:')
books = models.Book.query.order_by('author').all()
for book in books:
    print('%r\t%r\t%r\t%r\t%r' 
        %(book.id, book.author, book.title, book.category, book.copies))
print
