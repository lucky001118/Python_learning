# Starting with the standard imports
import numpy as np                          # numerical libraries
import pandas as pd                         # Pandas gives us the data-frame
np.random.seed(42)                          # for reproducible results
import tensorflow as tf


# Now the Graphical libraries imports and settings
#%matplotlib inline
import matplotlib.pyplot as plt             # for plotting
import seaborn as sns                       # nicer looking plots

plt.rcParams['figure.figsize'] = '20,10'
plt.rcParams['legend.fontsize'] = 16
plt.rcParams['axes.labelsize'] = 16
plt.style.use('ggplot')                     # emulate ggplot style

# For latex-quality legends
from matplotlib import rc
rc('font', family='serif')
rc('text', usetex=True)
rc('font', size=20)
import warnings
warnings.filterwarnings('ignore')           # suppress warning




#x_train = np.linspace(-1, 1, 100)
#y_train = 2*x_train + np.random.randn(*x_train.shape)*0.33

data = pd.read_csv("dataset-1.csv")
x_train = data.x
y_train = data.y
count = len(data.index)
plt.scatter(x_train, y_train)
plt.title(r'Scatterplot of $x\_train$ vs $y\_train$ showing a linear relationship')
plt.xlabel(r'$x\_train \longrightarrow $')
plt.ylabel(r'$y\_train \longrightarrow $')
plt.show()


# Now define the data-placeholders

X = tf.placeholder(tf.float64)
Y = tf.placeholder(tf.float64)

# Define the function for computing yhat
# We define the weight as scalar variable, in order to optimize it

w_start = np.random.rand(4)
w = tf.Variable (w_start, name="weights")
mu = 1

print("Initial weights" + str(w))

def lm(X, w):
    terms = 0
    for n in range(len(w_start)):
        terms = terms + tf.multiply(tf.pow(X, n), w[n])
    return terms

def penalty(w):
    total = 0.
    for n in range(len(w_start)):
        total += w[n]*w[n]
    return mu*total/count

# Based on this, we can express the formula of the yhat, and consequently the cost
yhat = lm(X, w)
cost = tf.reduce_sum(tf.square(Y - yhat))  + penalty(w)

train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

# Finally, let us now execute this code and see what happens.

training_epochs = 10000

with tf.Session () as session:
    init = tf.global_variables_initializer()
    session.run(init)

    for epoch in range(training_epochs):
        for x, y in zip (x_train, y_train):
            session.run(train_op, feed_dict={X: x, Y: y})

    w_val = session.run(w)

print (f"The weights are: {w_val}")
# Now, let us plot the scatter-plot along with the yhat.

plt.scatter(x_train, y_train)


def predict (x, w):
    result = 0
    for n in range(len(w)):
        result = result + (np.power(x,n)*w[n])
    return result


xx = np.linspace(0, 6.3, 1000)

prediction = predict(xx, w_val)
print (prediction)
plt.plot (xx, prediction, 'maroon', linewidth='6')
title = 'The prediction line: $y = \\vec w \\cdot \\vec x+ w_0$'
plt.title(fr'{title}')
plt.xlabel(r'$x \rightarrow $')
plt.ylabel(r'$y \rightarrow $')
plt.show()