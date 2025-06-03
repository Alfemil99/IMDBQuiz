from app.db import db_cursor, conn
from app.models import LeaderboardEntry

def insert_score(username, score):
    # Insert a new score into the leaderboard table
    try:
        sql = """
        INSERT INTO leaderboard (username, score)
        VALUES (%s, %s)
        """
        db_cursor.execute(sql, (username, score))
        conn.commit() # Save the changes to the database
    except Exception as e:
        conn.rollback() # Undo the changes if an error occurs
        print("Error inserting score:", e)
        raise # Rethrow the exception

def get_top_scores(limit=10):
    # Get the top scores from the leaderboard, sorted by score descending
    sql = """
    SELECT * FROM leaderboard
    ORDER BY score DESC
    LIMIT %s
    """
    db_cursor.execute(sql, (limit,))

    # Convert each row into a LeaderboardEntry object and return the list
    return [LeaderboardEntry(row) for row in db_cursor.fetchall()]
