import psutil
import platform
import json
import logging
from datetime import datetime

# Configure a basic logger for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdminMonitor:
    """
    A class to gather and log essential cross-platform system information.
    Designed for authorized system monitoring and diagnostics.
    """

    def __init__(self, log_file="system_admin_log.json"):
        """Initializes the monitor and sets the log file path."""
        self.log_file = log_file

    def get_system_info(self) -> dict:
        """
        Collects core OS, CPU, Memory, and Disk information.
        """
        try:
            info = {
                "timestamp": datetime.now().isoformat(),
                "os_name": platform.system(),
                "os_release": platform.release(),
                "cpu_cores_physical": psutil.cpu_count(logical=False),
                "cpu_cores_logical": psutil.cpu_count(logical=True),
                "memory_total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
                "memory_percent_used": psutil.virtual_memory().percent,
                "disk_usage_root_percent": psutil.disk_usage('/').percent,
            }
            return info
        except Exception as e:
            logging.error(f"Error gathering system info: {e}")
            return {"error": str(e)}

    def log_info_to_file(self, data: dict):
        """
        Appends the collected system data to the designated JSON log file.
        """
        try:
            with open(self.log_file, 'a') as f:
                json.dump(data, f)
                f.write('\n') # Newline for each log entry
            logging.info(f"System data successfully logged to {self.log_file}")
        except IOError as e:
            logging.error(f"Failed to write to log file {self.log_file}: {e}")

    # Functional Step (Method) to run the full process
    def run_system_check(self) -> dict:
        """
        Performs a full monitoring cycle: gather data and log it.
        Returns the data dictionary.
        """
        system_data = self.get_system_info()
        self.log_info_to_file(system_data)
        return system_data

# Simple Function for quick interaction outside the class
def quick_check():
    """A standalone function to instantiate and run a quick check."""
    monitor = AdminMonitor()
    monitor.run_system_check()
    print(f"\n✅ Quick check complete. See '{monitor.log_file}' for details.")