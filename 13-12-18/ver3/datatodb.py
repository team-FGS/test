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
    temperature = ''
    channel = ''
    sound_volume = ''
    boiling_status = ''
    level = ''

    dev = db_session.query(db.devices).get(int(device))


    if device == '1':
        # 1 = Fan
        if _status == '1':
            dev.param_1 = 'Level: ' + str(value1)
            dev.status = 'ON'
            dev.level = 'Level: ' + str(value1)
        else:
            dev.param_1 = '0'
            dev.status = 'OFF'
            dev.level = '0'        
        db_session.commit()

    elif device == '2':
        # 2 = Airconditioner 
        if _status == '1':
            dev.param_1 = 'Temperature: ' + str(value1) + '.' + str(dec1) + ' degrees celsius'
            dev.status = 'ON'
            dev.temperature = 'Temperature: ' + str(value1) + '.' + str(dec1) + ' degrees celsius'
        else:
            dev.param_1 = 'undetected'
            dev.status = 'OFF'
            dev.temperature = 'undetected'
        db_session.commit()

    elif device == '3':
        # 3 = Kettle
        print(3)
        if _status == '1':
            dev.status = 'ON'
            dev.param_2 = 'Temperature: ' + str(value2) + '.' + str(dec2) + ' degrees celsius'
            dev.temperature = 'Temperature: ' + str(value2) + '.' + str(dec2) + ' degrees celsius'
            if value1 == '1':
                dev.param_1 = 'Boiled'
                dev.boiling_status = 'Boiled'
            else:
                dev.param_1 = 'Warming'
                dev.boiling_status = 'Warming'
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'undetected'
            dev.temperature = 'undetected'
        db_session.commit()


    elif device == '4':
        # 4 = Television
        if _status == '1':
            dev.status = 'ON'
            dev.param_1 = 'Channel: ' + str(value1)
            dev.param_2 = 'Sound Volume: ' + str(value2)
            dev.channel = 'Channel: ' + str(value1)
            dev.sound_volume = 'Sound Volume: ' + str(value2)
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'OFF'
            dev.channel = 'Channel: OFF'
            dev.sound_volume = 'Volume: OFF'
        
        db_session.commit()

    elif device == '5':
        # 5 = Radio
        if status == '1':
            dev.status = 'ON'
            dev.param_1 = str(value1) + '.' + str(dec1)
            dev.param_2 = str(value2)
            dev.channel = 'Channel: ' + str(value1) + '.' = str(dec1)
            dev.sound_volume = 'Sound Volume: ' + str(value2)
        else:
            dev.status = 'OFF'
            dev.param_1 = 'OFF'
            dev.param_2 = 'OFF'
            dev.channel = 'OFF'
            dev.sound_volume = 'OFF'
        db_session.commit()