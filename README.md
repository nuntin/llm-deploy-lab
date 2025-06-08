# 🧠 llm-deploy-lab (Internal Only)

> ✅ Deploy LLM (e.g. Falcon-RW-1B) via FastAPI + Streamlit + Docker  
> 🛠️ Used for internal experimentation — not intended for public use or production

## 🚧 Status
This project is considered **complete for internal purposes only**.  
The result is not production-quality and **should not be showcased**.

---

## 📦 Stack

- **FastAPI** – For serving LLM API at `/generate`
- **Streamlit** – Simple frontend UI for user interaction
- **Docker Compose** – To run LLM backend + UI in isolated containers
- **Transformers Pipeline** – Uses `pipeline("text-generation")` to serve HuggingFace models

---

## 🖼️ Architecture

```plaintext
[ Streamlit UI ]
        |
        v
[ FastAPI + Transformers pipeline ]
        |
        v
[ CPU-based LLM model (e.g. Falcon-RW-1B) ]

---

🧪 Example Prompt (Postman or CLI)

curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "สวัสดี"}'

Response:

{
  "result": "Hello .... (sample text)"
}

🧱 Folder Structure
.
├── app.py                 # FastAPI backend
├── web_ui.py             # Streamlit UI
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

⚠️ Limitation
❌ Very slow (running on CPU, large model load time)

❌ Output quality poor (Falcon-RW-1B is small, not tuned)

❌ Not optimized for inference

❌ Not suitable for demo/public exposure

✅ ✅ BUT: Was successfully deployed, works end-to-end

🪵 Internal Note
This project was used to practice real LLM deployment flow —
from building an API to UI, Dockerization, model loading, and prompt-response roundtrip.

It’s now archived and used as internal proof of work.