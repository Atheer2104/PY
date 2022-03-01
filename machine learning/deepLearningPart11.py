import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.ops import rnn, rnn_cell
from tensorflow.contrib import rnn

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)


#cycels feed forward + backprop
hm_epochs = 10

# how manu classes we have
n_classes = 10

#how many images in this example we take in before we manipulate weights
batch_size = 128

chunk_size = 28
n_chunks = 28
rnn_size = 128

#height x width
x = tf.placeholder('float',[None, n_chunks, chunk_size])
#label of x (data)
y  = tf.placeholder('float')

def recurrent_network_model(x ):
    # assign weights to a variabel weith random numbers we have to start somewhere and westart with something random
    #we multiply input_data and weight then we add biases (input * weight + biases)
    layer = {'weights':tf.Variable(tf.random_normal([rnn_size,n_classes])),
             'biases':tf.Variable(tf.random_normal([n_classes]))}

    x = tf.transpose(x, [1,0,2])
    x = tf.reshape(x, [-1, chunk_size])
    x = tf.split(x, n_chunks, 0)

    lstm_cell = rnn.BasicLSTMCell(rnn_size, state_is_tuple=True)
    outputs, states = tf.contrib.rnn.static_rnn(lstm_cell, x, dtype=tf.float32)

    output = tf.matmul(outputs[-1], layer['weights']) + layer['biases']

    return output

def train_neural_network(x):
    #assign that thw prediction should be the answear
    prediction = recurrent_network_model(x)
    #calucat the diffirence of the predicton to know label (y)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
    #optimizing
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        #training the network
        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                epoch_x = epoch_x.reshape((batch_size, n_chunks, chunk_size))
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)


        correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print('Accuracy:', accuracy.eval({x:mnist.test.images.reshape((-1, n_chunks, chunk_size)), y:mnist.test.labels}))


train_neural_network(x)
            
        



'''
input > weight > hidden layer 1 (activation function) > weights > hidden layer 2
(activation function) > weights > output layer

compare output to intended output > cost function (cross entropy)
optimaization function (optimizer) > minimize cost (AdamOptimizier....SGD, AdaGrad)

backpropagation

feed forward + backprop = epoch
'''


