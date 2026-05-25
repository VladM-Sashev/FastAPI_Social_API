"""create table votes

Revision ID: 6b02a552635b
Revises: 5af236de79c9
Create Date: 2026-05-21 14:35:22.353300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b02a552635b'
down_revision: Union[str, Sequence[str], None] = '5af236de79c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("votes", sa.Column("post_id", sa.Integer(), nullable=False),
                    sa.Column("user_id", sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
                    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("post_id", "user_id"))
    


def downgrade() -> None:
    op.drop_table("votes")
    
