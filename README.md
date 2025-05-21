# 🐍 Flask + PostgreSQL Web App

A minimal full-stack starter project using:

- 🧠 Python + Flask
- 🗃️ PostgreSQL (via SQLAlchemy)
- 🌐 HTML + CSS3
- 🔑 Environment Variables via `.env`

---

## 🚀 Features

- Modular Flask project layout
- PostgreSQL integration with SQLAlchemy
- Environment variable config using `python-dotenv`
- Pre-wired for team collaboration and expansion

---

## 🛠️ Setup Guide

### 1. Clone the Repo

```bash
git clone https://github.com/Alfemil99/IMDBQuiz/tree/main
cd <your-repo>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Update `.env` with your local PostgreSQL credentials.

### 4. Set Up the Database Locally

Log into psql and run:

```sql
CREATE DATABASE myappdb;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE myappdb TO myuser;
```

---

## 🧪 Run the App

```bash
python run.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to test.

---

## 👥 Team Workflow

### Working in Groups:

- Use **branches** for new features:
  ```bash
  git checkout -b feature/some-feature
  ```

- Submit **pull requests** to `main` after pushing
- Use `.env.example` to help teammates sync environments

---

## 📦 Tech Stack

| Layer     | Tool                |
|-----------|---------------------|
| Backend   | Flask (Python)      |
| Database  | PostgreSQL          |
| ORM       | SQLAlchemy          |
| Styling   | HTML + CSS3         |
| Config    | `dotenv` (`.env`)   |
| Versioning| Git + GitHub        |

---

## 📂 Project Structure

```bash
myapp/
├── app/
│   ├── templates/       # HTML files
│   ├── static/          # CSS/JS assets
│   ├── routes.py        # Flask routes
│   └── __init__.py      # App + DB setup
├── config.py            # Loads DB settings from .env
├── .env.example         # Env variable template
├── run.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ✅ Coming Soon (Optional Add-ons)

- User authentication
- Shared hosted PostgreSQL instance (e.g., Render)
- Flask-Migrate for DB versioning
