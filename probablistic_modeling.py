class _Encounter(object):
    def __init__(self, event):
        self.__event = event

    def occurs(self, num1, num2):
        return self.__event(num1, num2)


class ProbableCapacity(object):
    def __init__(self, capacity):
        self.__capacity = capacity

    def occurs(self, num):
        return num / self.__capacity


class ProbableEvent(object):
    def __init__(self, chance_rate):
        self.__chance_rate = chance_rate

    def occurs(self, num):
        return self.__chance_rate * num


class ProbableEncounter(object):
    def __init__(self, event, chance_rate):
        self.__encounter = _Encounter(event)
        self.__probable_event = ProbableEvent(chance_rate)

    def occurs(self, num1, num2):
        return self.__probable_event.occurs(self.__encounter.occurs(num1, num2))

    @property
    def encounter(self):
        return self.__encounter

    @property
    def probable_event(self):
        return self.__probable_event
