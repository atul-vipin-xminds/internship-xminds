class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            print("Database Connection Created")
            cls._instance = super().__new__(cls)

        return cls._instance