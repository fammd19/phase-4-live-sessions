"""Add location column to User model

Revision ID: 73c1ded0f288
Revises: dfb83b0aa264
Create Date: 2024-07-01 19:56:04.794473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73c1ded0f288'
down_revision = 'dfb83b0aa264'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('location')

    # ### end Alembic commands ###
