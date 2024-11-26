import ujson
from machine import RTC


class RTCStorage:
    def __init__(self):
        self._rtc = RTC()
        self._data = self._load()

    def _load(self):
        try:
            data = self._rtc.memory()
            return ujson.loads(data) if data else {}
        except:
            return {}

    def _save(self):
        try:
            self._rtc.memory(ujson.dumps(self._data))
            return True
        except:
            return False

    def set(self, key, value):
        current = self._data.get(key)
        if current != value:
            self._data[key] = value
            return self._save()
        return True

    def get(self, key, default=None):
        return self._data.get(key, default)

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            return self._save()
        return True

    def clear(self):
        self._data.clear()
        return self._save()

    def data(self):
        return self._data


rtc_storage = RTCStorage()
