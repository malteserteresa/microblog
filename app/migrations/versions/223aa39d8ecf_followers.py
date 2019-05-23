"""followers

Revision ID: 223aa39d8ecf
Revises: 09c43fe01185
Create Date: 2019-05-23 10:04:41.555373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '223aa39d8ecf'
down_revision = '09c43fe01185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
