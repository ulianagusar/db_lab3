import csv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from datetime import datetime, timedelta

DATABASE_URL = "postgresql://postgres:123456@localhost:5433/bd_lab_3"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def load_csv_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            moonrise = None
            if row['moonrise'] != 'No moonrise':
                moonrise = datetime.strptime(row['moonrise'], "%I:%M %p").time()
            moonset = None
            if  row['moonset'] != 'No moonset':
                moonset_time = datetime.strptime(row['moonset'], "%I:%M %p")
                if 'AM' in row['moonset']:
                    moonset = moonset_time.time()
                elif 'PM' in row['moonset']:
                    moonset = (moonset_time + timedelta(hours=12)).time()
            new_record = {
                'country': row['country'],
                'last_updated': datetime.strptime(row['last_updated'], "%Y-%m-%d %H:%M") if row['last_updated'] else None,
                'temperature': float(row['temperature_celsius']) if row['temperature_celsius'] else None,
                'wind_direction': row['wind_direction'],
                'moon_phase': row['moon_phase'],
                'moon_illumination': int(row['moon_illumination']) if row['moon_illumination'] else None,
                'moonset': moonset,
                'moonrise': moonrise,
                'sunset': datetime.strptime(row['sunset'], "%I:%M %p").time() if row['sunset'] else None,
                'sunrise': datetime.strptime(row['sunrise'], "%I:%M %p").time() if row['sunrise'] else None,
            }
            query = text("INSERT INTO weather_data (country, last_updated, temperature, wind_direction, moon_phase, moon_illumination, moonset, moonrise, sunset, sunrise) VALUES (:country, :last_updated, :temperature, :wind_direction, :moon_phase, :moon_illumination, :moonset, :moonrise, :sunset, :sunrise)")
            session.execute(query, new_record)
    session.commit()

load_csv_data('/Users/ulanagusar/Desktop/bd_lab3/GlobalWeather.csv')
