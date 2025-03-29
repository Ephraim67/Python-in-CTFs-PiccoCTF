## **Python in CTFs - PicoCTF** 

### **Overview**  
This repository contains Python scripts and solutions for various **PicoCTF** challenges. It serves as a resource for learning and applying Python in **Capture The Flag (CTF)** competitions, focusing on cryptography, reverse engineering, forensics, and automation.  

### **Contents**  
- 🔹 **Cryptography** – Solving encryption/decryption challenges.  
- 🔹 **Reverse Engineering** – Analyzing binaries with Python.  
- 🔹 **Forensics** – Extracting hidden data from files.  
- 🔹 **Exploitation** – Automating interactions with remote services.  

### **Getting Started**  
#### **Prerequisites**  
Ensure you have Python installed:  
```bash
python3 --version
```
If it is not installed, get it from [Python.org](https://www.python.org/downloads/).  

#### **Clone the Repository**  
```bash
git clone https://github.com/Ephraim67/Python-in-CTFs-PiccoCTF.git
cd Python-in-CTFs-PiccoCTF
```

#### **Install Dependencies**  
If any challenge requires additional libraries, install them using:  
```bash
pip install -r requirements.txt
```

#### **Run a Script**  
```bash
python3 challenge_script.py
```

### **Examples**  
#### 🔹 **Basic Cryptography Script**  
```python
from base64 import b64decode

encoded = "U2VjcmV0IEZsYWc="  # Example base64 encoded string
decoded = b64decode(encoded).decode()
print(decoded)  # Output: Secret Flag
```

#### 🔹 **Automating a Netcat Connection**  
```python
import socket

host, port = "jupiter.challenges.picoctf.org", 64287
s = socket.socket()
s.connect((host, port))
print(s.recv(1024).decode())  # Receive and print flag
s.close()
```

### **Contributing**  
If you'd like to contribute:  
1. Fork the repo  
2. Create a new branch: `git checkout -b my-feature`  
3. Commit your changes: `git commit -m "Added new challenge solution"`  
4. Push and open a Pull Request  

### **Resources**  
- 🔗 [PicoCTF Website](https://picoctf.org/)  
- 📜 [Python Docs](https://docs.python.org/3/)  
- 🛠️ [Cybersecurity Learning Resources](https://tryhackme.com/)  

### **License**  
This project is open-source and licensed under the **MIT License**.  
