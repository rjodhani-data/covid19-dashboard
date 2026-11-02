"""Start the COVID-19 dashboard.

Run from the project folder:
    pip install -r requirements.txt
    python main.py
Then open http://127.0.0.1:8050 in your browser.
"""
from app import app

if __name__ == "__main__":
    app.run(debug=True)
