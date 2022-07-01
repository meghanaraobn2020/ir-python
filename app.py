from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from python_scripts.key_phrase_extraction import KeyPhraseExtraction
from python_scripts.drmm import DRMM
from python_scripts.relevance_feedback import RelevanceFeedback
from flask import request

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/keyphrases', methods=['GET'])
def get_key_phrases():
    document_list = request.args.get('document_list')
    doc_key_phrase_list = KeyPhraseExtraction().generate_key_phrases(document_list)
    return jsonify(doc_key_phrase_list)


@app.route('/reldocs', methods=['GET'])
def get_relevant_docs():
    query = request.args.get('query')
    relevant_document_list = DRMM().get_relevant_documents(query)
    return jsonify(relevant_document_list)


@app.route('/userreldocs', methods=['GET'])
def get_user_relevant_docs():
    user_relevant_document_list = request.args.get('docslist')
    user_relevant_document_list = user_relevant_document_list.split(",")
    docs_key_phrases_list = RelevanceFeedback().get_user_relevant_document_list(user_relevant_document_list)
    return jsonify(docs_key_phrases_list)


if __name__ == '__main__':
    app.run(debug=True)
