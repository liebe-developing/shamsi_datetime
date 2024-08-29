import numpy as np
import jdatetime
from datetime import datetime

class ShamsiDateTime:
    """
    A class to handle Shamsi (Jalali) dates with functionality for conversion
    to and from Gregorian dates, and formatting in both Persian and English.

    Attributes:
        shamsi_date (jdatetime.date): The Shamsi date object.
    """

    def __init__(self, year: int = None, month: int = None, day: int = None):
        """
        Initializes a ShamsiDateTime instance. Defaults to the current date if no arguments are provided.

        Args:
            year (int, optional): The year in the Shamsi calendar.
            month (int, optional): The month in the Shamsi calendar.
            day (int, optional): The day in the Shamsi calendar.

        Raises:
            ValueError: If the provided date is not valid in the Shamsi calendar.
        """
        if year is None or month is None or day is None:
            # Default to the current date
            current_date = jdatetime.date.today()
            self.shamsi_date = current_date
        else:
            try:
                self.shamsi_date = jdatetime.date(year, month, day)
            except ValueError as e:
                raise ValueError(f"Invalid Shamsi date: {e}")

    def to_gregorian(self) -> np.datetime64:
        """Convert the Shamsi date to Gregorian date in NumPy datetime64 format.

        Returns:
            np.datetime64: The corresponding Gregorian date.
        """
        return np.datetime64(self.shamsi_date.togregorian())

    @classmethod
    def from_gregorian(cls, gregorian_date: np.datetime64) -> "ShamsiDateTime":
        """Create a ShamsiDateTime instance from a Gregorian date in NumPy datetime64 format.

        Args:
            gregorian_date (np.datetime64): The Gregorian date.

        Returns:
            ShamsiDateTime: An instance of ShamsiDateTime representing the equivalent Shamsi date.

        Raises:
            ValueError: If the conversion from Gregorian date fails.
        """
        try:
            g_date = gregorian_date.astype(object)
            shamsi_date = jdatetime.date.fromgregorian(date=g_date)
            return cls(shamsi_date.year, shamsi_date.month, shamsi_date.day)
        except Exception as e:
            raise ValueError(f"Error converting from Gregorian: {e}")

    def format_shamsi(self) -> str:
        """Format the Shamsi date in a full descriptive string format in Persian.

        Returns:
            str: The formatted Shamsi date in Persian.
        """
        day_of_week = self._get_persian_day_of_week(self.shamsi_date.strftime('%A'))  # Day of the week in Persian
        day = self._convert_to_persian_digits(self.shamsi_date.day)
        month = self._get_persian_month(self.shamsi_date.month)  # Get correct Persian month name
        year = self._convert_to_persian_digits(self.shamsi_date.year)
        return f"{day_of_week} - {day} {month} {year}"

    def format_gregorian(self) -> str:
        """Format the Gregorian date in a full descriptive string format in English.

        Returns:
            str: The formatted Gregorian date in English.
        """
        g_date = self.shamsi_date.togregorian()  # Convert to Gregorian
        day_of_week = g_date.strftime('%A')  # Day of the week in English
        day = g_date.day
        month = g_date.strftime('%B')  # Month name in English
        year = g_date.year
        return f"{day_of_week} - {year} {day} {month}"

    def format_bilingual(self) -> str:
        """Format the Shamsi date in a full descriptive bilingual string format.

        Returns:
            str: The formatted date in both English (Gregorian) and Persian (Shamsi).
        """
        return f"{self.format_gregorian()}\n{self.format_shamsi()}"

    def _convert_to_persian_digits(self, number: int) -> str:
        """Convert English digits in the number to Persian digits.

        Args:
            number (int): The number to convert.

        Returns:
            str: The number with Persian digits.
        """
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"
        number_str = str(number)
        translation_table = str.maketrans(english_digits, persian_digits)
        return number_str.translate(translation_table)

    def _get_persian_month(self, month_number: int) -> str:
        """Get the correct Persian month name based on the Shamsi month number.

        Args:
            month_number (int): The month number in the Shamsi calendar.

        Returns:
            str: The Persian month name.
        """
        persian_months = [
            'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
            'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
        ]
        return persian_months[month_number - 1]  # Adjust for zero-based index

    def _get_persian_day_of_week(self, day_name: str) -> str:
        """Convert English days of the week to Persian.

        Args:
            day_name (str): The English day name.

        Returns:
            str: The Persian day name, or the original if not found.
        """
        days_translation = {
            'Saturday': 'شنبه',
            'Sunday': 'یک‌شنبه',
            'Monday': 'دوشنبه',
            'Tuesday': 'سه‌شنبه',
            'Wednesday': 'چهارشنبه',
            'Thursday': 'پنج‌شنبه',
            'Friday': 'جمعه'
        }
        return days_translation.get(day_name, day_name)  # Default to the same if not found

    def __str__(self) -> str:
        """String representation of the Shamsi date.

        Returns:
            str: The date in YYYY-MM-DD format.
        """
        return f"{self.shamsi_date.year}-{self.shamsi_date.month:02d}-{self.shamsi_date.day:02d}"

    def __eq__(self, other: object) -> bool:
        """Equality comparison for ShamsiDateTime instances.

        Args:
            other (object): Another ShamsiDateTime instance to compare.

        Returns:
            bool: True if both instances represent the same Shamsi date, False otherwise.
        """
        if isinstance(other, ShamsiDateTime):
            return self.shamsi_date == other.shamsi_date
        return False