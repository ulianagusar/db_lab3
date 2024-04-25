from sqlalchemy import Column, Integer, String, Boolean, Time, create_engine, DateTime , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
from sqlalchemy import Enum
from sqlalchemy import Column, Integer, String, Boolean, Time, DateTime, Float, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WindDirection(PyEnum):
    ENE = "East-Northeast"
    SSW = "South-Southwest"
    WSW = "West-Southwest"
    NNW = "North-Northwest"
    W = "West"
    E = "East"
    S = "South"
    N = "North"
    NW = "Northwest"
    SW = "Southwest"
    SE = "Southeast"
    NE = "Northeast"
    ESE = "East-Southeast"
    NNE = "North-Northeast"
    SSE = "South-Southeast"
    WNW = "West-Northwest"


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
    wind_direction = Column(Enum(WindDirection), default='N')



# class WeatherData(Base):
#     __tablename__ = 'weather_data'
#     id = Column(Integer, primary_key=True)
#     country = Column(String(100))
#     last_updated = Column(DateTime)
#     temperature = Column(Float)
#     wind_direction = Column(Enum(WindDirection), default=WindDirection.N)
    
#     moon_phase = Column(String(50))
#     moon_illumination = Column(Integer)
#     moonset = Column(Time)
#     moonrise = Column(Time)
#     sunset = Column(Time)
#     sunrise = Column(Time)


engine = create_engine('mysql+pymysql://uliana:2006Uliana@localhost:3306/weather_bd_mysql', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)