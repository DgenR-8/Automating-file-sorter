import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/Jdsta/Downloads"
dest_dir_sfx = "/Users/Jdsta/Sounds"
dest_dir_music = "/Users/Jdsta/Sounds/Music"
dest_dir_video = "/Users/Jdsta/Videos"
dest_dir_image = "/Users/Jdsta/Images"
dest_dir_exe = "/Users/Jdsta/Desktop/Exe Files"
dest_dir_zip = "/Users/Jdsta/Desktop/Zip Files"
dest_dir_links = "/Users/Jdsta/Desktop/Hyperlink Files"

def makeUnique(path):
    filename, extension = splitext(path)
    counter = 1

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry,dest)

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries: 
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith ('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('mp4'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('jpeg') or name.endswith('.png'):
                    dest = dest_dir_image
                    move(dest, entry, name)
                elif name.endswith('.exe'):
                    dest = dest_dir_exe
                    move(dest, entry, name)
                elif name.endswith('.zip'):
                    dest = dest_dir_zip
                    move(dest, entry, name)
                elif name.endswith('.htm'):
                    dest = dest_dir_links
                    move(dest, entry, name)
            


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()