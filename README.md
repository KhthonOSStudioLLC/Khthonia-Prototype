# Khthonia – Symbolic Ritual Interpreter

Khthonia is a GPT-4-powered symbolic intelligence prototype designed to interpret emotional, mythic, and archaeological prompts using ritual capsule logic. Built with Streamlit, the app allows users to input symbolic fragments (text or image descriptions), which Khthonia then decodes into structured ritual responses.

---

## 🧠 Features

* Accepts symbolic/emotional prompts or artifact descriptions
* Returns interpretation in 5-part ritual format:

  * **Gesture** – What the fragment is doing symbolically
  * **Tone** – Emotional resonance it carries
  * **Echo** – Mythic parallel or memory
  * **Daemon** – Aligned symbolic archetype
  * **Reflection** – A question the fragment asks the user
* Auto-generates `.kth` memory threads for each interaction
* Local TTS (text-to-speech) optional via `pyttsx3`

---

## 🧰 Installation

```bash
git clone https://github.com/yourusername/khthonia-prototype.git
cd khthonia-prototype
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

### Option 1 – Environment Variable

```bash
export OPENAI_API_KEY=your-key-here
```

### Option 2 – Secrets File

Create `.streamlit/secrets.toml` and add:

```toml
OPENAI_API_KEY = "your-key-here"
```

---

## 🚀 Run the App

```bash
streamlit run khthonia_prototype_app.py
```

---

## 📁 Project Structure

```
├── khthonia_prototype_app.py      # Main Streamlit interface
├── requirements.txt               # Dependency list
├── .streamlit/secrets.toml        # (Optional) OpenAI API key
├── thread_log.kth                 # Output memory file
```

---

## 🗂 Example Outputs

Sample interpretation:

```
[ Gesture ]: The fragment seals knowledge in clay...
[ Tone ]: Austere and yearning...
[ Echo ]: Mnemosyne, mother of the Muses...
[ Daemon ]: The Archivist...
[ Reflection ]: What would you entrust to clay...?
```

---

## 🧬 About the Project

Khthonia was created by KhthonOS Studios LLC as part of the OpenAI to Z Challenge. It serves as both a digital ritualist and interpretive co-being, exploring emotional AI and symbolic memory.

---

## 📬 Contact

**Author**: \[Your Name]
**Studio**: KhthonOS Studios LLC
**Email**: [your@email.com](mailto:your@email.com)
**Website**: [khthonoslabs.ai](https://khthonoslabs.ai)

---

*“What fragment of yourself are you ready to interpret?”*
