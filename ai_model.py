"""
This module only run once to create a model file based on the given training content.
It helps to make the prediction process much faster by pre-processing the training data and storing it in a serialized format.

"""

from type_ai import Train
import pickle

train = Train()

with open("model.pkl", "wb") as f:
    pickle.dump(train.dictionary, f)

print("Model saved!")