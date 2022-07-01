import pandas as pd
import re


class DocumentPreprocess:
    def __init__(self):
        self.csv_path = 'C:/Users/megha/Git_Repo/IR_Project/ir-python/preprocessed_ten_trec_docs.csv'

    def document_preprocess(self):
        data_frame = pd.read_csv(self.csv_path)
        data_frame['pre_processed_text'] = [self.pre_process(x) for x in data_frame['text']]
        return data_frame

    def pre_process(self, document_text):
        new_doc_text = document_text.replace('\n', ' ').replace('\r', '')
        new_doc_text = re.sub("[^a-zA-Z0-9 :\.]", "", new_doc_text)
        return new_doc_text

