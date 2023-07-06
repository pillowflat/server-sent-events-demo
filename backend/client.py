from dotenv import load_dotenv
load_dotenv()
import os
import sseclient

PORT = os.getenv('PORT')
messages = sseclient.SSEClient(f"http://localhost:{PORT}/listen")

for msg in messages:
    print(msg)