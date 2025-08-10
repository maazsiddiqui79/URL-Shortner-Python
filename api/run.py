# api/run.py
from url_short import app  # Import from your package

# Vercel looks for "app" here
if __name__ != "__main__":
    app = app  # Explicitly ensure the variable exists

# For local dev
if __name__ == "__main__":
    app.run(debug=True)
