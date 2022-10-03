class SingletonConfigMeta(type):

    _instances = {}
    _data = None

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('Downloading config from database.')
            instance = super().__call__(*args, **kwargs)
            instance._data = 'Data'
            cls._instances[cls] = instance
        else:
            print('Singleton already exists.')
        return cls._instances[cls]


class ConfigSingleton(metaclass=SingletonConfigMeta):

    @classmethod
    def get_data(cls):
        return cls._instances[cls]._data


singleton1 = ConfigSingleton()
singleton2 = ConfigSingleton()

if id(singleton1) == id(singleton2):
    print('Works')
    print(singleton1.get_data())


# Downloading config from database.
# Singleton already exists.
# Works
# Data
