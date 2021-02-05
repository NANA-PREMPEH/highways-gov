"""empty message

Revision ID: d8ee7fe79e02
Revises: 
Create Date: 2021-02-04 10:04:30.511348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8ee7fe79e02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roadcondition2_k19',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reg', sa.String(length=50), nullable=True),
    sa.Column('road_no', sa.String(length=50), nullable=True),
    sa.Column('road_name', sa.String(length=50), nullable=True),
    sa.Column('link_ref', sa.String(length=50), nullable=True),
    sa.Column('sect_ref', sa.String(length=50), nullable=True),
    sa.Column('fr_om', sa.String(length=50), nullable=True),
    sa.Column('t_o', sa.String(length=50), nullable=True),
    sa.Column('start', sa.String(length=50), nullable=True),
    sa.Column('end', sa.String(length=50), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('width', sa.String(length=50), nullable=True),
    sa.Column('surf_type', sa.String(length=50), nullable=True),
    sa.Column('cond_score', sa.String(length=50), nullable=True),
    sa.Column('iri', sa.String(length=50), nullable=True),
    sa.Column('cond', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('regravelling', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('regravelling', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_table('roadcondition2_k19')
    # ### end Alembic commands ###
