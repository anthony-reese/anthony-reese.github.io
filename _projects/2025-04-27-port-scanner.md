---
layout: post
title: "🛡️ Port Scanner"
tags: [Qt, C++, CLI, Networking]
date: 2025-04-27 13:41:01 +0400
description: "A tool that allows users to input an IP address and scan a range of TCP ports."
categories: projects
---
### 🔍 Overview
A minimal C++ port scanner using Qt. Clean and responsive GUI for scanning open TCP ports.

### 🚀 Features
- Built with Qt Creator for performance and cross-platform support
- Input an IP address and scan a range of TCP ports
- Uses `QTcpSocket` with asynchronous UI updates
- Displays response time for each open port

### 🛡️ How Port Scanner Works
The program uses QTcpSocket to attempt TCP connections to a range of ports on a specified IP address.
If the connection succeeds, it is considered "open" and the response time is recorded.

### 📸 Preview
![Port Scanner Output]({% link assets/images/port-scanner-demo.png %})

### 💻 Demo
```sh  
Enter IP address: 127.0.0.1  
Enter start port: 1  
Enter end port: 200

Scanning 127.0.0.1 from port 1 to 200...  
Port 22 is open (Response Time: 9 ms)  
Port 80 is open (Response Time: 13 ms)  
Port 135 is open (Response Time: 15 ms)  
```

### 🔗 View Code
- 🔧 [Source Code on GitHub](https://github.com/anthony-reese/port-scanner)
