import project as p
import binarytree as b
import bktree as bk
import ranker as r
import metrics as m
import redblacktree as rb
import pickle
query_processor = p.QueryProcessor()
dataset = pickle.load(open('dataset.p', 'rb'))
bktree = bk.BKTree(m.levenshtein_distance_DP)
token_bookids = dataset.get_token_bookids()
words = dataset.get_dictionary()
for word in words:
    bktree.insert(query_processor.process(word))
pickle.dump(open('bkpickle.p', 'wb'))
RBtree = rb.RedBlackTree()
for book in token_bookids:
    RBtree.insert(book[0], book[1])
Ranker = r.Ranker(dataset, query_processor, RBtree, bktree)
print(Ranker.evaluate('The search engine'))