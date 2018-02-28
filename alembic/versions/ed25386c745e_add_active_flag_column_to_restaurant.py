"""Add active flag column to Restaurant

Revision ID: ed25386c745e
Revises: ab8bbf9118b7
Create Date: 2017-12-31 10:20:10.803785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed25386c745e'
down_revision = 'ab8bbf9118b7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('restaurant', sa.Column('active', sa.Boolean, server_default='t'))

def downgrade():
    op.drop_column('restaurant', 'active')
