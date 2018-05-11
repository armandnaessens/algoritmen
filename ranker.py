class Ranker():

    def __init__(self,dataset,query_processor,binary_search_tree,bk_tree = None):
        self._dataset = dataset
        self._query_processor = query_processor
        self._binary_search_tree = binary_search_tree
        self._bk_tree = bk_tree

    def evaluate(self,query):
        tokens = self._query_processor.process(query)
        results = {}
        for token in tokens:
           intermediate_results = self._binary_search_tree.get(token)
           if len(intermediate_results) < 5:
               token = self._bk_tree.get(token, 2)
               for tok in token:
                   intermediate_results + self._binary_search_tree.get(tok)
           for book_id in intermediate_results:
               if book_id in results.keys():
                   results[book_id] += 1
               else:
                   results[book_id] = 1
        #dictionary nog sorteren
        return results