import queue
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class MessageAnnouncer:
    def __init__(self):
        self.listeners = []

    def listen(self):
        q = queue.Queue(maxsize=5)
        LOGGER.info(f"add listener: ")
        self.listeners.append(q)
        return q

    def announce(self, msg):
        for i in reversed(range(len(self.listeners))):
            try:
                LOGGER.info(f"announce: {msg}")
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]