"""Create author table

Revision ID: 29e2bec6e177
Revises: 
Create Date: 2024-06-15 09:19:05.427795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '29e2bec6e177'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('author',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('birthdate', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_index(op.f('ix_author_id'), 'author', ['id'], unique=True)
    op.create_index('ix_author_birthdate', 'author', ['birthdate'], unique=False)


def downgrade() -> None:
    # Check out create_index
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_birthdate'), table_name='author')
    op.drop_index(op.f('ix_author_id'), table_name='author')
    op.drop_table('author')
