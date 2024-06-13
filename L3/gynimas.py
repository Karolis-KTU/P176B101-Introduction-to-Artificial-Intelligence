import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from tensorflow import keras
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Generate parabola
x_parabola = np.linspace(-5, 5, 500)
y_parabola = x_parabola**2

# Generate random dots
dots_x = np.random.uniform(-5, 5, 500)
dots_y = np.random.uniform(-7, 30, 500)

# Create DataFrame
data = pd.DataFrame({'x': dots_x, 'y': dots_y})

# Add label column: 1 if the dot is above the parabola, 0 otherwise
data['label'] = np.where(data['y'] > data['x']**2, 1, 0)

# Prepare data for training
X = data[['x', 'y']]
y = data['label']
kf = KFold(n_splits=10, shuffle=True)

scores = []
lr = 0.001

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Create model
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(10, input_dim=X_train.shape[1], activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    optimizer = keras.optimizers.Adam(learning_rate=lr)
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    
    model.fit(X_train, y_train, epochs=50, batch_size=32)

    score = model.evaluate(X_test, y_test, verbose=0)
    scores.append(score[1])



print(f'Average accuracy: {np.mean(scores)}')

# Predict the labels for the entire dataset after all training is done
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

# Plotting
plt.plot(x_parabola, y_parabola, label='Parabola')

# plt.scatter(X['x'], X['y'], c=y, cmap=ListedColormap(('red', 'blue')), label='Actual')
plt.scatter(X['x'], X['y'], c=predictions, cmap=ListedColormap(('red', 'blue')), label='Predicted')

plt.title('Parabola, above/below testing')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# # Interactive plot
# plt.plot(x_parabola, y_parabola, label='Parabola')
# plt.title("Yay, It's interactive!")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show(block=False)

# while True:
#     # Use ginput to add points by clicking
#     points = plt.ginput(n=1, timeout=0)

#     if not points:
#         break

#     x, y = points[0]
#     prediction = model.predict(np.array([[x, y]]))
#     prediction = (prediction > 0.5).astype(int)

#     color = 'blue' if prediction else 'red'
#     plt.scatter(x, y, c=color)

# plt.show()