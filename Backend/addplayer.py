from sqlalchemy import create_engine,exc
from sqlalchemy.orm import sessionmaker

from playerdatabasesetup import Base,Player,Stat

engine = create_engine('sqlite:///playerdatabase.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
def addplayer(name,rfid,foot,position):

    player1=Player(name=name,id=rfid,foot=foot,position=position)
    session.add(player1)
    session.commit()
    stat1=Stat(totalkick=0,totalin=0,goal_in_pos_1=0,goal_in_pos_2=0,goal_in_pos_3=0,goal_in_pos_4=0,goal_in_pos_5=0,goal_in_pos_6=0,
                foot_contact_1=0,foot_contact_2=0,foot_contact_3=0,foot_contact_4=0,fieldgoal=0,best_goal_pos=0,best_feet=0,player=player1)
    session.add(stat1)
    session.commit()
addplayer(name='Davee',rfid='aabbaaa',foot='L',position='SW')
addplayer(name='Dave',rfid='aaabbaa',foot='R',position='SR')
addplayer(name='Daee',rfid='aaaaaa',foot='L',position='SW')
addplayer(name='Dvee',rfid='bbaaa',foot='R',position='F')
print ('add success')
