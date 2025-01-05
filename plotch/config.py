import copy
from .config_default import DEFAULT


class Config:
    def __init__(self):
        self._defaults = copy.deepcopy(DEFAULT)
        self.reset()

    def reset(self):
        """Reset all settings to their default values."""
        self._current = copy.deepcopy(self._defaults)

    def update(self, **kwargs):
        """Update settings with provided keyword arguments."""
        for key, value in kwargs.items():
            if key in self._defaults:
                self._current[key] = value
            else:
                raise KeyError(f"Invalid configuration key: {key}")

    def __getitem__(self, key):
        return self._current.get(key, None)

    def __setitem__(self, key, value):
        if key in self._defaults:
            self._current[key] = value
        else:
            raise KeyError(f"Invalid configuration key: {key}")

    def get(self, key, default=None):
        return self._current.get(key, default)

    def as_dict(self):
        """Return a copy of the current configuration as a dictionary."""
        return copy.deepcopy(self._current)


Params = Config()
