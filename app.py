from flask import Flask, render_template, request, redirect, url_for
import os, csv

app = Flask(__name__)

# ======== YOU CAN EDIT THESE ========
BRAND = "PIP-PORTFOLIO"  

# External profile links (used by the “Open …” button on the snapshot tabs)
PROFILE_LINKEDIN = "https://www.linkedin.com/in/YOUR_USERNAME/"
PROFILE_GITHUB   = "https://github.com/YOUR_USERNAME"

# Snapshot images shown on the LinkedIn/GitHub tabs (replace these files)
# Put your screenshots in static/img and point here:
SNAPSHOT_LINKEDIN = "img/linkedin_snapshot.png"  # <-- replace the image file
SNAPSHOT_GITHUB   = "img/github_snapshot.png"    # <-- replace the image file

# STATS/SKILLS list. Rename labels to your skills and point each to a pose image.
# value is 0–10. image must be under static/img.
SPECIAL = [
    {"key":"python",      "label":"Python",       "value":9, "image":"img/vaultboy_start.png"},  # <-- change image per skill
    {"key":"javascript",  "label":"JavaScript",   "value":8, "image":"img/vaultboy.avif"},
    {"key":"sql",         "label":"SQL",          "value":7, "image":"img/vaultboy.avif"},
    {"key":"flask",       "label":"Flask",        "value":8, "image":"img/vaultboy.avif"},
    {"key":"react",       "label":"React",        "value":7, "image":"img/vaultboy.avif"},
    {"key":"aws",         "label":"AWS",          "value":6, "image":"img/vaultboy.avif"},
    {"key":"ml",          "label":"ML",           "value":6, "image":"img/vaultboy.avif"},
]
# NOTE: The first item’s image is what shows at startup. Replace with your preferred default.

# ====================================

@app.route("/")
def index():
    links = {
        "linkedin": "/linkedin",  # internal snapshot page (fast; no CSP issues)
        "projects": "/projects",
        "github":   "/github",    # internal snapshot page
        "contact":  "/contact",
    }
    return render_template("index.html", brand=BRAND, links=links, special=SPECIAL)

# --- Snapshot tabs (image + “Open …” button) ---
@app.route("/linkedin")
def linkedin():
    return render_template("snapshot.html",
                           title="LinkedIn",
                           snapshot=SNAPSHOT_LINKEDIN,
                           url=PROFILE_LINKEDIN)

@app.route("/github")
def github():
    return render_template("snapshot.html",
                           title="GitHub",
                           snapshot=SNAPSHOT_GITHUB,
                           url=PROFILE_GITHUB)

# --- Projects (placeholder if you kept v2 gallery separate) ---
@app.route("/projects")
def projects():
    return render_template("projects.html")

# --- Contact ---
CONTACT_SAVE_TO = os.path.join(os.path.dirname(__file__), "data", "messages.csv")
os.makedirs(os.path.dirname(CONTACT_SAVE_TO), exist_ok=True)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/submit", methods=["POST"])
def contact_submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    wrote_header = not os.path.exists(CONTACT_SAVE_TO)
    with open(CONTACT_SAVE_TO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if wrote_header:
            w.writerow(["name", "email", "message"])
        w.writerow([name, email, message])

    return redirect(url_for("contact") + "?ok=1")

if __name__ == "__main__":
    app.run(debug=True)
