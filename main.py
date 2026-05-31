import subprocess
import sys
import os
import time
import threading

def run_fastapi():
    os.chdir("app")
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "main:app", "--port", "8000"
    ])

def run_streamlit():
    time.sleep(2)  # FastAPI ko start hone do pehle
    os.chdir("..")
    subprocess.run([
        sys.executable, "-m", "streamlit", 
        "run", "streamlit_app.py"
    ])

if __name__ == "__main__":
    print("Starting CKD Prediction System...")
    print("FastAPI  → http://127.0.0.1:8000")
    print("Streamlit → http://localhost:8501")
    
    # FastAPI thread mein run karo
    api_thread = threading.Thread(target=run_fastapi, daemon=True)
    api_thread.start()
    
    # Streamlit main thread mein
    run_streamlit()