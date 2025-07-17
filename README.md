
# 🔗 URL Shortener

A simple and secure URL Shortener web application built using **Flask (Python)**, deployed on **Vercel**, with data stored in a **PostgreSQL** database hosted on **Render**.

---

## 🌐 Live Demo

👉 [Visit the URL Shortener Website]()

---

## 🚀 Features

- 🔐 Password-protected short URLs  
- ✂️ Generate unique short codes  
- 🔁 Instant redirection using the short URL  
- 🗑️ Delete shortened URLs securely using password verification  
- 📅 Timestamped URL creation  
- ⚙️ Backend validation for URLs and passwords  

---

## 🛠️ Tech Stack

| Layer         | Technology             |
|---------------|------------------------|
| Backend       | Flask (Python)         |
| Forms & Validation | Flask-WTF, WTForms  |
| Database      | PostgreSQL (Render)    |
| ORM           | SQLAlchemy             |
| Hosting       | Vercel                 |
| Deployment (DB) | Render               |
| Templating    | Jinja2 (HTML)          |
| Styling       | CSS                    |

---

## 🧱 Project Structure

```

url-shortener/
│
├── templates/
│   ├── index.html
│   └── delete.html
│
├── static/
│   └── (optional CSS/JS files)
│
├── app.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. **Run the application**

   ```bash
   flask run
   ```

6. **Visit**:
   `http://127.0.0.1:5000`

---

## 📦 Deployment

### 🌍 Vercel (Frontend)

* Flask app deployed using Vercel.
* You can use the Vercel Python template or custom configuration.

### 🗄️ Render (Database)

* PostgreSQL database is hosted on [Render.com](https://render.com).
* Connection string format:

  ```
  postgresql+psycopg2://username:password@host:port/database_name
  ```

---

## 📑 Sample Usage

### 🔧 Shorten a URL

* Input your long URL and password.
* Click "Shorten URL".
* Copy and use the returned short link.

### 🗑️ Delete a URL

* Input the short URL and password.
* Click "Delete".
* If credentials match, the URL is removed.

---

## 📬 Contact Me

* 📝 **To-Do App**: [Visit My To-Do App](https://go-todo-task.vercel.app/)
* 💼 **LinkedIn**: [linkedin.com/in/siddiqui-maazzz](https://www.linkedin.com/in/siddiqui-maazzz/)
* 🛠️ **GitHub**: [github.com/your-username](https://github.com/maazsiddiqui79)

---

### ✍️ Author

**Maaz Siddiqui**
_Diploma in Computer Engineering | Passionate about Web Development and AI_ | 

---
