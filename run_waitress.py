from __future__ import annotations
from waitress import serve
from engine_server import CONFIG, app

if __name__ == "__main__":
    serve(app, host=CONFIG.host, port=CONFIG.port, threads=4)
