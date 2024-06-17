from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

def run_tkinter_script(script_name):
    try:
        script_path = os.path.join(os.path.dirname(__file__), script_name)
        subprocess.run(["python", script_path], check=True)
        return "Script started successfully."
    except subprocess.CalledProcessError as e:
        return f"Error running Tkinter script: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

@app.route("/")
def index():
    return render_template("a2.html")

@app.route("/open_account")
def open_account():
    result = run_tkinter_script("an.py")
    return result

@app.route("/login")
def login():
    result = run_tkinter_script("login.py")
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5001)
