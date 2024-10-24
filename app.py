from flask import Flask, request, jsonify, render_template
from prometheus_client import Counter, Summary, Gauge, generate_latest
import psutil

app = Flask(__name__)

# Mock exchange rates (for simplicity)
EXCHANGE_RATES = {
    'USD_EUR': 0.85,
    'EUR_USD': 1.18,
    'USD_GBP': 0.75,
    'GBP_USD': 1.33
}

# Prometheus metrics
conversion_requests_total = Counter('conversion_requests_total', 'Total number of conversion requests', ['from_currency', 'to_currency'])
conversion_request_duration_seconds = Summary('conversion_request_duration_seconds', 'Duration of conversion requests in seconds')
request_counter = Counter('http_requests_total', 'Total HTTP requests')
memory_usage_gauge = Gauge('memory_usage_bytes', 'Memory usage of the Flask app')
cpu_usage_gauge = Gauge('cpu_usage_percent', 'CPU usage of the Flask app')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
@conversion_request_duration_seconds.time()
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    try:
        amount = float(request.args.get('amount'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid amount parameter'}), 400

    if not from_currency or not to_currency or amount <= 0:
        return jsonify({'error': 'Missing or invalid required parameters'}), 400

    key = f"{from_currency}_{to_currency}"
    if key not in EXCHANGE_RATES:
        return jsonify({'error': 'Unsupported currency conversion'}), 400

    # Perform conversion
    rate = EXCHANGE_RATES[key]
    converted_amount = amount * rate

    # Update Prometheus metrics
    conversion_requests_total.labels(from_currency, to_currency).inc()
    request_counter.inc()


    return jsonify({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount,
        'converted_amount': converted_amount,
        'rate': rate
    })

@app.route('/metrics', methods=['GET'])
def metrics():
    # Update system metrics
    memory_usage_gauge.set(psutil.virtual_memory().used)
    cpu_usage_gauge.set(psutil.cpu_percent(interval=1))
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
