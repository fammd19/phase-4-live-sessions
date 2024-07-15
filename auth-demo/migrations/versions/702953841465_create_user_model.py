"""Create User model

Revision ID: 702953841465
Revises: 
Create Date: 2024-07-15 10:39:34.098412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702953841465'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('isAdmin', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###