"""create weather_data

Revision ID: 84d93c317593
Revises: 
Create Date: 2024-04-24 22:12:08.835165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84d93c317593'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

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



def downgrade() -> None:

    op.drop_table('weather_data')

