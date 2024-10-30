import requests
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import threading
import logging

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

print("\nMemulai program monitoring website...")

url = input("\nMasukkan URL website yang akan dipantau (contoh: https://www.example.com): ")

# Inisialisasi deque untuk menyimpan data
request_counts = deque(maxlen=60)
response_times = deque(maxlen=60)
total_requests = 0
suspicious_threshold = 50

def make_request():
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        return 1, end_time - start_time
    except requests.RequestException:
        return 0, 0

def monitor_traffic():
    global total_requests
    while True:
        successful_requests = 0
        total_response_time = 0
        
        for _ in range(10):
            success, response_time = make_request()
            successful_requests += success
            total_response_time += response_time
        
        request_counts.append(successful_requests)
        avg_response_time = total_response_time / 10 if successful_requests > 0 else 0
        response_times.append(avg_response_time)
        total_requests += successful_requests

        avg_requests = sum(request_counts) / len(request_counts) if request_counts else 0
        status = "Normal" if avg_requests < suspicious_threshold else "PERINGATAN"
        
        logger.info(f"Status: {status} | "
                   f"Requests: {avg_requests:.2f}/s | "
                   f"Avg Response: {avg_response_time:.3f}s | "
                   f"Total Requests: {total_requests}")
        
        time.sleep(1)

# Membuat figure dan axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle(f'Website Traffic Monitoring: {url}', fontsize=12)

# Inisialisasi lines dan fills
line1, = ax1.plot([], [], 'r-', linewidth=2)
line2, = ax2.plot([], [], 'r-', linewidth=2)
fill1 = None
fill2 = None

# Konfigurasi axes
ax1.set_ylabel('Requests per Second')
ax1.grid(True, alpha=0.3)
ax2.set_ylabel('Response Time (seconds)')
ax2.set_xlabel('Time (last 60 seconds)')
ax2.grid(True, alpha=0.3)

# Threshold line
threshold_line = ax1.axhline(y=suspicious_threshold, color='yellow', linestyle='--', linewidth=2)

def update_plot(frame):
    global fill1, fill2
    
    if len(request_counts) > 1:
        x = list(range(len(request_counts)))
        
        # Update traffic rate plot
        line1.set_data(x, list(request_counts))
        
        # Remove old fill_between and create new one
        if fill1 is not None:
            fill1.remove()
        fill1 = ax1.fill_between(x, list(request_counts), color='red', alpha=0.3)
        
        ax1.set_xlim(0, len(request_counts))
        ax1.set_ylim(0, max(max(request_counts) * 1.1, suspicious_threshold * 1.2))
        
        # Update response time plot
        line2.set_data(x, list(response_times))
        
        # Remove old fill_between and create new one
        if fill2 is not None:
            fill2.remove()
        fill2 = ax2.fill_between(x, list(response_times), color='red', alpha=0.3)
        
        ax2.set_xlim(0, len(response_times))
        ax2.set_ylim(0, max(response_times) * 1.1 if response_times else 1)

        # Update warning text
        avg_requests = sum(request_counts) / len(request_counts)
        if avg_requests > suspicious_threshold:
            warning_text = f"PERINGATAN: Kemungkinan serangan! ({avg_requests:.2f} req/s)"
            plt.figtext(0.5, 0.95, warning_text, ha='center', va='top',
                       color='yellow', fontweight='bold', fontsize=12,
                       bbox=dict(facecolor='red', alpha=0.8, edgecolor='none'))
        else:
            plt.figtext(0.5, 0.95, '', ha='center', va='top')

    return line1, line2

print("\nMemulai monitoring...")
print("Tekan Ctrl+C untuk menghentikan program")

try:
    monitor_thread = threading.Thread(target=monitor_traffic)
    monitor_thread.daemon = True
    monitor_thread.start()

    ani = FuncAnimation(fig, update_plot, interval=1000, blit=False)
    plt.tight_layout()
    plt.show()

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh user")
except Exception as e:
    logger.error(f"Error tidak terduga: {e}")
finally:
    plt.close(fig)
