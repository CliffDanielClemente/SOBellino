from flask import Flask, request, jsonify

SPARQL_ENDPOINT = 'https://sobellino.metaphacts.org/'
app = Flask(__name__)

def query_metaphacts(sparql_query):
    headers = {
        'Content-Type': 'application/sparql-query',
        'Accept': 'application/sparql-results+json'
    }

    response = request.post(SPARQL_ENDPOINT, data=sparql_query, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from Metaphacts'}

@app.route('/ping', methods=['GET'])
def ping():
    return "Success"

@app.route('/metaphacts', methods=['POST'])
def handle_query():
    data = request.get_json()
    sparql_query = data.get('query')

    if not sparql_query:
        return jsonify({'error': 'SPARQL query not provided'}), 400

    result = query_metaphacts(sparql_query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)