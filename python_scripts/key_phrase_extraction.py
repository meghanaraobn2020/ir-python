import pke
import re
import pandas as pd


class KeyPhraseExtraction:

    def __init__(self):
        self.extractor = pke.unsupervised.TopicRank()

    def generate_key_phrases(self, document_text):
        self.extractor.load_document(input=document_text, language='en')

        self.extractor.candidate_selection()

        self.extractor.candidate_weighting()

        key_phrases = self.extractor.get_n_best(n=20, stemming=False)

        key_phrase_candidates = []
        for i, (candidate, score) in enumerate(key_phrases):
            key_phrase_candidates.append(candidate)

        return key_phrase_candidates

    def pre_process(self, document_text):
        new_doc_text = document_text.replace('\n', ' ').replace('\r', '')
        new_doc_text = re.sub("[^a-zA-Z0-9 :\.]", "", new_doc_text)
        return new_doc_text

    def pre_process_and_save_key_phrases(self, csv_path):
        df = pd.read_csv(csv_path)
        df['pre_processed_text'] = [self.pre_process(x) for x in df['text']]
        df['key_phrases'] = [self.generate_key_phrases(x) for x in df['pre_processed_text']]
        return df


# should be removed
if __name__ == "__main__":
    document = """Inverse problems for a mathematical model of ion exchange in a compressible ion 
        exchanger.A mathematical model of ion exchange is considered, allowing for ion exchanger compression in the 
        process of ion exchange. Two inverse problems are investigated for this model, unique solve ability is proved, 
        and numerical solution methods are proposed. The efficiency of the proposed methods is demonstrated by a 
        numerical experiment.""".replace("\n", " ")
    KeyPhraseExtraction(document)
