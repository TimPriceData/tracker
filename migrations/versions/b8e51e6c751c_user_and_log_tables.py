"""User and Log tables

Revision ID: b8e51e6c751c
Revises: 
Create Date: 2020-01-02 10:55:16.361168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8e51e6c751c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_country'), 'user', ['country'], unique=False)
    op.create_index(op.f('ix_user_dob'), 'user', ['dob'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_start', sa.DateTime(), nullable=True),
    sa.Column('time_stop', sa.DateTime(), nullable=True),
    sa.Column('shallow', sa.Integer(), nullable=True),
    sa.Column('concentrated', sa.Integer(), nullable=True),
    sa.Column('deep', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_log_concentrated'), 'log', ['concentrated'], unique=False)
    op.create_index(op.f('ix_log_deep'), 'log', ['deep'], unique=False)
    op.create_index(op.f('ix_log_shallow'), 'log', ['shallow'], unique=False)
    op.create_index(op.f('ix_log_time_start'), 'log', ['time_start'], unique=False)
    op.create_index(op.f('ix_log_time_stop'), 'log', ['time_stop'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_log_time_stop'), table_name='log')
    op.drop_index(op.f('ix_log_time_start'), table_name='log')
    op.drop_index(op.f('ix_log_shallow'), table_name='log')
    op.drop_index(op.f('ix_log_deep'), table_name='log')
    op.drop_index(op.f('ix_log_concentrated'), table_name='log')
    op.drop_table('log')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_dob'), table_name='user')
    op.drop_index(op.f('ix_user_country'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
