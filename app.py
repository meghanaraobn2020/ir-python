from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from python_scripts.key_phrase_extraction import KeyPhraseExtraction
from python_scripts.drmm import DRMM
from flask import request

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/docs")
def get_docs_with_ranks():
    doc_names = ['document_1', 'document_2', 'document_3']
    return jsonify(doc_names)


@app.route('/keyphrases', methods=['GET'])
def get_key_phrases():
    document_list = request.args.get('document_list')
    doc_key_phrase_list = KeyPhraseExtraction().generate_key_phrases(document_list)
    return jsonify(doc_key_phrase_list)


@app.route('/docranks', methods=['GET'])
def get_most_relevant_docs():
    query = request.args.get('query')
    document_list = DRMM().get_relevant_documents(query)
    return jsonify(document_list)


if __name__ == '__main__':
    app.run(debug=True)
