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
for i in session.query(Player).all():
    print (i.name)
    print (i.id)
    print (i.foot)
    print (i.position)
for j in session.query(Stat).all():
    print (j.totalkick)
    print (j.totalin)
    print (j.goal_in_pos_1)
    print (j.goal_in_pos_2)
    print (j.goal_in_pos_3)
    print (j.goal_in_pos_4)
    print (j.goal_in_pos_5)
    print (j.goal_in_pos_6)
    print (j.foot_contact_1)
    print (j.foot_contact_2)
    print (j.foot_contact_3)
    print (j.foot_contact_4)
    print (j.fieldgoal)
    print (j.best_goal_pos)
    print (j.best_feet)
    print (j.player.name)
