
from flask import Flask, jsonify
from flask_cors import CORS
from ticket_generator_module import generate_full_strip

app = Flask(__name__)
CORS(app)

@app.route('/api/tickets')
def get_tickets():
    try:
        tickets = generate_full_strip()
        return jsonify(tickets)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

