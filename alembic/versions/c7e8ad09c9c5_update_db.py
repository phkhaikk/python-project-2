"""update db

Revision ID: c7e8ad09c9c5
Revises: e3a6b7c33ded
Create Date: 2024-08-15 17:06:47.011505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e8ad09c9c5'
down_revision = 'e3a6b7c33ded'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_product_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.BigInteger(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_at', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_db_product_category_created_at'), 'db_product_category', ['created_at'], unique=False)
    op.create_index(op.f('ix_db_product_category_deleted'), 'db_product_category', ['deleted'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_db_product_category_deleted'), table_name='db_product_category')
    op.drop_index(op.f('ix_db_product_category_created_at'), table_name='db_product_category')
    op.drop_table('db_product_category')
    # ### end Alembic commands ###
