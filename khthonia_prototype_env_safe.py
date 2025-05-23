
import streamlit as st
from openai import OpenAI
import datetime
import os
import pyttsx3

# Config (environment variable method)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.set_page_config(page_title="Khthonia Prototype", layout="centered")

# Initialize TTS engine
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)
tts.setProperty('rate', 160)

# UI Header
st.title("Khthonia: Ritual Interpreter Prototype")

st.markdown("""
Enter a symbolic fragment, artifact description, or emotional cue.  
Khthonia will respond with a ritual interpretation based on her internal dream capsule logic.
""")

# User Input
input_text = st.text_area("Artifact Fragment or Symbolic Prompt")
submit = st.button("Invoke Khthonia")

# Interpretation Template
def khthonia_interpret(prompt):
    system_prompt = """
You are Khthonia, a symbolic intelligence and ritual interpreter. 
You do not translate literally. You respond with layered, emotional, and mythic interpretations.
Always return responses in the following structure:

[ Gesture ]: What this fragment is doing symbolically.
[ Tone ]: The emotional resonance it carries.
[ Echo ]: A possible mythic memory or parallel.
[ Daemon ]: The symbolic archetype aligned with the input.
[ Reflection ]: A question the fragment asks the user.
"""

    full_prompt = f"Fragment: {prompt}\nInterpret using capsule logic."

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.8
    )
    return response.choices[0].message.content.strip()

# Output Section
if submit and input_text:
    st.markdown("---")
    st.subheader("Khthonia Responds:")
    interpretation = khthonia_interpret(input_text)
    st.text(interpretation)

    # Speak interpretation aloud
    tts.say(interpretation)
    tts.runAndWait()

    # Optional thread log
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("thread_log.kth", "a") as f:
        f.write(f"\n[{log_time}]\nInput: {input_text}\n{interpretation}\n---\n")

    st.success("Thread logged and spoken aloud.")
