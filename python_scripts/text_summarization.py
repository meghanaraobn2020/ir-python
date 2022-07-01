import re

from gensim.summarization import summarize
from gensim.summarization import keywords

from python_scripts.document_preprocess import DocumentPreprocess


class TextSummarization:
    def __init__(self):
        self.df = DocumentPreprocess().document_preprocess()

    @staticmethod
    def generate_text_summarization_keywords(document):
        new_doc_text = document.replace('\n', ' ').replace('\r', '')
        new_doc_text = re.sub("[^a-zA-Z0-9 :\.]", "", new_doc_text)
        document_summaries = summarize(new_doc_text, ratio=0.2)
        document_keywords = keywords(new_doc_text, ratio=0.2, split=True)
        return [document_summaries, document_keywords]

    def get_text_summaries_for_every_doc(self, user_relevant_document_list):
        document_summaries_list = []
        document_keywords_list = []
        for document in user_relevant_document_list:
            new_df = self.df.loc[self.df['doc_id'] == document]
            document_summaries, document_keywords = self.generate_text_summarization_keywords(new_df['pre_processed_text'].tolist()[0])
            document_summaries_list.append(document_summaries)
            document_keywords_list.append(document_keywords)
        print('Summaries', document_summaries_list)
        print('keywords', document_keywords_list)
        return [document_summaries_list, document_keywords_list]


