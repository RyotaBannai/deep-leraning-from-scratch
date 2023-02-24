import pickle

import numpy as np

from libs.dataset.mnist import load_mnist

from .functions import sigmoid, softmax


def get_test_data():
    _, (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    return x_test, t_test


def init_network():
    with open("./x/sample_weight.pkl", "rb") as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


if __name__ == "__main__":

    x, t = get_test_data()
    network = init_network()
    accuracy_cnt = 0
    batch_size = 100
    for i in range(0, len(x), batch_size):
        x_batch = x[i : i + batch_size]  # batch_size * image size (100,784)
        y = predict(network, x_batch)
        # 行ごとに最も確率の高い要素のインデックスを取得
        p = np.argmax(y, axis=1)
        accuracy_cnt += np.sum(p == t[i : i + batch_size])

    print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
