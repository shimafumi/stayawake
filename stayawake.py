import time
import ctypes
from datetime import datetime

_ES_CONTINUOUS = 0x80000000
_ES_SYSTEM_REQUIRED = 0x00000001
_ES_DISPLAY_REQUIRED = 0x00000002

if __name__ == '__main__':
    print(" " * 10, datetime.now())
    ctypes.windll.kernel32.SetThreadExecutionState(
        _ES_CONTINUOUS | _ES_DISPLAY_REQUIRED | _ES_SYSTEM_REQUIRED)
    try:
        while True:
            print(" " * 10, datetime.now(), end="\r", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        ctypes.windll.kernel32.SetThreadExecutionState(_ES_CONTINUOUS)