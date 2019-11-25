from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
from searchAPI import searchapi
import urllib.parse

class DetailHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin','*')
        BaseHTTPRequestHandler.end_headers(self)
    
    def response_json(self,msg, statuscode=200):
        message = json.dumps((msg),indent=2).encode("utf-8")
        self.protocol_version = "HTTP/1.1"
        self.send_response(statuscode)
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(message)
    

    def get_key(self):
        key=re.findall(r"key=([^\&]+)",self.path)
        return key
    
    def get_query(self):
        query=urllib.parse.unquote(str(re.findall(r"query=([^\&]+)", self.path)))
        return query
    
    def do_GET(self):
        
        if (self.path.startswith("/search?")):
            key = self.get_key()
            query = self.get_query()
            if not key:
                self.response_json({"error": "key is not found"},400)
                return
            if not query:
                self.response_json({"error": "query is not found"},400)
                return
            
            response= searchapi(key,query)
            self.response_json(response)
            return
        
        elif (self.path.startswith("/url?")):
            key = self.get_key()
            query = self.get_query()
            if not key:
                self.response_json({"error": "key is not found"},400)
                return
            if not query:
                self.response_json({"error": "query is not found"},400)
                return
            
            response= searchapi(key,query,"url")
            self.response_json(response)
            return 

        elif (self.path.startswith("/address?")):
            key = self.get_key()
            query = self.get_query()
            if not key:
                self.response_json({"error": "key is not found"},400)
                return
            if not query:
                self.response_json({"error": "query is not found"},400)
                return
            
            response= searchapi(key,query,"address")
            self.response_json(response)
            return   

        elif (self.path.startswith("/geometry?")):
            key = self.get_key()
            query = self.get_query()
            if not key:
                self.response_json({"error": "key is not found"},400)
                return
            if not query:
                self.response_json({"error": "query is not found"},400)
                return
            
            response= searchapi(key,query,"geometry")
            self.response_json(response)
            return  
        else:
            self.response_json({"error": "path not found"},404)

if __name__ == "__main__":
    server_addr=("",1234)
    httpd = HTTPServer(server_addr, DetailHandler)
    httpd.serve_forever()
