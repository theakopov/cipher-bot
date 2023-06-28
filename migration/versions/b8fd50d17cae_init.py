"""Init

Revision ID: b8fd50d17cae

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8fd50d17cae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('user_id', sa.BigInteger(),
                  nullable=False, primary_key=True),
        sa.Column('first_name', sa.Text(), nullable=False),
        sa.Column('registration', sa.Date(), default=sa.func.now()),
    )


def downgrade():
    ...
