import pke


class KeyPhraseExtraction:

    def __init__(self, document):
        self.extractor = pke.unsupervised.TopicRank()
        self.document = document
        self.key_phrases = self.generate_key_phrases()

    def generate_key_phrases(self):
        self.extractor.load_document(input=self.document, language='en')

        self.extractor.candidate_selection()

        self.extractor.candidate_weighting()

        key_phrases = self.extractor.get_n_best(n=20, stemming=False)

        key_phrase_candidates = []
        for i, (candidate, score) in enumerate(key_phrases):
            key_phrase_candidates.append(candidate)

        return key_phrase_candidates

# should be removed
if __name__ == "__main__":
    document = """Inverse problems for a mathematical model of ion exchange in a compressible ion 
        exchanger.A mathematical model of ion exchange is considered, allowing for ion exchanger compression in the 
        process of ion exchange. Two inverse problems are investigated for this model, unique solve ability is proved, 
        and numerical solution methods are proposed. The efficiency of the proposed methods is demonstrated by a 
        numerical experiment.""".replace("\n", " ")
    KeyPhraseExtraction(document)
