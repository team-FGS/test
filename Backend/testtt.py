from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from playerdatabasesetup import Base, Player, Stat

app = Flask(__name__)

engine = create_engine('sqlite:///playerdatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
@app.route('/')
@app.route('/football')
def football():
    player=session.query(Player).all()
    #stat=session.query(Stat).all()
    #return render_template('mainfootball.html',playerS=player)
    return "<h1>hi</h1>"

@app.route('/football/register')
def footballRegister():
    return "<h1> this page register football </h1>"

if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0')