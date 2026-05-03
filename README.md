# 🗳️ CivicTrack: The Interactive Election Guide

Welcome to **CivicTrack**, a modern, lightweight web application designed to gamify and simplify the democratic election process. 

Election information is often buried in dense, confusing PDFs. CivicTrack solves this by acting as a personalized civic concierge. It takes a user's specific scenario and generates a real-time, step-by-step interactive timeline (similar to a delivery tracker) so voters know exactly what to do and when to do it.

**Live Demo:** https://civictrack-app.onrender.com

---ven

## ✨ Core Features

*   **📍 The Voter Tracker (Interactive Timeline):** Users input their current civic status (e.g., "I just turned 18 and moved to a new state"). The Google Gemini API dynamically generates a chronological, step-by-step timeline from registration to polling day, rendered in an animated Vue.js UI.
*   **💡 Democracy Sandbox:** A dedicated edge-case solver. Users can ask complex electoral questions (e.g., "How do postal ballots work?") and the AI breaks it down into exactly three simple, digestible bullet points.
*   **🎨 Highly Accessible UI:** Built with a non-partisan "Deep Navy" glassmorphism aesthetic using Tailwind CSS, ensuring high contrast and clean typography for all demographics.

---

## 🛠️ Technology Stack

| Component | Technology Used |
| :--- | :--- |
| **Frontend** | HTML5, Vue.js 3 (CDN), Tailwind CSS (CDN) |
| **Backend** | Python, Flask |
| **AI Engine** | Google Gemini 2.5 Flash API |
| **Deployment** | Render, Gunicorn |

*Note: The entire frontend leverages CDNs to keep the repository size strictly under 1MB for maximum efficiency.*

---

## 🚀 Quick Setup (Local Development)

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd civictrack-app
   ```

2. **Set up your virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API Key:**
   Create a `.env` file in the root directory and add your Google Gemini key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   Navigate to `http://localhost:8080` to view the app!