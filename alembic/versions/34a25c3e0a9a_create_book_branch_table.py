"""Create book branch table

Revision ID: 34a25c3e0a9a
Revises: dd7286715ec3
Create Date: 2024-06-17 08:58:28.066016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34a25c3e0a9a'
down_revision: Union[str, None] = 'dd7286715ec3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('book_branch',
                    sa.Column('book_id', sa.String(length=36), nullable=False),
                    sa.Column('branch_id', sa.String(36), nullable=False),
                    sa.Column('quantity', sa.Integer, nullable=False),
                    sa.ForeignKeyConstraint(['book_id'], ['book.id']),
                    sa.ForeignKeyConstraint(['branch_id'], ['library_branch.id']),
                    )


def downgrade() -> None:
    op.drop_table('book_branch')
