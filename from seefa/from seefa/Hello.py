from flask import Flask
from flask import render_template, jsonify, session, abort, flash, redirect,request
from  db  import *


app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')

@app.route('/main')
def main():
    if not session.get('logged_in'):
        return redirect('/login_form')
    return render_template('main.html')

@app.route('/login_form')
def login_form():
    return render_template('1.html')

@app.route('/login', methods=["POST"])
def login():
    print("login ")
    print (request.form.get("pass"))
    if request.form.get("pass") == '1234' :
        session['logged_in'] = True
        return redirect('/home')
    else :
        flash("wrong password")
        return redirect('/login_form')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/login_form')

@app.route('/home')
def home():
    return render_template('2.html')

@app.route('/kick/<rf_id>/<ball_pos>/<goal_pos>')
def kick(rfid, ball_pos, goal_pos):
    print (rfid, ball_pos, goal_pos)

    kick = db.kick()
    kick.rfid = rfid
    kick.ball_pos = ball_pos
    kick.goal_pos = goal_pos
    db_session.add(kick)
    db_session.commit()

    f = db_session.query(db.football).filter(db.football == rfid).first()
    if f == None :
        f = db.football()
        f.rfid = rfid
        db_session.add(f)

    if ball_pos == 1 :
        f.contract_1 = f.contract_1 +1
    elif ball_pos == 2:
        f.contract_2 = f.contract_2 + 1
    else :
        f.contract_3 = f.contract_3 +1

    db_session.commit()

    return "ok"

@app.route('/ctrl/<device_id>/<status>')
def ctrl(device_id, status):
   d = db_session.query(db.managed_device).get(device_id)
   d.status = status
   db_session.commit()
   return "ok"

@app.route('/get_command/<gesture_id>')
def get_command(gesture_id):
   d = db_session.query(db.gesture).get(gesture_id)
   return jsonify(device=d.device_id, status=d.status)



if __name__ == '__main__':
   app.run(debug=True)
