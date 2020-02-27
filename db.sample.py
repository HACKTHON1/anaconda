from main import db,Message

db.session.add(Message("firstname"))
db.session.commit()

db.session.query(Message).all()

#[<Message 1>]

db.session.query(Message).all()[0].usermessage

#'firstname'

f= db.session.query(Message).all()[0]
f

#<Message 1>

f.usermessage="changemessage"
db.session.commit()
db.session.query(Message).all()[0].usermessage

# 'changemessage'
