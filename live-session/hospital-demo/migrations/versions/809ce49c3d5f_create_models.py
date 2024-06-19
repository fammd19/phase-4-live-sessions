"""Create models

Revision ID: 809ce49c3d5f
Revises: 
Create Date: 2024-06-20 06:11:44.080744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '809ce49c3d5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('specialism', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('complaint', sa.String(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    op.drop_table('patients')
    op.drop_table('doctors')
    # ### end Alembic commands ###