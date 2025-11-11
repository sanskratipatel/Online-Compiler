"""recreate_users_table

Revision ID: a7e7d29f2fe5
Revises: bf2305cd131f
Create Date: 2025-11-11 19:10:25.217457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7e7d29f2fe5'
down_revision: Union[str, Sequence[str], None] = 'bf2305cd131f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop old table if it exists
    op.execute("DROP TABLE IF EXISTS users;")

    # Create new table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, server_default='1'),
    )

def downgrade():
    op.drop_table('users')
