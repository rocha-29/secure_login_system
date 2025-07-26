# 🔐 Secure Login System

A secure and modern login system built with **Flask**, featuring:
- User registration and login
- Advanced password validation
- Persistent encrypted user storage using **Fernet**
- Custom login_required decorator
- User dashboard & profile
- Bootstrap 5 dark theme

## 🚀 Features

- 🔒 Password hashing with Werkzeug
- ✅ Client-side and server-side validation
- 📁 User data encrypted in `users.json`
- 🌐 Clean and responsive UI
- 🧪 Fully working demo with test users

## 📦 Tech Stack

- Python 3.x
- Flask
- Bootstrap 5
- Jinja2
- Werkzeug
- Cryptography (Fernet)

## 📂 Folder Structure

secure_login_system/
├── app.py
├── generate_key.py
├── secret.key
├── users.json
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ └── profile.html
└── requirements.txt


## 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/rocha-29/secure_login_system.git
cd secure_login_system

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate encryption key (one-time)
python generate_key.py

# 5. Run the app
python app.py
App will run at http://127.0.0.1:5000

🧪 Test Credentials
Username	Password
Prueba	Secure123!

🖼️ Demo Screenshot

📄 License
This project is licensed under the MIT License.


## 📸 Demo Screenshot

![Login Screenshot](https://raw.githubusercontent.com/rocha-29/secure_login_system/main/demo/login.png)


🌟 Author
Daniel Rocha — @rocha-29
