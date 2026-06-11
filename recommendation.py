import sqlite3
import pandas as pd

def recommend_songs(mood, language=None, top_n=10):
    conn = sqlite3.connect("songs.db")

    if language:
        query = """
        SELECT track_name, artist_name, mood, language, popularity
        FROM songs
        WHERE mood = ?
        AND language = ?
        ORDER BY popularity DESC
        LIMIT ?
        """
        result = pd.read_sql(query, conn, params=(mood, language, top_n))

    else:
        query = """
        SELECT track_name, artist_name, mood, language, popularity
        FROM songs
        WHERE mood = ?
        ORDER BY popularity DESC
        LIMIT ?
        """
        result = pd.read_sql(query, conn, params=(mood, top_n))

    conn.close()
    return result


print(recommend_songs("Workout"))
print(recommend_songs("Happy", language="Hindi"))