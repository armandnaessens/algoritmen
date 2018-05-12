class Ranker():

    def __init__(self,dataset,query_processor,binary_search_tree,bk_tree = None):
        self._dataset = dataset
        self._query_processor = query_processor
        self._binary_search_tree = binary_search_tree
        self._bk_tree = bk_tree

    def evaluate(self,query):
        import re
        TokenList = []
        TokenList.append([i for i in re.split(r'(\d+|W+)',query) if i]);
        