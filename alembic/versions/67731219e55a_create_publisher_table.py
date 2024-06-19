"""Create publisher table

Revision ID: 67731219e55a
Revises: 29e2bec6e177
Create Date: 2024-06-15 09:20:11.349568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67731219e55a'
down_revision: Union[str, None] = '29e2bec6e177'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('publisher',
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('name', sa.String(255), nullable=False),
                    sa.Column('address', sa.String(255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_publisher_id'), 'publisher', ['id'], unique=True)
    op.create_index(op.f('ix_publisher_name'), 'publisher', ['name'], unique=True)
    op.create_index(op.f('ix_publisher_address'), 'publisher', ['address'], unique=False)


def downgrade() -> None:
    # Check out create_index
    op.drop_index(op.f('ix_publisher_id'), table_name='publisher')
    op.drop_index(op.f('ix_publisher_name'), table_name='publisher')
    op.drop_index(op.f('ix_publisher_address'), table_name='publisher')
    op.drop_table('publisher')
