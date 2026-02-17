class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of the class.
        :return: The new instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
