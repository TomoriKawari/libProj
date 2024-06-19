"""Create book table

Revision ID: dd7286715ec3
Revises: ff12555fb78c
Create Date: 2024-06-15 09:21:29.026358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd7286715ec3'
down_revision: Union[str, None] = 'ff12555fb78c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('book',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('author_id', sa.String(length=36), nullable=False),
                    sa.Column('publisher_id', sa.String(length=36), nullable=False),
                    sa.Column('title', sa.String(255), nullable=False),
                    sa.Column('publication_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
                    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=True)
    op.create_index(op.f('ix_book_author_id'), 'book', ['author_id'], unique=False)
    op.create_index(op.f('ix_book_publisher_id'), 'book', ['publisher_id'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_index(op.f('ix_book_publication_date'), 'book', ['publication_date'], unique=False)


def downgrade() -> None:
    # Check out index
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_index(op.f('ix_book_author_id'), table_name='book')
    op.drop_index(op.f('ix_book_publisher_id'), table_name='book')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_publication_date'), table_name='book')
    op.drop_table('book')
