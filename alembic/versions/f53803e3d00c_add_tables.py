"""add tables

Revision ID: f53803e3d00c
Revises: 
Create Date: 2024-06-26 02:05:57.521170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f53803e3d00c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "UserModel",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False, default=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    )    
    
    op.create_table(
        "Posts",
        sa.Column("primary_key", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("UserModel.id", ondelete="CASCADE"), nullable=False),
        sa.Column("content", sa.String, nullable=False),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("published", sa.Boolean, nullable=False, default=False),
        sa.Column("rating", sa.Integer),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    )

    op.create_table(
        "Likes",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("UserModel.id", ondelete="CASCADE")),
        sa.Column("post_id", sa.Integer, sa.ForeignKey("Posts.primary_key", ondelete="CASCADE")),
    )



def downgrade() -> None:
    pass
