"""create log_info table

Revision ID: 489535cd2cf6
Revises: 4ff0dfe03dc6
Create Date: 2015-06-04 04:54:22.746920

"""

# revision identifiers, used by Alembic.
revision = '489535cd2cf6'
down_revision = '4ff0dfe03dc6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'host_info',
        sa.Column('access_no'   , sa.Integer    , primary_key = True),
        sa.Column('send_number' , sa.Integer    , nullable = False),
        sa.Column('action_verb' , sa.String(1))
    )
    pass


def downgrade():
    op.drop_table('host_info')
    pass
