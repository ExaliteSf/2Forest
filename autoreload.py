import subprocess
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SCRIPT_PATH = os.path.join("scripts", "map.py")

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.run_script()

    def run_script(self):
        if self.process:
            self.process.kill()
        print("🔁 Relancement de map.py...\n")
        self.process = subprocess.Popen(["python", SCRIPT_PATH])

    def on_modified(self, event):
        if event.src_path.endswith("map.py"):
            print("💾 Changement détecté !")
            self.run_script()

if __name__ == "__main__":
    print(f"👀 Surveillance de {SCRIPT_PATH}...")
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path="scripts", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Arrêt manuel.")
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()
