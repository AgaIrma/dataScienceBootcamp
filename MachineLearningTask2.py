#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.datasets import make_classification
from sklearn.datasets import fetch_openml


def load_simple_classifier_dataset(weights=[0.5, 0.5]):

    X, y = make_classification(
        n_samples=1000,
        n_classes=len(weights),
        n_informative=len(weights),
        weights=weights,
        flip_y=0,
        random_state=1
    )

    return X, y

def load_mnist_data():

    mnist_data = fetch_openml('mnist_784', version=1)
    print("keys of data dictionary: ", mnist_data.keys())

    X, y = mnist_data['data'], mnist_data['target']

    return X, y, mnist_data.target_names
    
    #importujemy train_test_split
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.33, random_state=42)

