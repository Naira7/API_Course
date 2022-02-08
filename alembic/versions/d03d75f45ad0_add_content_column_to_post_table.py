"""Add content column to post table

Revision ID: d03d75f45ad0
Revises: 7619a4d490d4
Create Date: 2022-02-04 10:42:35.057269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd03d75f45ad0'
down_revision = '7619a4d490d4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
