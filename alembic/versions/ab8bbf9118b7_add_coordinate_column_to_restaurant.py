"""Add coordinate column to Restaurant

Revision ID: ab8bbf9118b7
Revises: 5785ee6a8724
Create Date: 2017-12-27 00:56:17.859411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab8bbf9118b7'
down_revision = '5785ee6a8724'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('restaurant', sa.Column('lat', sa.Integer))
    op.add_column('restaurant', sa.Column('lon', sa.Integer))

def downgrade():
    op.drop_column('Restaurant', 'lat')
    op.drop_column('Restaurant', 'lon')
