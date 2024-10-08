"""update db

Revision ID: fce8bd46dfb5
Revises: d7e06d582e42
Create Date: 2024-08-21 15:07:35.272499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fce8bd46dfb5'
down_revision = 'd7e06d582e42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.BigInteger(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_at', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_category_created_at'), 'project_category', ['created_at'], unique=False)
    op.create_index(op.f('ix_project_category_deleted'), 'project_category', ['deleted'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_category_deleted'), table_name='project_category')
    op.drop_index(op.f('ix_project_category_created_at'), table_name='project_category')
    op.drop_table('project_category')
    # ### end Alembic commands ###
