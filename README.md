# 🔗 Shortify — URL Shortener

> A simple, efficient, and secure URL shortening web application built with Python and Flask.

<p align="center">
  <strong>Turn long URLs into short, clean, and shareable links.</strong>
</p>

<p align="center">
  <a href="https://shortify-maazdev.vercel.app/">🌐 Live Demo</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/maazsiddiqui79/URL-Shortner-Python">📂 GitHub Repository</a>
</p>

---

## 📑 Table of Contents

* [📖 Overview](#-overview)
* [🎯 Objectives](#-objectives)
* [✨ Key Features](#-key-features)
* [🔗 URL Shortening](#-url-shortening)
* [🔐 Password Protection](#-password-protection)
* [🛡️ URL Validation](#️-url-validation)
* [↪️ Automatic Redirection](#️-automatic-redirection)
* [🗑️ Short Link Deletion](#️-short-link-deletion)
* [🧠 How It Works](#-how-it-works)
* [🏗️ Application Architecture](#️-application-architecture)
* [🗄️ Database Design](#️-database-design)
* [🖥️ Project Screenshots](#️-project-screenshots)
* [🛠️ Technology Stack](#️-technology-stack)
* [📂 Project Structure](#-project-structure)
* [⚙️ Installation & Setup](#️-installation--setup)
* [▶️ Running Locally](#️-running-locally)
* [☁️ Deployment](#️-deployment)
* [🚀 Future Improvements](#-future-improvements)
* [👨‍💻 Author](#-author)
* [📜 License](#-license)

---

## 📖 Overview

**Shortify** is a full-stack URL shortening web application developed with **Python and Flask**.

It allows users to convert long URLs into short, shareable links. Each generated short link is associated with the original URL and a user-provided password.

The application generates a unique short code, stores the URL information in a SQLite database, and provides a shortened link that can be used to redirect visitors to the original destination.

Shortify also includes a dedicated deletion interface where a shortened link can be removed by providing the link and its associated password.

The application is deployed and publicly accessible through **Vercel**.

---

## 🎯 Objectives

Shortify was developed with the following objectives:

* 🔗 Create short and shareable URLs
* ⚡ Generate short codes automatically
* 🛡️ Validate URLs before processing
* 🔐 Protect link deletion with a password
* 💾 Store shortened URLs using a database
* ↪️ Redirect users automatically to original URLs
* 🎨 Provide a clean and responsive interface
* ☁️ Deploy a Flask application using Vercel

---

## ✨ Key Features

### 🔗 URL Shortening

Shortify accepts a long URL and generates a compact short link.

The application generates an **8-character alphanumeric short code** using uppercase letters, lowercase letters, and numbers. The generated code is then stored together with the original URL.

Example:

```text
Original URL
https://example.com/a-very-long-page-name

              ↓

Shortify

              ↓

Short URL
https://shortify-maazdev.vercel.app/X7kP2mQa
```

---

### 🔐 Password Protection

When creating a shortened URL, the user provides a password.

The password is subsequently used to verify ownership when deleting the shortened URL.

This means a user does not need to create an account simply to manage a generated link.

---

### 🛡️ URL Validation

Shortify validates the submitted URL before creating a short link.

The application checks that the entered value begins with an accepted web URL prefix and limits the original URL to **500 characters**.

---

### ↪️ Automatic Redirection

Every generated short code is associated with an original URL.

When a visitor opens the short link:

```text
Short URL
    │
    ▼
Short Code
    │
    ▼
Database Lookup
    │
    ▼
Original URL
    │
    ▼
Redirect
```

If the short code exists, Flask redirects the visitor to the stored original URL.

If the short code does not exist, the application displays an error and returns the visitor to the home page.

---

### 🗑️ Short Link Deletion

Shortify includes a dedicated deletion page.

To delete a shortened URL, the user provides:

* The shortened URL
* The password associated with the URL

The application extracts the short code from the submitted URL and checks it against the provided password.

If a matching database record is found, the record is deleted.

If the details do not match, the application displays an error message.

---

## 🧠 How It Works

### Step 1 — Enter the URL

The user enters the long URL into the Shortify home page.

### Step 2 — Enter a Password

The user enters a password that will later be required to delete the generated link.

### Step 3 — Validate the Form

Flask-WTF validates the submitted form and checks the URL requirements.

### Step 4 — Generate a Short Code

Shortify generates an 8-character alphanumeric code.

### Step 5 — Store the URL

The application stores:

```text
Original URL
Short Code
Password
Creation Date
```

inside the SQLite database.

### Step 6 — Generate the Short Link

The application combines the current application URL with the generated short code.

### Step 7 — Redirect Visitors

When the short URL is opened, the application searches for the corresponding short code and redirects the visitor to the original URL.

### Step 8 — Delete the Link

If the user wants to remove the link, they can visit the deletion page and provide the shortened URL together with the correct password.

---

## 🏗️ Application Architecture

```text
                         ┌─────────────────┐
                         │      User       │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   Shortify UI   │
                         │   HTML / CSS    │
                         │   JavaScript    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      Flask      │
                         │   Application   │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       ┌─────────────┐    ┌──────────────┐    ┌──────────────┐
       │ Form        │    │ Short Code   │    │ URL Redirect │
       │ Validation  │    │ Generation    │    │ Logic        │
       └─────────────┘    └──────┬───────┘    └──────┬───────┘
                                  │                   │
                                  └─────────┬─────────┘
                                            ▼
                                  ┌─────────────────┐
                                  │ Flask-SQLAlchemy│
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │ SQLite Database │
                                  └─────────────────┘
```

---

## 🗄️ Database Design

Shortify currently uses one primary database model:

```text
┌──────────────────────────────────────┐
│           URL_DB_CLASS               │
├──────────────────────────────────────┤
│ id                                   │
│ original_url                         │
│ short_code                           │
│ created_at                           │
│ password                             │
└──────────────────────────────────────┘
```

### Relationship

```text
               URL_DB_CLASS
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
 Original URL   Short Code    Password
                     │
                     ▼
               Redirect URL
```

The model is implemented using Flask-SQLAlchemy.

---

## 🖥️ Project Screenshots

The following screenshots showcase the actual Shortify interface and its primary workflows.

### 🌙 Home Page — Dark Mode

<img src="./Project%20Screenshots/home%20page%20in%20dark%20mode.png" alt="Shortify Home Page in Dark Mode" width="85%">

---

### ☀️ Manage Page — Light Mode

<img src="./Project%20Screenshots/mange%20page%20in%20light%20mode.png" alt="Shortify Manage Page in Light Mode" width="85%">

---

### 🔗 Short Link Creation

<img src="./Project%20Screenshots/short%20link%20creation.png" alt="Shortify Short Link Creation" width="85%">

---

### 🗑️ Short Link Deletion

<img src="./Project%20Screenshots/short%20link%20deletion%20.png" alt="Shortify Short Link Deletion" width="85%">

---

## 🛠️ Technology Stack

| Category               | Technology              |
| ---------------------- | ----------------------- |
| **Language**           | Python                  |
| **Backend**            | Flask                   |
| **Database**           | SQLite                  |
| **ORM**                | Flask-SQLAlchemy        |
| **Forms & Validation** | Flask-WTF               |
| **Frontend**           | HTML5, CSS3, JavaScript |
| **Templating**         | Jinja2                  |
| **Deployment**         | Vercel                  |
| **Version Control**    | Git & GitHub            |

The current repository specifies Flask `2.3.3`, Flask-WTF `1.2.1`, Flask-SQLAlchemy `3.1.1`, and psycopg2-binary `2.9.9`.

---

## 📂 Project Structure

```text
URL-Shortner-Python/
│
├── Project Screenshots/
│   ├── home page in dark mode.png
│   ├── mange page in light mode.png
│   ├── short link creation.png
│   └── short link deletion .png
│
├── api/
│   │
│   ├── instance/
│   │
│   ├── static/
│   │   ├── logo.png
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── delete.html
│   │   ├── index.html
│   │   └── layout.html
│   │
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
├── vercel.json
├── LICENSE
├── Project Screenshots
└── README.md
```

The repository currently contains the `Project Screenshots`, `api`, `requirements.txt`, and `vercel.json` components shown above. The `api` directory contains the application's templates, static assets, initialization file, and main Flask application.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/maazsiddiqui79/URL-Shortner-Python.git
```

### 2. Navigate to the Project

```bash
cd URL-Shortner-Python
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Locally

The Flask application is located inside the `api` directory.

Run:

```bash
python api/main.py
```

The application starts using Flask's development server when `main.py` is executed directly.

Open the local address displayed by Flask in your browser.

---

## ☁️ Deployment

Shortify is deployed using **Vercel**.

The repository contains a `vercel.json` configuration that:

* Uses the Vercel Python runtime.
* Builds `api/main.py`.
* Routes incoming requests to `api/main.py`.

### Deployment Flow

```text
GitHub Repository
       │
       ▼
    Vercel
       │
       ▼
 @vercel/python
       │
       ▼
  api/main.py
       │
       ▼
 Flask Application
       │
       ▼
    Shortify
```

### 🌐 Live Application

The deployed application is available at:

**https://shortify-maazdev.vercel.app/**

The live interface currently presents the URL and password fields used to create shortened links.

---

## 🚀 Future Improvements

Possible future enhancements coming soon:

* 📊 URL click analytics
* 📈 Link performance statistics
* 👤 User accounts
* 🔗 Multiple links per user
* 🏷️ Custom aliases
* ⏳ URL expiration
* 📅 Scheduled link deletion
* 📋 One-click copy functionality
* 🔐 Secure password hashing
* 🛡️ Rate limiting
* 🚫 Malicious URL detection
* 🌍 Geographic analytics
* 📱 Further mobile optimization
* 🔌 REST API endpoints
* 🌐 Custom domains

---

## 👨‍💻 Author

### Maaz Siddiqui

**Python Developer | Computer Engineering | Full-Stack Development**

* **GitHub:** [@maazsiddiqui79](https://github.com/maazsiddiqui79)
* **Portfolio:** [themaaz.online](https://the-maaz-portfolio.vercel.app/)

Shortify was independently developed as a practical full-stack project to explore **Python, Flask, database integration, form validation, URL processing, application deployment, and web interface design**.

---

## 📜 License

No `LICENSE` file is currently present in the repository.

If you intend to distribute Shortify as an open-source project, adding an explicit license such as the **MIT License** would clearly define how others may use, modify, and distribute the project.

---

<div align="center">

## 🔗 Long URLs End Here.

**Shortify — URL Shortener**

Built with **Python + Flask**

**Designed & Engineered by Maaz Siddiqui**

</div>
