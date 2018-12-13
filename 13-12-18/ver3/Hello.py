from flask import Flask
from flask import render_template, jsonify,  abort, flash, redirect,request, url_for

from flask import session
from  db  import *


app = Flask(__name__)
app.secret_key = '1234'

def decodeCmd( cmd):
    device = cmd[0]
    _status = cmd[1]
    status = ''
    value1 = int(cmd[2:4],16)
    dec1 =  int(cmd[4:6],16)
    value2 = int(cmd[6:8],16)
    dec2 = int(cmd[8:],16)
    param_2 = ''
    
    dev = db_session.query(db.devices).get(int(device))
    
    
    if device == '1':
        # 1 = Fan
        if _status == '1':
            dev.param_1 = 'Level: ' + str(value1)
            dev.status = 'ON'
        else:
            dev.param_1 = '0'
            dev.status = 'OFF'
        
        db_session.commit()

    elif device == '2':
        # 2 = Airconditioner
        if _status == '1':
            dev.param_1 = str(value1) + '.' + str(dec1) + ' degrees celsius'
            dev.status = 'ON'
        else:
            dev.param_1 = 'undetected'
            dev.status = 'OFF'
        
        db_session.commit()

    elif device == '3':
        # 3 = Kettle
        print(3)
        if _status == '1':
            dev.status = 'ON'
            dev.param_2 = str(value2) + '.' + str(dec2) + ' degrees celsius'
            if value1 == '1':
                dev.param_1 = 'Boiled'
            else:
                dev.param_1 = 'Warming'
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'undetected'

        db_session.commit()


    elif device == '4':
        # 4 = Television
        if _status == '1':
            dev.status = 'ON'
            dev.param_1 = 'Channel: ' + str(value1)
            dev.param_2 = 'Sound Volume: ' + str(value2)
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'OFF'

        db_session.commit()

    elif device == '5':
        # 5 = Radio
        if status == '1':
            dev.status = 'ON'
            dev.param_1 = str(value1) + '.' + str(dec1)
            dev.param_2 = str(value2)
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'OFF'
        db_session.commit()


@app.route('/')
@app.route('/main')
def main():
    if not session.get('logged_in'):
        return redirect('/login_form')
    return render_template('main.html')

@app.route('/login_form')
def login_form():
    if session.get('logged_in'):
        print("login_form ....", session.get('logged_in'))
        return redirect(url_for('home'))

    return render_template('login.html')

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
    return render_template('gorf.html')

@app.route('/status')
def status():
    devices = db_session.query(db.devices).filter(db.devices.managed==1).all()
    return render_template('status.html', devices= devices)

@app.route('/settings')
def settings():
    gestures = db_session.query(db.gestures).all()
    devices = db_session.query(db.devices).filter(db.devices.managed==0).all()
    return render_template('setting.html', gestures=gestures, devices=devices)

@app.route('/manage_device/<int:gesture_id>/<int:device_id>')
def manage_device(gesture_id, device_id):
    gesture = db_session.query(db.gestures).get(gesture_id)
    old_device_id = gesture.device_id
    gesture.device_id = device_id

    old_device = db_session.query(db.devices).get(old_device_id)
    if old_device is not None :
        old_device.managed = 0
    device = db_session.query(db.devices).get(device_id)
    if device is not None :
        device.managed = 1

    db_session.commit()

    gestures = db_session.query(db.gestures).all()
    devices = db_session.query(db.devices).filter(db.devices.managed==0).all()

    return render_template('setting.html', gestures=gestures, devices=devices)

@app.route('/settingsandstatus')
def sands():
    return render_template('sands.html')

@app.route('/command/<cmd>')
def command(cmd):
    decodeCmd(cmd)
    return "result=ok"
           
if __name__ == '__main__':
   app.run(debug=True)
