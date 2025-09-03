
# 💵 Currency Converter API

A simple and fast currency converter application built with a FastAPI backend and a vanilla JavaScript frontend.

🚀 Check out the live demo: https://currency-conversor-7.onrender.com

<img width="1736" height="1204" alt="image" src="https://github.com/user-attachments/assets/08ffe65d-06cf-4c54-aafe-4b4c9ea1dd25" />



---

# 📝 About The Project

This project is a web-based currency converter. It features a backend API built with Python and FastAPI that fetches real-time exchange rates from an external service, and a clean user interface created with vanilla JavaScript, HTML, and CSS.

---

# ⭐ Key Features

Convert values between multiple currencies (USD, EUR, BRL, etc.).

Clean and simple user interface.

Utilizes real-time exchange rate data.

RESTful API backend powered by FastAPI.

---

# 🛠️ Tech Stack

*  **Backend:** Python, FastAPI 

*  **Frontend:** HTML, CSS and JavaScript

* **Deployment:** Render

---


# ⚙️ How to Run Locally

To get a local copy up and running, follow these simple steps.

---

# 🔑 Prerequisites

Python 3.8+

An API Key from ExchangeRate-API

---

# 📦 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/correagss/currency-conversor.git
cd currency-conversor
```

**2. Create and activate a virtual environment:**
```bash
(For Windows)
python -m venv venv
.\venv\Scripts\activate

(For macOS/Linux)
python3 -m venv venv
source venv/bin/activate
```


**3. Install the required packages:**
```bash
pip install -r requirements.txt

4. Set up your environment variables:
Create a file named .env in the root directory of the project and add your API key:

API_KEY=your_exchangerate_api_key_here
```

**5. Run the application:**
The application will be available at http://localhost:8000.

```bash
uvicorn api.main:app --reload
```
