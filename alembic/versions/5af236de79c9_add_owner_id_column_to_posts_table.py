"""add owner_id column to posts table

Revision ID: 5af236de79c9
Revises: 85074858bcfb
Create Date: 2026-05-21 14:22:24.594649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5af236de79c9'
down_revision: Union[str, Sequence[str], None] = '85074858bcfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", "posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
    
