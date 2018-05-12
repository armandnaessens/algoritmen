class Ranker():

    def __init__(self,dataset,query_processor,binary_search_tree,bk_tree = None):
        self._dataset = dataset
        self._query_processor = query_processor
        self._binary_search_tree = binary_search_tree
        self._bk_tree = bk_tree

    def evaluate(self,query):
<<<<<<< HEAD
        import re
        TokenList = []
        TokenList.append([i for i in re.split(r'(\d+|W+)',query) if i]);
                
=======
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
        list_results = [(key, value) for key, value in results.items()]
        results_sorted = sorted(list_results, key = lambda tup: tup[1], reverse = True)
        return results_sorted
>>>>>>> d9718b05af071a628eae9844c0b9593dfa21c859
