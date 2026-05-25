"""create table users

Revision ID: 85074858bcfb
Revises: 1c62975e1834
Create Date: 2026-05-21 13:57:23.503123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85074858bcfb'
down_revision: Union[str, Sequence[str], None] = '1c62975e1834'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), primary_key=True),
                    sa.Column("email", sa.String(), nullable=False, unique=True),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))
    


def downgrade() -> None:
    op.drop_table("users")
    
