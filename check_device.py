import psutil
import socket
import platform

def check_os():
    return platform.platform()

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_memory():
    return psutil.virtual_memory().percent

def check_disk():
    disk = psutil.disk_usage("/")
    return disk.percent

def check_network():
    interfaces = psutil.net_if_stats()
    return any(iface.isup for iface in interfaces.values())

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def main():
    print(f"OS: {check_os()}")
    print(f"CPU負荷: {check_cpu()}%")
    print(f"メモリ使用率: {check_memory()}%")
    print(f"ディスク使用率: {check_disk()}%")
    print(f"ネットワーク稼働中: {check_network()}")
    print(f"インターネット接続: {check_internet()}")

if __name__ == "__main__":
    main()
