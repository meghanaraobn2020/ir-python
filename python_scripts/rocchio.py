import operator

import numpy as np


class Rocchio:
    def __init__(self):
        print("Rocchio")

    @staticmethod
    def rocchio_algorithm(query_doc_vector, docs_relevant_vectors, docs_irrelevant_vectors, alpha, beta):
        sum_of_rel_doc_vectors = []
        sum_of_irrel_doc_vectors = []
        for each_rel_doc_vector in docs_relevant_vectors:
            if len(sum_of_rel_doc_vectors) == 0:
                sum_of_rel_doc_vectors = each_rel_doc_vector
            else:
                sum_of_rel_doc_vectors = list(map(operator.add, sum_of_rel_doc_vectors, each_rel_doc_vector))

        for each_irrel_doc_vector in docs_irrelevant_vectors:
            if len(sum_of_irrel_doc_vectors) == 0:
                sum_of_irrel_doc_vectors = each_irrel_doc_vector
            else:
                sum_of_irrel_doc_vectors = list(map(operator.add, sum_of_irrel_doc_vectors, each_irrel_doc_vector))

        new_doc_vector_query = np.array(query_doc_vector) + (
                    (alpha / len(docs_relevant_vectors)) * np.array(sum_of_rel_doc_vectors)) - (
                                           (beta / len(docs_irrelevant_vectors)) * np.array(sum_of_irrel_doc_vectors))

        return new_doc_vector_query
