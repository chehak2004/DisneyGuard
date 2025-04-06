from flask import Flask, render_template, jsonify, send_from_directory
import disneyguard

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["GET"])
def scan():
    violations = disneyguard.scrape_piracy_websites()
    return jsonify({"violations": violations})

@app.route("/testsite.html")
def serve_testsite():
    return send_from_directory(".", "testsite.html")

if __name__ == "__main__":
    app.run(debug=True)
