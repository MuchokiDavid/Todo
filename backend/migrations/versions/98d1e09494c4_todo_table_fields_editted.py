"""todo table fields editted

Revision ID: 98d1e09494c4
Revises: d9b94b3d0367
Create Date: 2024-02-28 23:00:13.144610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98d1e09494c4'
down_revision = 'd9b94b3d0367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('description', sa.String(length=100), nullable=True))
    op.drop_column('todos', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('text', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('todos', 'description')
    # ### end Alembic commands ###
