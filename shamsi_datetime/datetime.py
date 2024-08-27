import numpy as np
import jdatetime
from datetime import datetime

class ShamsiDateTime:
    def __init__(self, year=None, month=None, day=None):
        if year is None or month is None or day is None:
            # Default to the current date
            current_date = jdatetime.date.today()
            self.shamsi_date = current_date
        else:
            self.shamsi_date = jdatetime.date(year, month, day)
    
    def to_gregorian(self):
        """Convert the Shamsi date to Gregorian date in NumPy datetime64 format."""
        return np.datetime64(self.shamsi_date.togregorian())
    
    @classmethod
    def from_gregorian(cls, gregorian_date):
        """Create a ShamsiDateTime instance from a Gregorian date in NumPy datetime64 format."""
        g_date = gregorian_date.astype(object)
        shamsi_date = jdatetime.date.fromgregorian(date=g_date)
        return cls(shamsi_date.year, shamsi_date.month, shamsi_date.day)
    
    def __str__(self):
        return f"{self.shamsi_date.year}-{self.shamsi_date.month:02d}-{self.shamsi_date.day:02d}"
    
    def __eq__(self, other):
        if isinstance(other, ShamsiDateTime):
            return self.shamsi_date == other.shamsi_date
        return False