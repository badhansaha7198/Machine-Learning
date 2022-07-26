import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

# We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Now we have to separate the feature columns from the target column.
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

# Create a Decision Tree
# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
# data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# graph = pydotplus.graph_from_dot_data(data)
# graph.write_png('test.png')
#
# img = pltimg.imread('test.png')
# imgplot = plt.imshow(img)
# plt.show()


# print(X)
# print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[30, 5, 6, 2]]))

print("[1] means 'GO'")
print("[0] means 'ON'")