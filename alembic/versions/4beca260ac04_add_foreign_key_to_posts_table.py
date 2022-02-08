"""Add foreign key to posts table

Revision ID: 4beca260ac04
Revises: b18d6aacbf5b
Create Date: 2022-02-04 11:02:36.190144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4beca260ac04'
down_revision = 'b18d6aacbf5b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
         local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id')
    pass
