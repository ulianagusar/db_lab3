"""add is_safe_to_go_out

Revision ID: 0212abdb3b26
Revises: 2b358895b9a3
Create Date: 2024-04-24 23:40:50.620490

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0212abdb3b26'
down_revision: Union[str, None] = '2b358895b9a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column('celestial_bodies', sa.Column('is_safe_to_go_out', sa.Boolean(), nullable=True))
    op.execute("""
    UPDATE celestial_bodies
    SET is_safe_to_go_out = CASE
        WHEN moon_phase = 'Full moon' THEN False
        ELSE True
    END
    """)


def downgrade() -> None:

    op.drop_column('celestial_bodies', 'is_safe_to_go_out')

