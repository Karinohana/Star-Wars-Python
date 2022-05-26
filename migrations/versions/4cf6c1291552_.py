"""empty message

Revision ID: 4cf6c1291552
Revises: 9e8b4f3433a0
Create Date: 2022-05-26 01:46:48.220804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4cf6c1291552'
down_revision = '9e8b4f3433a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('image1', sa.String(length=200), nullable=False))
    op.add_column('people', sa.Column('image2', sa.String(length=200), nullable=False))
    op.add_column('people', sa.Column('brief', sa.String(length=200), nullable=False))
    op.add_column('people', sa.Column('description', sa.String(length=200), nullable=False))
    op.add_column('people', sa.Column('tbd', sa.String(length=200), nullable=True))
    op.add_column('people', sa.Column('tbd2', sa.String(length=200), nullable=True))
    op.drop_index('name', table_name='people')
    op.drop_index('name_2', table_name='people')
    op.drop_column('people', 'hair_color')
    op.drop_column('people', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('gender', mysql.VARCHAR(length=200), nullable=False))
    op.add_column('people', sa.Column('hair_color', mysql.VARCHAR(length=80), nullable=False))
    op.create_index('name_2', 'people', ['name'], unique=False)
    op.create_index('name', 'people', ['name'], unique=False)
    op.drop_column('people', 'tbd2')
    op.drop_column('people', 'tbd')
    op.drop_column('people', 'description')
    op.drop_column('people', 'brief')
    op.drop_column('people', 'image2')
    op.drop_column('people', 'image1')
    # ### end Alembic commands ###