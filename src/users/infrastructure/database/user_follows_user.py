from sqlalchemy import Table, Column, Text, ForeignKey


def define_table(metadata):
    user_follows_user_table = Table(
        "user_follows_user",
        metadata,
        Column("follower_id", Text(length=36), ForeignKey("user.id"), primary_key=True),
        Column("followed_id", Text(length=36), ForeignKey("user.id"), primary_key=True),
    )
    return user_follows_user_table
