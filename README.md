# 🔐 Secure Login System

A secure and modern login system built with **Flask**, featuring:
- User registration and login
- Advanced password validation
- Persistent encrypted user storage using **Fernet**
- Custom `@login_required` decorator
- User dashboard and profile page
- Bootstrap 5 dark theme

---

## 🚀 Features

- 🔒 Password hashing with Werkzeug
- ✅ Client-side and server-side validation
- 🔐 Encrypted user data stored in `users.json`
- 🌐 Clean and responsive UI with Bootstrap 5
- 🧪 Fully functional demo with test user

---

## 📦 Tech Stack

- Python 3.x
- Flask
- Bootstrap 5
- Jinja2
- Werkzeug
- Cryptography (Fernet)

---

## 📁 Project Structure

secure_login_system/
├── app.py
├── generate_key.py
├── secret.key
├── users.json
├── requirements.txt
├── demo/
│ └── login.png
└── templates/
├── base.html
├── login.html
├── register.html
├── dashboard.html
└── profile.html


---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/rocha-29/secure_login_system.git
cd secure_login_system

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate encryption key (only once)
python generate_key.py

# 5. Run the Flask app
python app.py
App will be available at: http://127.0.0.1:5000

🧪 Test Credentials
Username	Password
Prueba	Secure123!

📸 Demo Screenshot

![Login Screenshot](https://raw.githubusercontent.com/rocha-29/secure_login_system/main/demo/login.png)

📄 License
This project is licensed under the MIT License.

🌟 Author
Daniel Rocha — @rocha-29