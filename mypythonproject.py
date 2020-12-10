import pandas as pd
from pybliometrics.scopus import ScopusSearch
import os
q = "AU-ID(7004212771)"  # any query that works in the Advanced Search on scopus.com
s = ScopusSearch(q)
df = pd.DataFrame(s.results)
path = "C:\\Users\\shrre\\PycharmProjects\\MyProjectPythonCode"
output_file = os.path.join(path, 'Combined Book.csv')
df.to_csv(output_file)
