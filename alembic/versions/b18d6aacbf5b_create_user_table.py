"""Create user table

Revision ID: b18d6aacbf5b
Revises: d03d75f45ad0
Create Date: 2022-02-04 10:53:10.476645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18d6aacbf5b'
down_revision = 'd03d75f45ad0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
       sa.Column('id', sa.Integer(), nullable=False),
       sa.Column('email', sa.String(), nullable=False),
       sa.Column('password', sa.String(), nullable=False),
       sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
       sa.PrimaryKeyConstraint('id'),
       sa.UniqueConstraint('email')
       )
    pass
 

def downgrade():
    op.drop_table('users')
    pass
