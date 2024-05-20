import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv('network_traffic.csv')

# Preprocess data
# Convert categorical features to numerical values
le = LabelEncoder()
df['protocol'] = le.fit_transform(df['protocol'])
df['flags'] = le.fit_transform(df['flags'].astype(str))

# Select features
features = df[['src_ip', 'dst_ip', 'src_port', 'dst_port', 'protocol', 'packet_length', 'flags']]
# For simplicity, let's encode IP addresses as numerical values
features['src_ip'] = features['src_ip'].apply(lambda x: int(''.join(x.split('.'))))
features['dst_ip'] = features['dst_ip'].apply(lambda x: int(''.join(x.split('.'))))

# Train-test split (if you have labeled data)
# labels = df['label']  # Assuming you have a label column indicating normal or anomaly
# X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Train Isolation Forest model (unsupervised)
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(features)

# Predict anomalies
df['predicted'] = clf.predict(features)

# Convert predictions from (-1 for anomaly, 1 for normal) to (0 for normal, 1 for anomaly)
df['predicted'] = df['predicted'].apply(lambda x: 1 if x == -1 else 0)

# Evaluate the model (if you have labeled data)
# print(classification_report(y_test, df['predicted']))

# Save predictions
df.to_csv('network_traffic_with_predictions.csv', index=False)
