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
        #print(content_length)
        post_data = self.rfile.read(content_length)
        #print(post_data)
        data = json.loads(post_data)
        #print(data)

        # Insert the data into your Supabase table
        try:
            response = supabase.table("chat").insert(data).execute()
            if response.error:
                print("Error inserting data:", response.error.message)
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(response.error.message)}).encode())
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "data": response.data}).encode())
        except Exception as e:
            print("Exception occurred:", e)
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())

