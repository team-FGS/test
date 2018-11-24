from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from playerdatabasesetup import Base, Player, Stat
#from databasetest import Base,Restaurant,MenuItem
app = Flask(__name__)

engine = create_engine('sqlite:///playerdatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/football')
def football():
    
    player=session.query(Player).all()
    stat=session.query(Stat).all()
    return render_template('mainfootball.html',playerS=player,statS=stat)
    #return "<h1>hi</h1>"

@app.route('/football/register')
def footballRegister():

    return render_template('football_register.html')
if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)