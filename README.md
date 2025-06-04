# IMDB Quiz

- Python + Flask
- PostgreSQL (via SQLAlchemy)
- HTML + CSS3
- Environment Variables via `.env`

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

\c myappdb

CREATE TABLE leaderboard (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    score INTEGER NOT NULL,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

GRANT USAGE ON SCHEMA public TO myuser;
GRANT CREATE ON SCHEMA public TO myuser;

GRANT SELECT, INSERT, UPDATE, DELETE ON leaderboard TO myuser;
GRANT USAGE, SELECT ON SEQUENCE leaderboard_id_seq TO myuser;

```

---

## 5. Import the csv databse

Run import_csv.py

```bash
python import_csv.py
```
---

## 6. Run the code

Run the code

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

## How to play:
* You start the game at the main menu where you can see the leaderboard.
* You then choose your player name for the next playthrough. When you have chosen your name and pressed start, the first hint appears.
* You start by getting one hint and four possible movies to guess. The hints start by being hard, but get progressively easier by pressing the hint button more. But be careful of getting too many hints. For each hint the amount of points you get by answering correctly is reduced. So if you want a high score you have to take some risks.
* If you answer correctly the game will show you that you guessed correctly, if not the you will see what the right movie was and be sent to the main menu again.
* If you guessed correctly a new movie has to be guessed.
* When you fail your score and name will be added to the leaderboard from highest to lowest.
