import sqlite3
import pandas as pd

from chatbo import detect_mood

DB_NAME = "songs.db"

def ask_song_bot(question):
    mood = detect_mood(question)

    allowed_moods = ["Sad", "Happy", "Study", "Workout", "Chill"]

    if mood not in allowed_moods:
        mood = "Chill"

    query = f"""
    SELECT track_name, artist_name, mood, popularity
    FROM songs
    WHERE mood = '{mood}'
    ORDER BY popularity DESC
    LIMIT 5
    """

    conn = sqlite3.connect(DB_NAME)
    result = pd.read_sql_query(query, conn)
    conn.close()

    return result