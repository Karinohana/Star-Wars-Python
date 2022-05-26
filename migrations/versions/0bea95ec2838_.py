"""empty message

Revision ID: 0bea95ec2838
Revises: 1d7d6bdaac2b
Create Date: 2022-05-26 16:36:08.037804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bea95ec2838'
down_revision = '1d7d6bdaac2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('image1', sa.String(length=200), nullable=False))
    op.add_column('planets', sa.Column('image2', sa.String(length=200), nullable=False))
    op.add_column('planets', sa.Column('brief', sa.String(length=200), nullable=False))
    op.add_column('planets', sa.Column('description', sa.String(length=400), nullable=False))
    op.add_column('planets', sa.Column('tbd', sa.String(length=200), nullable=True))
    op.add_column('planets', sa.Column('tbd2', sa.String(length=200), nullable=True))
    op.drop_index('name', table_name='planets')
    op.drop_index('name_2', table_name='planets')
    op.drop_column('planets', 'climate')
    op.drop_column('planets', 'terrain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('terrain', mysql.VARCHAR(length=80), nullable=False))
    op.add_column('planets', sa.Column('climate', mysql.VARCHAR(length=80), nullable=False))
    op.create_index('name_2', 'planets', ['name'], unique=False)
    op.create_index('name', 'planets', ['name'], unique=False)
    op.drop_column('planets', 'tbd2')
    op.drop_column('planets', 'tbd')
    op.drop_column('planets', 'description')
    op.drop_column('planets', 'brief')
    op.drop_column('planets', 'image2')
    op.drop_column('planets', 'image1')
    # ### end Alembic commands ###
