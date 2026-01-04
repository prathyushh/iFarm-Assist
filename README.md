# iFarmAssist 🌿🚜

**iFarmAssist** is an AI-powered agricultural assistant designed for farmers in Kerala. It provides instant, context-aware advice about crops, pests, and weather in simple language.

## 🚀 Features
*   **AI Chatbot**: Powered by Google Gemini + RAG (Retrieval-Augmented Generation).
*   **Knowledge Base**: Trained on Kerala Agricultural University manuals.
*   **Context Aware**: Knows your location (Kerala) and crops (e.g., Coconut) automatically.
*   **Mobile App**: Built with React Native (Expo).

## 📂 Project Structure
*   `backend/`: FastAPI server (Python).
*   `mobile/`: React Native app (Expo).
*   `data/`: Agricultural PDF manuals (The "Brain").

## 🛠️ Setup Instructions

### Prerequisites
*   Node.js & npm
*   Python 3.9+
*   Expo Go App (on your phone)

### 1. Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
**Important:** create a `.env` file in `backend/` with your API Key:
`GOOGLE_API_KEY=your_gemini_key_here`

### 2. Knowledge Base Setup
Place your PDF manuals in `data/` and run:
```bash
python backend/services/ingest.py
```

### 3. Run Server
```bash
python -m backend.main
```

### 4. Mobile App Setup
```bash
cd mobile
npm install
```
**Important:** create a `.env` file in `mobile/` with your Laptop's IP:
`EXPO_PUBLIC_API_URL=http://YOUR_LAPTOP_IP:8000`

### 5. Run App
```bash
npx expo start -c
```
Scan the QR code with your phone!

---
*Created for Final Year Project (2026)*
