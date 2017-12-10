import pickle
import os
from collections import OrderedDict

newpath = r'../../Encoded Data Structures (Phase 3)/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

path = r'../../../Phase 1/Task 1/Encoded Data Structures/Encoded-BM25-NoRelevance-Top100Docs-perQuery'
queryID_top100Docs = {}
for file in os.listdir(path):
    doc_bm25Score = {}
    current_file = os.path.join(path,file)
    string = current_file.split("Encoded-Top100Docs-BM25-NoRelevance_")
    id = string[1].split(".")[0]
    with open(current_file, 'rb') as f:
        doc_bm25Score = pickle.loads(f.read())
    all_docs = list(doc_bm25Score.keys())
    top_100_docs = all_docs[:100]
    queryID_top100Docs[id] = top_100_docs

queryID_top100Docs_sorted = OrderedDict(sorted(queryID_top100Docs.items(), key=lambda x: x,reverse=False))

output = open(newpath + 'Encoded-QueryID_Top100Docs_BM25_NoRelevance.txt', 'wb')
pickle.dump(queryID_top100Docs_sorted, output)
output.close()