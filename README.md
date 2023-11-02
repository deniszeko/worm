## Because a worm is just a little snake, right?

This is a friendly challenge to practice Python by building a worm simulator class.

Main ``Worm`` class has a single class variable ``food`` which represents a shared storage of food available to every instance of class. Instances are initialized with self-describing ``length`` and ``energy`` properties, which cannot be lesser than 1 each. A newborn worm is always 0 days old and is ``alive`` until it dies.

Four instance methods exist:
- ``eat()`` increases worm's ``energy`` by consuming ``food`` (rate is configured). It is the only method which accepts a numerical argument: a worm can eat an arbitrary number of food.
- ``dig()`` restocks ``food`` by wasting ``energy`` (rates are configured).
- ``grow()`` adds to ``length`` in exchange for exactly 1 ``energy`` (rate is configured), but no more than maximal length.
- ``divide()`` returns two newborn worm instances with parent worm's ``length`` and ``energy`` split roughly in half. Parent worm is then flagged as both dead (``alive = False``) and ``divided``. There are some restrictions for a division to be available: hardcoded ``length`` and ``energy`` (at least 2 each) and configured minimal ``age``.

After any of those methods successfully invoked, a worm with ``energy`` lesser than zero is flagged as dead (``alive = False``). A dead worm cannot use its methods, raising an exception instead. A worm with a positive energy becomes 1 day older, and is ready for another action.