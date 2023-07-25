import sys
import gpiozero
import time
from datetime import datetime
import threading

from consts import PUMP_GPIO, PUMP_RUNTIME, PUMP_RUN_INTERVAL
from controller_library import EventLogger

pumpRelay = gpiozero.OutputDevice(PUMP_GPIO, active_high=False, initial_value=False)


def poll():
    lastLog = EventLogger.log_event('LatestPumpRun', 'Get')  # Fetch the last pump run
    interval = 0

    if lastLog is not None:
        lastTimestamp = datetime.fromtimestamp(float(lastLog['time']))
        interval = (datetime.now() - lastTimestamp).total_seconds()
    else:
        interval = PUMP_RUN_INTERVAL + 1

    if interval > PUMP_RUN_INTERVAL:
        runPump()


def runPump():
    pumpRelay.on()
    time.sleep(PUMP_RUNTIME)  # Keep pump running for PUMP_RUNTIME seconds.
    pumpRelay.off()

    # Log this run
    EventLogger.log_event('Pump', 'Run')  # Log the pump run


def heartbeat():
    EventLogger.log_event('Heartbeat', '1')  # Log the heartbeat
    # threading.Timer(600, heartbeat).start() - Handled by crontab


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'runnow':
        runPump()
    else:
        heartbeat()
        poll()

