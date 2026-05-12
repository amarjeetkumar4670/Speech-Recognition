import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("READY TO SPEAK NOW")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You just said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio")

# Start program
#       ↓
# Open microphone
#       ↓
# Reduce background noise
#       ↓
# Ask user to speak
#       ↓
# Record voice
#       ↓
# Send audio to Google
#       ↓
# Convert speech to text
#       ↓
# Print recognized text
#       ↓
# If recognition fails → show error message