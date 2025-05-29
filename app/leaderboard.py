from app.db import db_cursor, conn
from app.models import LeaderboardEntry


def insert_score(username, score):
    sql = """
    INSERT INTO leaderboard (username, score)
    VALUES (%s, %s)
    """
    db_cursor.execute(sql, (username, score))
    conn.commit()


def get_top_scores(limit=10):
    sql = """
    SELECT * FROM leaderboard
    ORDER BY score DESC
    LIMIT %s
    """
    db_cursor.execute(sql, (limit,))
    return [LeaderboardEntry(row) for row in db_cursor.fetchall()]
