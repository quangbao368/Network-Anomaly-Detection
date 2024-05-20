import pyshark
import pandas as pd

# Read the PCAP file
capture = pyshark.FileCapture('network_traffic.pcap')

# Function to extract features
def extract_features(packet):
    features = {}
    try:
        features['src_ip'] = packet.ip.src
        features['dst_ip'] = packet.ip.dst
        features['src_port'] = packet[packet.transport_layer].srcport
        features['dst_port'] = packet[packet.transport_layer].dstport
        features['protocol'] = packet.transport_layer
        features['packet_length'] = packet.length
        features['flags'] = packet.tcp.flags if 'TCP' in packet else 'N/A'
    except AttributeError as e:
        pass
    return features

# Process packets and build the dataset
data = []
for packet in capture:
    features = extract_features(packet)
    if features:
        data.append(features)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file (optional)
df.to_csv('network_traffic.csv', index=False)
