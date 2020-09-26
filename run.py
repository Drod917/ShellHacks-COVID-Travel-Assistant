#If you see this, then I did something right.
from flask import Flask, request, jsonify, render_template
from google.cloud import bigquery
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/bq', methods=['GET'])
def query():
    client = bigquery.Client()

    # Perform a query.
    QUERY = (
        'SELECT * FROM `bigquery-public-data.covid19_public_forecasts.county_14d` '
        'WHERE state_name = "New York" '
        'AND prediction_date > forecast_date '
        'ORDER BY prediction_date '
        'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    clean = []
    # Iterate through result
    for row in rows:
        clean.append(row)
    res = []
    for row in clean:
        res.append(dict(row))
    return jsonify(res)
    
# POST example template
# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     new_records = []
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#     for r in records:
#         if r['name'] == record['name']:
#             r['email'] = record['email']
#         new_records.append(r)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(new_records, indent=2))
#     return jsonify(record)


if __name__ == "__main__":
    app.run(debug=True)
