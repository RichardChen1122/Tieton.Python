import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """test"""