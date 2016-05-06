
import sqlite3
from flask import g


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('mydb.sqlite')
        
        db.execute('CREATE TABLE IF NOT EXISTS sales(title,firstname,surname,organisation,email,telepone,carmileage,carmodel,carmake,careregistration,carregdate,comment)')
        
        db.commit()
        
    return db
