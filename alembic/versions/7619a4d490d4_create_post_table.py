"""Create Post Table

Revision ID: 7619a4d490d4
Revises: 
Create Date: 2022-02-04 10:12:21.129670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7619a4d490d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.Integer(), nullable=False))


def downgrade():
    op.drop_table('posts')
