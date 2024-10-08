"""update db

Revision ID: adc134ab7900
Revises: c7e8ad09c9c5
Create Date: 2024-08-15 22:53:23.932576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc134ab7900'
down_revision = 'c7e8ad09c9c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('price_sale', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('short_description', sa.String(), nullable=True),
    sa.Column('product_cat', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.BigInteger(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('deleted_by', sa.String(), nullable=True),
    sa.Column('deleted_at', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_db_product_created_at'), 'db_product', ['created_at'], unique=False)
    op.create_index(op.f('ix_db_product_deleted'), 'db_product', ['deleted'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_db_product_deleted'), table_name='db_product')
    op.drop_index(op.f('ix_db_product_created_at'), table_name='db_product')
    op.drop_table('db_product')
    # ### end Alembic commands ###
