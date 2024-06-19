"""Create library branch table

Revision ID: ff12555fb78c
Revises: 67731219e55a
Create Date: 2024-06-15 09:20:39.120259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff12555fb78c'
down_revision: Union[str, None] = '67731219e55a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('library_branch',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('name', sa.String(255), nullable=False),
                    sa.Column('address', sa.String(255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_library_branch_id'), 'library_branch', ['id'], unique=True)
    op.create_index(op.f('ix_library_branch_name'), 'library_branch', ['name'], unique=False)
    op.create_index(op.f('ix_library_branch_address'), 'library_branch', ['address'], unique=False)


def downgrade() -> None:
    # Check out index
    op.drop_index(op.f('ix_library_branch_id'), table_name='library_branch')
    op.drop_index(op.f('ix_library_branch_name'), table_name='library_branch')
    op.drop_index(op.f('ix_library_branch_address'), table_name='library_branch')
    op.drop_table('library_branch')
