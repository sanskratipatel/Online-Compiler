"""create_users_table

Revision ID: bf2305cd131f
Revises: 
Create Date: 2025-11-11 19:03:19.899978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf2305cd131f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), unique=True, nullable=False),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )

def downgrade():
    op.drop_table('users')
