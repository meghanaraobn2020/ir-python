import pandas as pd

from python_scripts.document_preprocess import DocumentPreprocess


class DRMM:
    def __init__(self):
        self.df = DocumentPreprocess().document_preprocess()

    def get_relevant_documents(self, search_query):
        # DRMM logic
        doc_list = self.df['doc_id'].values.tolist()
        return doc_list
