"""Loopback-only, stateless HTTP stub for checking JMeter method wiring.

This is not a CRM or a performance benchmark. Writes are echoed, not persisted.
"""

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path != '/posts':
            return self.respond(404, {'error': 'not_found'})
        self.respond(200, [{'id': 1, 'title': 'Synthetic title'}])

    def write_response(self, status, expected_path):
        if self.path != expected_path:
            return self.respond(404, {'error': 'not_found'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 65536:
                return self.respond(400, {'error': 'invalid_length'})
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                return self.respond(400, {'error': 'object_required'})
        except (ValueError, UnicodeDecodeError):
            return self.respond(400, {'error': 'invalid_json'})
        self.respond(status, {**body, 'id': 1})

    def do_POST(self):
        self.write_response(201, '/posts')

    def do_PUT(self):
        self.write_response(200, '/posts/1')

    def do_PATCH(self):
        self.write_response(200, '/posts/1')

    def do_DELETE(self):
        if self.path != '/posts/1':
            return self.respond(404, {'error': 'not_found'})
        self.respond(200, {})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    with ThreadingHTTPServer(('127.0.0.1', args.port), Handler) as server:
        print(f'Synthetic method stub: http://127.0.0.1:{args.port}; Ctrl+C to stop.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
