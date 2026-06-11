def detect_mood(user_text):
    text = user_text.lower()

    if any(word in text for word in ["gym", "workout", "run", "energy", "motivation"]):
        return "Workout"

    elif any(word in text for word in ["sad", "cry", "heartbroken", "breakup", "low"]):
        return "Sad"

    elif any(word in text for word in ["study", "focus", "exam", "assignment", "work"]):
        return "Study"

    elif any(word in text for word in ["happy", "excited", "party", "celebrate"]):
        return "Happy"

    else:
        return "Chill"

        print(detect_mood("I need gym motivation"))
print(detect_mood("I am feeling sad"))
print(detect_mood("I have an exam tomorrow"))
print(detect_mood("I am lowkey tired"))