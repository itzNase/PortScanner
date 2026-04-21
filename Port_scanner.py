import subprocess
import sys
def install(package):
    subprocess.call([sys.executable, '-m', 'pip', 'install', package])
try:
    import colorama
except ImportError:
    install('colorama')
    import colorama
    colorama.init()
import threading
import socket
from colorama import Fore, Style, init
init(autoreset=True, strip=False, convert=False)
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
print(Style.DIM + Fore.RED + (r"""
  __  __           _        ____          _   _                
 |  \/  | __ _  __| | ___  | __ ) _   _  | \ | | __ _ ___  ___ 
 | |\/| |/ _` |/ _` |/ _ \ |  _ \| | | | |  \| |/ _` / __|/ _ \
 | |  | | (_| | (_| |  __/ | |_) | |_| | | |\  | (_| \__ \  __/
 |_|  |_|\__,_|\__,_|\___| |____/ \__, | |_| \_|\__,_|___/\___|
                                  |___/                        """))
lock = threading.Lock()
semaphore = threading.Semaphore(500)
threads = []
open_ports = []
invalid_ip = False
total_ports = 65535
scanned = [0]
def print_progress(cuurent, total):
    percent = int((cuurent / total) * 100)
    bar = '█' * (percent // 2) + "░" * (50 - percent // 2)
    print(f'\rScaning: |{bar}| {percent}% |', end='', flush=True)
def scan_port(ip, port, Timeout):
    global invalid_ip
    with semaphore:
        try:
            s = socket.socket()
            s.settimeout(Timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                with lock:
                    open_ports.append(port)
            s.close()
        except socket.gaierror:
            with lock:
                invalid_ip = True
    with lock:
        scanned[0] += 1
        print_progress(scanned[0], total_ports)
try:
    print(Fore.WHITE + (f"Results may vary depending on firewall settings."))
    print(Fore.BLUE + (f"127.0.0.1"), Fore.RED + ("→"), Fore.YELLOW + ("scans your local machine most reliable"))
    print(Fore.BLUE + ("192.168.x.x"), Fore.RED + ("→"), Fore.YELLOW + ("may be blocked by windows firewall  "))
    IP = input(Style.DIM + Fore.LIGHTWHITE_EX + (f"Target IP: "))
    try:
        socket.inet_aton(IP)
    except socket.error:
        print(Fore.RED + (f"Invalid IP address '{IP}'"))
        input("Press Enter to exit...")
        sys.exit()
    if IP == "127.0.0.1":
        Timeout = 0.3
    else:
        Timeout = 1
    ports = range(1, 65536)
    for port in ports:
        t = threading.Thread(target=scan_port, args=(IP, port, Timeout))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    if invalid_ip:
            print(Fore.RED + (f"Invalid IP address '{IP}'"))
    elif open_ports:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Found {len(open_ports)} open ports:")
            for port in sorted(open_ports):
                print(Fore.GREEN + f" [OPEN PORT {port}]")
    else:
            print(Fore.RED + f"No open ports found.")
except Exception as e:
    print(Fore.RED + (f"an erorr accured {e}"))
finally:
    print(Fore.WHITE + 'Operation Finished.' + Style.RESET_ALL)
    input("Press Enter to exit...")
