import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import joblib

# Create a sample dataset
data = {
    'Timestamp': [
        '2024-02-02 15:11:19', '2024-01-25 18:06:30',
        '2024-01-16 16:00:31', '2024-04-05 02:03:46'
    ],
    'Source IP Address': ['145.242.59.216', '31.214.67.69', '21.42.170.185', '232.202.154.198'],
    'Destination IP Address': ['173.84.51.30', '220.92.111.74', '154.230.158.198', '171.221.165.59'],
    'Source Port': [61475, 44255, 62389, 20453],
    'Destination Port': [8357, 32725, 27183, 24154],
    'Protocol': ['FTP', 'TCP', 'ICMP', 'HTTPS'],
    'Packet Length': [182, 147, 377, 1415],
    'Packet Type': ['Response', 'Request', 'Request', 'Error'],
    'Traffic Type': ['Malicious', 'Malicious', 'Malicious', 'Malicious'],
    'Malware Indicators': [False, False, True, False],
    'Anomaly Scores': [0.99, 0.45, 0.17, 0.63],
    'Alerts/Warnings': [True, True, True, True],
    'Attack Type': [1, 0, 1, 0]  # 1 for malicious, 0 for normal
}

df = pd.DataFrame(data)

# Select features and target variable
X = df[['Anomaly Scores', 'Packet Length']]
y = df['Attack Type']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'models/model2.pkl')
