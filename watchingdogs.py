import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

count = 0

"""
def on_created(event):



def on_deleted(event):

"""

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")


#creating your own class cuz why not?
class NeObserver(Observer):
    pass

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = "."
    go_recursively = True
    my_observer = NeObserver()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
