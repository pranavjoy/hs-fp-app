from flask import Flask, render_template, jsonify, abort, request
import backend
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')

@app.route("/pranav")
def pranav():
    return backend.main()

@app.route('/process_user_query', methods=["POST"])
def process_user_query():
    json = request.get_json()
    if not json or json.get('query') is None:
        abort(400)

    query = str(json['query']).strip()
    return jsonify(backend.process_user_query(query))


if __name__ == "__main__":
    app.run()
