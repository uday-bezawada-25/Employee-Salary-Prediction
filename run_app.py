import os
import threading
import time
from pyngrok import ngrok, conf

# Set your Ngrok authtoken
conf.get_default().auth_token = "30RYCyV5pgQXqWAkMoPeGu9PFBs_4g6WZubmJw5GjBpeyBZ67"  # Replace with your actual token

def run_streamlit():
    os.system("streamlit run app.py --server.port 8501")

# Start Streamlit in a separate thread
thread = threading.Thread(target=run_streamlit)
thread.start()

# Give Streamlit a few seconds to start
time.sleep(5)

# Start Ngrok tunnel
public_url = ngrok.connect(8501)
print("Your public URL is:", public_url)
