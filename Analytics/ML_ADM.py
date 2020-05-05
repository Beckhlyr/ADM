from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus


print ("feature")
input_file = "KA.csv"
df = pd.read_csv(input_file, header=0)
df.head()
d = {'Y': 0, 'N': 1}
df['Response Type'] = df['Response Type'].map(d)
#df['Previous Searches'] = df['Previous Searches'].map(d)
df.head()
features = list(df.columns[:1])
print ("feature" + str(features))
y = df["Response Type"]
X = df[features]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)


dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=features)
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#Image(graph.create_png())

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

#Predict employment of an employed 10-year veteran
print(clf.predict([[55]]))
#...and an unemployed 10-year veteran
#print(clf.predict([[0]]))
 