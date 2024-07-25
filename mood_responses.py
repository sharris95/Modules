# mood_responses.py
def mood_response(mood):
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. Hope things get better soon.",
        "excited": "Awesome! What's got you so excited?",
        "angry": "Take a deep breath. It's going to be okay.",
    }
    return responses.get(mood.lower(), "I hope you have a good day!")
