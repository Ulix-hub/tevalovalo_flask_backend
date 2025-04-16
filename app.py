
from flask import Flask, jsonify
from ticket_generator_module import generate_full_strip

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Tevalovalo Backend Running ✅</h2><p>Use /generate to get tickets</p>"

@app.route("/generate")
def generate():
    tickets = generate_full_strip()
    return jsonify(tickets)

if __name__ == "__main__":
    app.run(debug=True)
