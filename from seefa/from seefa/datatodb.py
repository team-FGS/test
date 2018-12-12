from db import *

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