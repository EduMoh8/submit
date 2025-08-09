import sounddevice as sd
import wavio
import speech_recognition as sr
import time
import google.generativeai as genai

# ---------------- SETTINGS ----------------
DURATION = 10  # seconds
SAMPLE_RATE = 16000
FILENAME = "recorded_malayalam.wav"
API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your Gemini API key

# ---------------- RECORD AUDIO ----------------
print("🎤 Get ready! Recording will start in...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print(f"🎙 Recording for {DURATION} seconds... Speak in Malayalam!")
recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')

for sec in range(DURATION):
    time.sleep(1)
    print(f"⏳ {sec+1} / {DURATION} seconds")

sd.wait()
wavio.write(FILENAME, recording, SAMPLE_RATE, sampwidth=2)
print("✅ Recording complete!")

# ---------------- SPEECH TO TEXT ----------------
recognizer = sr.Recognizer()
with sr.AudioFile(FILENAME) as source:
    print("⏳ Recognizing speech...")
    audio_data = recognizer.record(source)

try:
    malayalam_text = recognizer.recognize_google(audio_data, language="ml-IN")
    print("📝 Malayalam Transcription:", malayalam_text)
except sr.UnknownValueError:
    print("❌ Could not understand the audio")
    exit()
except sr.RequestError as e:
    print("❌ API request error:", e)
    exit()

# ---------------- GEMINI SARCASM DETECTION📝 Malayalam Transcription: എടാ എടാ നീ ഒരു പൊട്ടനാണ് നീ ഒരു മണ്ടനാണ് ----------------
genai.configure(api_key="AIzaSyA6uX4L9HJ_gJnW-9RI35_8IVmkeHtUvLM")

prompt = f"""
You are a sarcasm detection expert for Malayalam text.
Rate sarcasm on a scale of 0 to 100.
0 means absolutely no sarcasm.
100 means extreme sarcasm.

Sentence: «{malayalam_text}»
Respond with ONLY the sarcasm score as a number. No explanation.
"""

model = genai.GenerativeModel("gemini-2.5-pro")
response = model.generate_content(prompt)

sarcasm_score = response.text.strip()
print("🎯 Sarcasm Score:", sarcasm_score)






#kfjebvkjqlefvhr92piqr