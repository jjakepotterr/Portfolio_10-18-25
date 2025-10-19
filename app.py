
from flask import Flask, render_template, request, Response
import os
import requests

app = Flask(__name__)

# ------------------------------------------------------
# OPTIONAL: Simple proxy to embed sites that block iframes
# WARNING: Many sites prohibit framing or proxying content.
# Use only for your own sites or with permission.
# To enable, set ENABLE_PROXY=True. Otherwise, iframes may
# be blocked by X-Frame-Options/CSP on some destinations.
# ------------------------------------------------------
ENABLE_PROXY = False  # Set to True only if you accept the risks.

@app.route('/proxy')
def proxy():
    if not ENABLE_PROXY:
        return Response("Proxy disabled. Set ENABLE_PROXY=True in app.py to enable.", status=403)
    url = request.args.get('url', '')
    if not url:
        return Response("Missing url parameter.", status=400)
    try:
        r = requests.get(url, timeout=10)
        # NOTE: This will not rewrite relative asset links, JS, or CSS.
        # It's a minimal example and many modern sites won't render well.
        content = r.text
        return Response(content, headers={"Content-Type": r.headers.get("Content-Type", "text/html; charset=utf-8")})
    except Exception as e:
        return Response(f"Proxy error: {e}", status=502)

@app.route('/')
def index():
    # You can change default URLs here or directly in the HTML comments.
    links = {
        "linkedin": "https://www.linkedin.com/",
        "projects": "https://example.com/",      # Replace with your portfolio/projects site
        "github":   "https://github.com/",
        "contact":  "https://example.com/contact" # Replace with your contact page or form
    }
    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(debug=True)
