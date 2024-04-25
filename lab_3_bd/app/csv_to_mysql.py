import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Time, Boolean, Float, DateTime
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Time, Boolean, Float, DateTime
Base = declarative_base()

class CelestialBodies(Base):
    __tablename__ = 'celestial_bodies'
    id = Column(Integer, primary_key=True)
    moon_phase = Column(String(50))
    moon_illumination = Column(Integer)
    moonset = Column(Time)
    moonrise = Column(Time)
    sunset = Column(Time)
    sunrise = Column(Time)
    is_safe_to_go_out = Column(Boolean)

class WeatherMain(Base):
    __tablename__ = 'weather_main'
    id = Column(Integer, primary_key=True)
    country = Column(String(100))
    last_updated = Column(DateTime)
    temperature = Column(Float)
    wind_direction = Column(String(100))


engine = create_engine('mysql+pymysql://uliana:2006Uliana@localhost:3306/weather_bd_mysql')
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

def import_csv_to_table(filename, table_class):
    df = pd.read_csv(filename)
    df = df.where(pd.notna(df), None)
    records = df.to_dict(orient='records')
    
    for record in records:
        obj = table_class(**record)
        session.merge(obj) 
    
    session.commit()


import_csv_to_table('celestial_bodies.csv', CelestialBodies)
import_csv_to_table('weather_main.csv', WeatherMain)

session.close()

