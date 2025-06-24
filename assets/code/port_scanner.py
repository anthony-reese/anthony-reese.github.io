"""
Basic TCP Port Scanner in Python

⚠️ For educational use only. Use this responsibly and only scan IPs you are authorized to scan.
"""

import socket
import sys

# 🎯 Target IP address (update this!)
IP_ADDRESS = '127.0.0.1'

# 📶 Port range to scan
START_PORT = 1
END_PORT = 1023  # Well-known ports

def scan_ports():
    """
    Scans a range of TCP ports on a target IP and reports which ports are open.
    """
    print(f"🔎 Starting scan on {IP_ADDRESS} (Ports {START_PORT}-{END_PORT})")

    for port in range(START_PORT, END_PORT + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # ⏱️ Timeout after 1 second
            result = sock.connect_ex((IP_ADDRESS, port))  # 0 = success

            if result == 0:
                print(f"✅ Port {port} is OPEN")
            # Uncomment to show closed ports:
            # else:
            #     print(f"❌ Port {port} is closed")

if __name__ == "__main__":
    try:
        scan_ports()
    except KeyboardInterrupt:
        print("\n🚪 Scan aborted by user.")
        sys.exit()
    except socket.gaierror:
        print("❗ Invalid hostname.")
        sys.exit()
    except socket.error as e:
        print(f"💥 Socket error: {e}")
        sys.exit()
