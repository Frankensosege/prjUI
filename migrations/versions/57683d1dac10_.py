"""empty message

Revision ID: 57683d1dac10
Revises: 20c8f3523bb8
Create Date: 2023-03-15 17:39:13.825450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57683d1dac10'
down_revision = '20c8f3523bb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('user_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('passwd', sa.VARCHAR(length=100), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('lastupdate_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###