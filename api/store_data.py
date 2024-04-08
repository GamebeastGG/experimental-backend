from http.server import BaseHTTPRequestHandler
from supabase import create_client
import json
import os

# Supabase project details from environment variables
URL = os.getenv('SUPABASE_URL')
KEY = os.getenv('SUPABASE_KEY')

supabase = create_client(URL, KEY)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        # Insert the data into your Supabase table
        response = supabase.table("experiments").insert(data).execute()

        if response.error:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(response.error)}).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "data": response.data}).encode())
