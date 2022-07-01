import pandas as pd

from python_scripts.key_phrase_extraction import KeyPhraseExtraction
from python_scripts.text_summarization import TextSummarization
from python_scripts.drmm import DRMM


class RelevanceFeedback:

    def __init__(self):
        print("Relevance Feedback")

    @staticmethod
    def get_user_relevant_document_list(user_relevant_document_list):
        docs_key_phrases_list = KeyPhraseExtraction().get_key_phrases_for_every_doc(user_relevant_document_list)
        print(len(docs_key_phrases_list))
        document_summaries_list, document_keywords_list = TextSummarization().get_text_summaries_for_every_doc(user_relevant_document_list)
        print(len(document_summaries_list))
        print(len(document_keywords_list))
        # call Rocchio

        # call DRMM
        doc_list = ['document_rel_s1', 'document_rel_s2', 'document_rel_s3']
        return doc_list



