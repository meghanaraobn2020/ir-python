from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from python_scripts import RelevanceFeedback

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/docs")
def get_docs_with_ranks():
    doc_names = ['document_1', 'document_2', 'document_3']
    return jsonify(doc_names)


@app.route("/relevancefeedback")
def get_docs_with_ranks():
    doc_names = RelevanceFeedback()
    return jsonify(doc_names)


if __name__ == '__main__':
    app.run(debug=True)
