import qrcode
import pyttsx3
import os

# Initialize the voice engine
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def generate_qr_code(link):
    """Function to generate QR code and save it as a .jpg file"""
    try:
        # Speak to the user
        speak("Processing the QR code for the given link.")
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill='black', back_color='white')

        # Save the image as a .jpg file
        img.save("qr_code.jpg", "JPEG")

        # Speak after QR code creation
        speak("QR code has been created and saved as qr_code.jpg")

    except Exception as e:
        # If an error occurs, speak the error message
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")

def main():
    """Main function to interact with the user and generate QR code"""
    try:
        # Prompt the user for input via voice
        speak("Paste the link you want to create QR code of.")
        
        # Get the link input from the user
        link = input("Enter the link to generate QR code: ")

        if link.strip() == "":
            raise ValueError("The link cannot be empty.")
        
        # Generate QR code
        generate_qr_code(link)

    except Exception as e:
        # Handle any exceptions that occur in the input or process
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
