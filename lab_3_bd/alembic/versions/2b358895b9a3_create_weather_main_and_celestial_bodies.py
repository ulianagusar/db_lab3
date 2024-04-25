"""create weather_main and celestial_bodies

Revision ID: 2b358895b9a3
Revises: 84d93c317593
Create Date: 2024-04-24 22:46:17.505789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2b358895b9a3'
down_revision: Union[str, None] = '84d93c317593'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:


    op.create_table('celestial_bodies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('moon_phase', sa.String(length=50), nullable=True),
    sa.Column('moon_illumination', sa.Integer(), nullable=True),
    sa.Column('moonset', sa.Time(), nullable=True),
    sa.Column('moonrise', sa.Time(), nullable=True),
    sa.Column('sunset', sa.Time(), nullable=True),
    sa.Column('sunrise', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_main',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('wind_direction', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.execute("""
    INSERT INTO celestial_bodies (id, moon_phase, moon_illumination, moonset, moonrise, sunset, sunrise)
    SELECT id, moon_phase, moon_illumination, moonset, moonrise, sunset, sunrise FROM weather_data
    """)
    
    op.execute(
        """
        INSERT INTO weather_main (id, country, last_updated, temperature, wind_direction)
        SELECT id, country, last_updated, temperature, wind_direction
        FROM weather_data
        """
    )
    op.drop_table('weather_data')




def downgrade() -> None:

    op.create_table('weather_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('wind_direction', sa.String(length=50), nullable=True),
    sa.Column('moon_phase', sa.String(length=50), nullable=True),
    sa.Column('moon_illumination', sa.Integer(), nullable=True),
    sa.Column('moonset', sa.Time(), nullable=True),
    sa.Column('moonrise', sa.Time(), nullable=True),
    sa.Column('sunset', sa.Time(), nullable=True),
    sa.Column('sunrise', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.execute("""
    INSERT INTO weather_data (id, country, last_updated, temperature, wind_direction, moon_phase, moon_illumination, moonset, moonrise, sunset, sunrise)
    SELECT w.id, w.country, w.last_updated, w.temperature, w.wind_direction, c.moon_phase, c.moon_illumination, c.moonset, c.moonrise, c.sunset, c.sunrise
    FROM weather_main w
    JOIN celestial_bodies c ON w.id = c.id
    """)


    op.drop_table('weather_main')
    op.drop_table('celestial_bodies')

