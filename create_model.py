import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    'packet_length': [182, 147, 377, 1415, 859, 150, 350, 680, 700, 920],
    'anomaly_scores': [0.99, 0.45, 0.17, 0.63, 0.94, 0.38, 0.58, 0.76, 0.82, 0.49],
    'source_ip': [1, 1, 2, 3, 2, 1, 2, 3, 1, 2],
    'destination_ip': [3, 3, 2, 1, 3, 2, 1, 1, 2, 3],
    'severity_level': [2, 2, 1, 3, 2, 1, 2, 3, 1, 2],
    'attack_type': [0, 1, 1, 0, 2, 1, 2, 0, 1, 0]
}
df = pd.DataFrame(data)

X = df[['packet_length', 'anomaly_scores', 'source_ip', 'destination_ip']]
y_severity = df['severity_level']
y_attack = df['attack_type']

X_train, X_test, y_severity_train, y_severity_test = train_test_split(X, y_severity, test_size=0.2, random_state=42)
X_train, X_test, y_attack_train, y_attack_test = train_test_split(X, y_attack, test_size=0.2, random_state=42)

model_severity = LogisticRegression()
model_severity.fit(X_train, y_severity_train)

model_attack = LogisticRegression()
model_attack.fit(X_train, y_attack_train)

with open('model_severity.pkl', 'wb') as file:
    pickle.dump(model_severity, file)

with open('model_attack.pkl', 'wb') as file:
    pickle.dump(model_attack, file)

print("Models saved to 'model_severity.pkl' and 'model_attack.pkl'")
