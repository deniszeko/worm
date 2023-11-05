class BadNewWorm(Exception):
    """When the newly initialized worm has length or energy less than 1."""

    def __init__(self, *args, **kwargs):
        super().__init__("New worm's length or energy cannot be less than 1.",
                         *args, kwargs)
        # Above "kwargs" goes without asterisk so that Exception() could treat that whole
        # dictionary as a single positional argument and store it as the last item of
        # instance's .args tuple attribute. Exception() will not accept keyword arguments
        # otherwise. It's certainly overcomplicated, but let it be for now.


class NotEnoughFood(Exception):
    """When there's not enough food available for consumption."""

    def __init__(self, *args, **kwargs):
        super().__init__("Not enough food available.",
                         *args, kwargs)


class MaxLengthReached(Exception):
    """When the worm is already at max length and can't grow more."""

    def __init__(self, *args, **kwargs):
        super().__init__("Maximal length is reached.",
                         *args, kwargs)


class CannotDivide(Exception):
    """When the worm is unable to divide due to insufficient parameters."""

    def __init__(self, *args, **kwargs):
        super().__init__("Worm is unable to divide.",
                         *args, kwargs)


class DividedWorm(Exception):
    """When the worm had already divided and effectively doesn't exist anymore."""

    def __init__(self, *args, **kwargs):
        super().__init__("This worm had divided and doesn't exist anymore.",
                         *args, kwargs)


class DeadWorm(Exception):
    """When the worm is dead."""

    def __init__(self, *args, **kwargs):
        super().__init__("This worm is dead.",
                         *args, kwargs)
