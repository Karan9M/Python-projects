import pywhatkit as kit
import pyttsx3
import time
import re
from datetime import datetime, timedelta

# Function to provide voice feedback
def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Function to validate phone number
def validate_phone_number(phone_number):
    pattern = r'^\+?[1-9]\d{1,14}$'  # E.164 phone number format
    if re.match(pattern, phone_number):
        return True
    return False

# Function to schedule the WhatsApp message
def schedule_whatsapp_message():
    try:
        # Ask for user inputs
        speak("Enter the time between 1 minute to 30 minutes to send the message after current time.")
        time_input = int(input("Enter time between 1m to 30m to send message after current time: "))
        if not (1 <= time_input <= 30):
            raise ValueError("Time must be between 1 and 30 minutes.")

        # Calculate the target time
        send_time = datetime.now() + timedelta(minutes=time_input)
        hour = send_time.hour
        minute = send_time.minute

        speak("Enter the recipient's phone number with country code.")
        phone_number = input("Enter recipient's phone number with country code: ")
        if not validate_phone_number(phone_number):
            raise ValueError("Invalid phone number format. Please enter a valid phone number with country code.")

        speak("Enter the message you want to send.")
        message = input("Enter message: ")

        # Provide voice feedback
        speak(f"Scheduling the message to {phone_number} at {hour}:{minute}.")

        # Schedule the WhatsApp message
        speak("Sending the message now.")
        kit.sendwhatmsg(phone_number, message, hour, minute)

        # Inform the user that the message is sent
        speak("Message sent successfully.")
        
    except ValueError as e:
        speak(f"Error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        speak(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

# Main function to run the program
if __name__ == "__main__":
    schedule_whatsapp_message()

