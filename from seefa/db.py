from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.orm import relation
from sqlalchemy import Table, Sequence, Column, ForeignKey, MetaData
from sqlalchemy.types import String, Unicode, UnicodeText, Integer, DateTime, \
                             Boolean, Float
from sqlalchemy.orm import mapper
from sqlalchemy.orm import class_mapper
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.sql.expression import *
from sqlalchemy.orm import joinedload

#from sqlalchemy.ext.automap import automap_base

from collections import OrderedDict
from datetime import datetime,date,time 

from cfg import *

import logging
log = logging.getLogger('printlog')

import sys

db = sys.modules[__name__]
#print db



mappers = {}

#engine = create_engine('pymysql://root:@cat20@119.59.121.79:3306/tourist_buddy?charset=utf8&use_unicode=1')
#engine = create_engine(DB_URI, pool_size=50,max_overflow=-1, echo=True)
#engine = create_engine(DB_URI, pool_size=50,max_overflow=-1)
engine = create_engine(DB_URI,  pool_size=50, pool_recycle=3600, pool_pre_ping=True)
Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
db_session = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine
Base.query = db_session.query_property()

# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# Base.metadata.bind = engine
# Base.query = db_session.query_property()
# print Base.classes
# for c in Base.classes:
#     print c


class DictSerializable(object):
  
    def _asdict(obj):
        #print "_asdict"
        result = {}
        for col in class_mapper(obj.__class__).mapped_table.c:
            #print col.name,type(getattr(obj, col.name))
            if type(getattr(obj, col.name)) is datetime:
                #result[col.name] = getattr(obj. col.name)
                d = getattr(obj, col.name)
                result[col.name] = d.strftime('%Y-%m-%d %H:%M:%S')
            elif type(getattr(obj, col.name)) is date:
                #result[col.name] = getattr(obj. col.name)
                d = getattr(obj, col.name)
                result[col.name] = d.strftime('%Y-%m-%d')
            elif type(getattr(obj, col.name)) is time:
                #result[col.name] = getattr(obj. col.name)
                d = getattr(obj, col.name)
                result[col.name] = d.strftime('%H:%M:%S')
            else :
                result[col.name] = getattr(obj, col.name)
        return result

    @classmethod
    def all(cls):
        return db_session.query(cls).all()
    
    @classmethod
    def add_column(cls, *args, **kwargs):
        return db_session.query(cls).add_column(*args, **kwargs)
    
    @classmethod
    def count(cls):
        return db_session.query(cls).count()
    
    @classmethod
    def order_by(cls, *args, **kwargs):
        return db_session.query(cls).order_by(*args, **kwargs)
    
    @classmethod
    def filter_by(cls, **kwargs):
        return db_session.query(cls).filter_by(**kwargs)
    
    @classmethod
    def filter(cls, *args):
        return db_session.query(cls).filter(*args)
    
    @classmethod
    def get(cls, id):
        return db_session.query(cls).get(id)
    
    @classmethod
    def query(cls):
        return db_session.query(cls)
    
    @classmethod
    def first(cls):
        return db_session.query(cls).first()
    
    @classmethod
    def insert(cls, **kwargs):
        try:
            instemp = cls(**kwargs)
            db_session.add(instemp)
            #db_session.commit()
            return instemp
        except:
            print("[SQLasagna] Insert Error: " + str(sys.exc_info()))
            #db_session.rollback()
            return False
    
    def save(self):
        try:
            db_session.add(self)
            #db_session.commit()
            return True
        except:
            print("[SQLasagna] ORM Save Error: " + str(sys.exc_info()))
            #db_session.rollback()
            return False
    
    def delete(self):
        try:
            if self.id:
                db_session.delete(self)
             #   db_session.commit()
            else:
                return False
            
            return True
        except:
            print("[SQLasagna] Delete Error: " + str(sys.exc_info()))
            #db_session.rollback()
            return False


def getMapName(table_name):
    return "".join([name.title() for name in table_name.split('_')])

def create_map(table):
    print ('[db.py] mapping', table.name)
    name = str(table.name)
    c = type(name, (DictSerializable,) , {})


    if table.name.startswith('vw'):
        mapper(c, table, primary_key=[table.c.id])
    else :
        mapper(c, table)

    setattr(db, name, c) 
    mappers[name] = table


def getTable(name):
    return mappers[name]

def getColumnsName(name):
    table = getTable(name)
    return [  c.name for c in table.columns]

def getColumns(name):
    table = getTable(name)
    return table.columns

def getModel(name):
    return getattr(db, name)


def getField(table_filed):
    return eval(table_field)



metadata = MetaData(bind=engine)
metadata.reflect(bind=engine,views=True)

tables = metadata.tables


#for key, table in tables.iteritems():
for key, table in tables.items():
    create_map(table)


for table in tables:
    # Now we map all relationships
    print("[db.py] Mapping Relationships for %s." % table)
    
    for fk in tables.get(table).foreign_keys:
        print (fk.target_fullname)

        fkn = fk.target_fullname.split('.')[0]
        if fkn != table:
            try:
                class_mapper(getattr(db, table))._configure_property(fkn, relationship(getattr(db, fkn), backref=table ))
            except :
                print("[db.py] Problem mapping relationships for %s." % table)
                print(sys.exc_info())
                print("[db.py] Re-Mapping Table %s." % table)
                setattr(db, table, type(str(table), (Base, DictSerializable), {}))
                #create_map(table)

        else:
            print("[db.py] Not mapping relationship %s into table %s because it is already mapped." %(fkn, table))



