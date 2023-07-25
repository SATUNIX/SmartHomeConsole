from tinydb import TinyDB, Query
import logging
import subprocess
from datetime import datetime
'''
New DBMS to logging system
Possibly look into using mySQL


'''
db = TinyDB('events.json')

class EventLogger:
    @staticmethod
    def log_event(event_type, action):
        try:
            logging.info(f"{event_type} {action}")
            subprocess.run(["mpv", f"{event_type.lower()}_{action.lower()}.mp3"], check=True)
            log_entry = {'event': f'{event_type} {action}', 'time': str(datetime.now())}
            db.insert(log_entry)  # Log the event
        except Exception as e:
            logging.error(f"Error for {event_type} {action}: {str(e)}")

class Action:
    @staticmethod
    def on():
        EventLogger.log_event(str(__class__.__name__), 'ON')

    @staticmethod
    def off():
        EventLogger.log_event(str(__class__.__name__), 'OFF')

class Fountain(Action):
    pass

class Plants(Action):
    pass

class TopLight(Action):
    pass

class BackLight(Action):
    pass

class Loggable:
    @staticmethod
    def log(value):
        EventLogger.log_event(str(__class__.__name__), value)

class Temperature(Loggable):
    pass

class UV(Loggable):
    pass

class Humidity(Loggable):
    pass

class Precipitation(Loggable):
    pass

class PM25(Loggable):
    pass



