"""add content column

Revision ID: 9f594d6cfb03
Revises: d47c2b9e193d
Create Date: 2024-06-26 02:09:18.524371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f594d6cfb03'
down_revision: Union[str, None] = 'd47c2b9e193d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("Posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("Posts", "content")
