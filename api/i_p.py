from http.server import BaseHTTPRequestHandler

#from dat import ii, uu

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg="w-i-mod data"
    self.wfile.write(msg.encode())
    return


#ii()
