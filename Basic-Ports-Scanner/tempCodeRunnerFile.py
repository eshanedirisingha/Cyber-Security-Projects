import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the socket connection
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def start_scan():
    target_ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = scan_ports(target_ip, start_port, end_port)
    
    if open_ports:
        result_text.insert(tk.END, "Open ports:\n")
        for port in open_ports:
            result_text.insert(tk.END, f"{port}\n")
    else:
        result_text.insert(tk.END, "No open ports found.\n")

# Set up the GUI
root = tk.Tk()
root.title("Port Scanner")

# Load logo image
logo_img = tk.PhotoImage(file="black.png")

# Create a frame for widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# Logo label at the top
logo_label = tk.Label(frame, image=logo_img)
logo_label.grid(row=0, columnspan=2, pady=5)

ip_label = tk.Label(frame, text="IP Address:")
ip_label.grid(row=1, column=0, padx=5, pady=5)
ip_entry = tk.Entry(frame)
ip_entry.grid(row=1, column=1, padx=5, pady=5)

start_port_label = tk.Label(frame, text="Start Port:")
start_port_label.grid(row=2, column=0, padx=5, pady=5)
start_port_entry = tk.Entry(frame)
start_port_entry.grid(row=2, column=1, padx=5, pady=5)

end_port_label = tk.Label(frame, text="End Port:")
end_port_label.grid(row=3, column=0, padx=5, pady=5)
end_port_entry = tk.Entry(frame)
end_port_entry.grid(row=3, column=1, padx=5, pady=5)

scan_button = tk.Button(frame, text="Start Scan", command=start_scan)
scan_button.grid(row=4, column=0, columnspan=2, pady=10)

result_text = scrolledtext.ScrolledText(root, width=50, height=15)
result_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
