"""add likes

Revision ID: d47c2b9e193d
Revises: f53803e3d00c
Create Date: 2024-06-26 02:08:15.882995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd47c2b9e193d'
down_revision: Union[str, None] = 'f53803e3d00c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Likes",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("UserModel.id", ondelete="CASCADE")),
        sa.Column("post_id", sa.Integer, sa.ForeignKey("Posts.primary_key", ondelete="CASCADE")),
    )


def downgrade() -> None:
    pass
