import tensorflow as tf
import numpy as np

iris_t = "../resources/tensor_tests/iris_training.csv"
iris_e = "../resources/tensor_tests/iris_test.csv"

def input_fn_train():
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=iris_t, target_dtype=np.int, features_dtype=np.float32)
    return tf.convert_to_tensor(training_set.data), tf.convert_to_tensor(training_set.target)


def input_fn_eval():
    testing_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=iris_e, target_dtype=np.int, features_dtype=np.float32)
    return tf.convert_to_tensor(testing_set.data), tf.convert_to_tensor(testing_set.target)

def main():
    # Specify that all features have real-value data
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

    # Build 3 layer DNN with 10, 20, 10 units respectively.
    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[2],
                                                n_classes=3,
                                                model_dir="/tmp/iris_model")

    # Fit model.
    classifier.fit(input_fn=input_fn_train,
                   steps=2000)

    # Evaluate accuracy.
    accuracy_score = classifier.evaluate(input_fn=input_fn_eval)["accuracy"]
    print('Accuracy: {0:f}'.format(accuracy_score))

main()