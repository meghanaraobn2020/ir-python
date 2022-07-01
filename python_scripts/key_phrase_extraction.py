import pke
from python_scripts.document_preprocess import DocumentPreprocess


class KeyPhraseExtraction:

    def __init__(self):
        self.df = DocumentPreprocess().document_preprocess()
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

    def get_key_phrases_for_every_doc(self, user_relevant_document_list):
        doc_key_phrases_list = []
        for doc in user_relevant_document_list:
            new_df = self.df.loc[self.df['doc_id'] == doc]
            doc_key_phrases_list.append(self.generate_key_phrases(new_df['pre_processed_text'].tolist()[0]))
        print('key_phrases:', doc_key_phrases_list)
        return doc_key_phrases_list


# should be removed
if __name__ == "__main__":
    document = """Inverse problems for a mathematical model of ion exchange in a compressible ion 
        exchanger.A mathematical model of ion exchange is considered, allowing for ion exchanger compression in the 
        process of ion exchange. Two inverse problems are investigated for this model, unique solve ability is proved, 
        and numerical solution methods are proposed. The efficiency of the proposed methods is demonstrated by a 
        numerical experiment.""".replace("\n", " ")
    KeyPhraseExtraction().get_key_phrases_for_every_doc(['FBIS3-1'])
