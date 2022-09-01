import statistics


class Joiners:
    """
    Contains Statistical functions which are used to squeeze
    time series values into a single value.
    In a few cases, it's not possible for cloud to squeeze the values
    due to value_type limitations, so it's processed manually at our end.
    """

    min = min
    max = max
    mean = statistics.mean
    sum = sum

    @staticmethod
    def first(values):
        """Return first value"""
        return values[0]

    @staticmethod
    def last(values):
        """return last value"""
        return values[-1]
