"""add content column to posts table

Revision ID: e66d4d7141bd
Revises: 7b0f4b383ce7
Create Date: 2025-11-26 18:49:23.288999

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e66d4d7141bd'
down_revision: Union[str, Sequence[str], None] = '7b0f4b383ce7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
  sa.Column('content', sa.String(), nullable=False))



def downgrade() -> None:
    op.drop_column('posts', 'content')

