#!/usr/bin/python3
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://alx_workflow:Alx_2025@localhost/hbtn_0e_0_usa")

engine.connect()




print(engine)