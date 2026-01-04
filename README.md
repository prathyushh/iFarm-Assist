# iFarmAssist 🌿
> **AI-Powered Agricultural Assistant for Kerala Farmers**

iFarmAssist is an intelligent mobile application designed to bridge the gap between farmers and agricultural experts. It uses **Context-Aware AI (RAG)** to provide instant, localized farming advice in simple language, solving the problem of delayed support from agricultural offices.

## 🚀 Key Features
*   **Context-Aware Advice:** Knows your location (Kerala) and crops (Coconut) to give specific answers.
*   **Multimodal Input:** Supports Text queries (Voice & Camera coming in Phase 5).
*   **Local Knowledge Base:** Trained on Kerala Agricultural University manuals (Coconut, Pest Mgmt, Biofertilizers).
*   **Privacy First:** All user data and API keys are secured.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Mobile App** | React Native (Expo), Axios |
| **Backend** | Python (FastAPI), Uvicorn |
| **AI Engine** | Google Gemini 2.0 Flash (LLM), LangChain (RAG) |
| **Database** | SQLite (Dev), ChromaDB (Vector Store) |
| **External APIs** | OpenWeatherMap |

---

## 📂 Project Structure
```
iFarmAssist/
├── mobile/           # React Native App (Frontend)
│   ├── src/          # Screens, Services, Components
│   ├── App.js        # Main Entry Point
│   └── .env          # API Config (Secret)
│
├── backend/          # FastAPI Server (Backend)
│   ├── routers/      # API Endpoints (Query, Auth)
│   ├── services/     # Logic (Gemini, Weather, VectorDB)
│   ├── data/         # PDF Manuals for AI Training
│   ├── main.py       # Server Entry Point
│   └── .env          # API Keys (Secret)
│
└── data/             # PDF Knowledge Sources
```

---

## ⚡ Setup Instructions

### 1. Prerequisites
*   Node.js & npm (for Mobile)
*   Python 3.10+ (for Backend)
*   Expo Go App (on your phone)

### 2. Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m backend.main
```
> Server runs at: `http://0.0.0.0:8000`

### 3. Mobile App Setup
```bash
cd mobile
npm install
npx expo start -c
```
> Scan the QR code with your phone (Expo Go).

---

## 🧠 AI Training (RAG)
To add new agricultural knowledge:
1.  Paste PDF into `data/` folder.
2.  Run the ingestion command:
    ```bash
    python backend/services/ingest.py
    ```

---

## 🛡️ Security Note
*   **API Keys**: Stored in `.env` (Excluded from Git).
*   **Database**: Local SQLite (Excluded from Git).
*   **Dependencies**: `node_modules` and `venv` are excluded.

---
**Status:** Phase 4 Complete (Mobile Foundation). Proceeding to Phase 5.
