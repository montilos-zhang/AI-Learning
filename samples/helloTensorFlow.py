import tensorflow as tf
a = tf.constant(10)
b = tf.constant(20)

sess = tf.Session()

print(sess.run(a*b))

hello = tf.constant('hello, tensorflow')

print(sess.run(hello))