"""added admin

Revision ID: 8061fe242c2a
Revises: 66cdf574de7c
Create Date: 2021-05-09 22:24:42.887927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8061fe242c2a'
down_revision = '66cdf574de7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
