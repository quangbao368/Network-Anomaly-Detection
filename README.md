# Network Anomaly Detection

This repository contains code and resources for detecting network anomalies, including Nmap scans, using machine learning and network traffic analysis. The project utilizes Wireshark for capturing network traffic, PyShark for preprocessing, and scikit-learn for building an anomaly detection model.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Network Anomaly Detection aims to identify suspicious activities and potential threats in network traffic. This project focuses on detecting Nmap scans and other anomalies using a combination of signature-based detection and machine learning techniques.

## Features

- Capture network traffic using Wireshark or tcpdump.
- Preprocess PCAP files to extract relevant features.
- Train and evaluate an Isolation Forest model for anomaly detection.
- Detect and label anomalies in network traffic.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Python Libraries

Install the required Python libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Capture Network Traffic
Use Wireshark or tcpdump to capture network traffic and save it as a PCAP file.

Example using tcpdump:

```bash
tcpdump -i eth0 -w network_traffic.pcap
```

### Step 2: Preprocess the PCAP File
Use the preprocess_pcap.py script to extract features from the PCAP file.

### Step 3: Train and Evaluate the Model
Use the train_model.py script to train and evaluate the Isolation Forest model.
