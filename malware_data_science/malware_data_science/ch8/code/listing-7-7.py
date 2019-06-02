# import sklearn modules
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
# initialize the decision tree classifier and vectorizer
classifier = tree.DecisionTreeClassifier()
vectorizer = DictVectorizer(sparse=False)
# declare toy training data
training_examples = [
{'packed':1,'contains_encrypted':0},
{'packed':0,'contains_encrypted':0},
{'packed':1,'contains_encrypted':1},
{'packed':1,'contains_encrypted':0},
{'packed':0,'contains_encrypted':1},
{'packed':1,'contains_encrypted':0},
{'packed':0,'contains_encrypted':0},
{'packed':0,'contains_encrypted':0},
]
ground_truth = [1,1,1,1,0,0,0,0]
# initialize the vectorizer with the training data
vectorizer.fit(training_examples)

# transform the training examples to vector form
X = vectorizer.transform(training_examples)
y = ground_truth # call ground truth 'y', by convention
# train the classifier (a.k.a. 'fit' the classifier)
classifier.fit(X,y)
test_example = {'packed':1,'contains_encrypted':0}
test_vector = vectorizer.transform(test_example)
print `classifier.predict(test_vector)` # prints [1]
#visualize the decision tree
with open("classifier.dot","w") as output_file:
    tree.export_graphviz(
        classifier,
        feature_names=vectorizer.get_feature_names(),
        out_file=output_file
    )

import os
os.system("dot classifier.dot -Tpng -o classifier.png")
