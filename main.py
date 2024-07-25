# main.py
import mood_responses
import text_utils as tu

def main():
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))

    text = input("Enter a string to manipulate: ")
    print(f"Reversed: {tu.reverse_string(text)}")
    print(f"Capitalized: {tu.capitalize_string(text)}")

if __name__ == "__main__":
    main()
