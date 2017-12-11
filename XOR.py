from networkComparison import NetworkComparer
import json
import numpy as np

trainingData = [
    {"input": [1, 1],
     "output": [0]},
    {"input": [0, 1],
     "output": [1]},
    {"input": [1, 0],
     "output": [1]},
    {"input": [0, 0],
     "output": [0]}]

testData = [
    {"input": [1, 1],
     "output": [0]},
    {"input": [0, 1],
     "output": [1]},
    {"input": [1, 0],
     "output": [1]},
    {"input": [0, 0],
     "output": [0]}]

networkData = [
    {"fnc_activate_type": "tanH",
     "fnc_learn_type": "BP",
     "learn_rate": [0.1, 0.15, 0.2, 0.25],
     "layers": [2, 3, 1],
     "weight_matrix": None,
     "rnd_values_low": -0.3,
     "rnd_values_high": 0.3,
     "max_iterations": 10000
     }]

weight_matrix = np.load("weight_matrix_final_np.npy")

networkComparer = NetworkComparer(
    networkData=networkData,
    trainingData=trainingData,
    testData=testData
)
networkComparer.compareNetworks()

