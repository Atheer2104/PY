import tensorflow as tf
import numpy as np
#from tensorflow.examples.tutorials.mnist import input_data

#mnist = input_data.read_data_sets("tmp/data/", one_hot=True)

from deepLearingPart5 import create_feature_sets_and_labels

train_x, train_y, test_x, test_y = create_feature_sets_and_labels('pos.txt', 'neg.txt')

#how many nodes we have in hidden layer
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

# how manu classes we have
n_classes = 2

#how many images in this example we take in before we manipulate weights
batch_size = 100

#height x width
x = tf.placeholder('float',[None, len(train_x[0])])
#label of x (data)
y  = tf.placeholder('float')

def neural_network_model(data):
    # assign weights to a variabel weith random numbers we have to start somewhere and westart with something random
    #we multiply input_data and weight then we add biases (input * weight + biases)
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([len(train_x[0]),n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    #creating all the different hidden layers
    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes]))}
    # now doing the calculation with (data * weights) + biases
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])

    #passing it through the activation function
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output

def train_neural_network(x):
    #assign that thw prediction should be the answear
    prediction = neural_network_model(x)
    #calucat the diffirence of the predicton to know label (y)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
    #optimizing
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    #cycels feed forward + backprop
    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        #training the network
        for epoch in range(hm_epochs):
            epoch_loss = 0
            
            i = 0
            while i < len(train_x):
                start = i
                end = i+batch_size

                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])
                
                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})
                epoch_loss += c
                i += batch_size
                
            print('Epoch', epoch+1, 'completed out of', hm_epochs, 'loss:', epoch_loss)


        correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print('Accuracy:', accuracy.eval({x:test_x ,y:test_y}))


train_neural_network(x)
