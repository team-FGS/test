import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'

    id = Column(String, primary_key=True)
    name = Column(String(250), nullable=False)
    foot = Column(String(1))
    position =Column(String(3))
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'foot': self.foot,
            'position':self.position
        }


class Stat(Base):
    __tablename__ = 'stat'

      
    totalkick=Column(Integer)
    totalin=Column(Integer)
    goal_in_pos_1=Column(Integer)
    goal_in_pos_2=Column(Integer)
    goal_in_pos_3=Column(Integer)
    goal_in_pos_4=Column(Integer)
    goal_in_pos_5=Column(Integer)
    goal_in_pos_6=Column(Integer)
    foot_contact_1=Column(Integer)
    foot_contact_2=Column(Integer)
    foot_contact_3=Column(Integer)
    foot_contact_4=Column(Integer)
    fieldgoal=Column(Float)
    best_goal_pos=Column(Integer)
    best_feet =Column(Integer)

    player_id = Column(String,ForeignKey('player.id'), primary_key=True)
    player=relationship(Player)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'player_id': self.player_id,
            'totalkick': self.totalkick,
            'totalin': self.totalin,
            'goal_in_pos_1': self.goal_in_pos_1,
            'goal_in_pos_2': self.goal_in_pos_2,
            'goal_in_pos_3': self.goal_in_pos_3,
            'goal_in_pos_4': self.goal_in_pos_4,
            'goal_in_pos_5': self.goal_in_pos_5,
            'goal_in_pos_6': self.goal_in_pos_6,
            'foot_contact_1': self.foot_contact_1,
            'foot_contact_2': self.foot_contact_2,
            'foot_contact_3': self.foot_contact_3,
            'foot_contact_4': self.foot_contact_4,
            'feildgoal':self.feildgoal,
            'best_goal_pos':self.best_goal_pos,
            'best_feet':self.best_feet
        }


engine = create_engine('sqlite:///playerdatabase.db')

Base.metadata.create_all(engine)