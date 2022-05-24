"""empty message

Revision ID: 9cbf6c3ae899
Revises: 05e749d4c781
Create Date: 2022-05-24 02:40:53.346506

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9cbf6c3ae899'
down_revision = '05e749d4c781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('gender', mysql.VARCHAR(length=80), nullable=False))
    # ### end Alembic commands ###
