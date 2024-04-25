import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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


engine = create_engine('postgresql://postgres:123456@localhost:5433/bd_lab_3') 
Session = sessionmaker(bind=engine)
session = Session()

def export_to_csv(session, table_class, filename):
    """Експорт таблиці до файлу CSV."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        results = session.query(table_class).all()
        # Запис заголовків
        writer.writerow([column.name for column in table_class.__table__.columns])
        # Запис рядків
        for result in results:
            writer.writerow([getattr(result, column.name) for column in table_class.__table__.columns])


export_to_csv(session, CelestialBodies, 'celestial_bodies.csv')
export_to_csv(session, WeatherMain, 'weather_main.csv')


session.close()




