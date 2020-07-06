import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def relu(x):
    return np.maximum(x, 0)

def output_results(num1, num2, num3, num4):
    bias_layer1 = np.load('bias_layer1.npy')
    bias_layer2 = np.load('bias_layer2.npy')
    bias_output = np.load('bias_output.npy')
    weights_layer1 = np.load('weights_layer1.npy')
    weights_layer2 = np.load('weights_layer2.npy')
    weights_output = np.load('weights_output.npy')
    X_mean = np.load('X_mean.npy')
    X_std = np.load('X_std.npy')

    labels = np.load('Labels.npy')

    features = []

    features.append(num1)
    features.append(num2)
    features.append(num3)
    features.append(num4)

    for i in range(0,4):
        features[i] = (features[i] - X_mean[i])/X_std[i]
    ftr = np.asarray(features)

    layer1 = relu(np.add(np.matmul(ftr,weights_layer1),bias_layer1))

    layer2 = relu(np.add(np.matmul(layer1,weights_layer2),bias_layer2))

    logits = np.add(np.matmul(layer2,weights_output),bias_output)

    output_activ = softmax(logits)

    out = output_activ.argsort()[-5:][::-1]

    output = []

    for key in out:
        output.append(labels[key])

    return output
