import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.preprocessing.sequence import pad_sequences

data_dict = pickle.load(open('./data.pickle', 'rb'))

data = data_dict['data']

# Pad sequences to the maximum length found in the data
max_length = max(len(element) for element in data)
data = pad_sequences(data, maxlen=max_length, padding='post', dtype='float32')

# Convert to a NumPy array
data = np.asarray(data)

labels = np.asarray(data_dict['labels']) 

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)