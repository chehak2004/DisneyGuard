from flask import Flask, jsonify
import disneyguard  # Import piracy detection module

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "DisneyGuard AI is running!"})

@app.route("/scan", methods=["GET"])
def scan():
    violations = disneyguard.scrape_piracy_websites()
    return jsonify({"violations": violations})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

