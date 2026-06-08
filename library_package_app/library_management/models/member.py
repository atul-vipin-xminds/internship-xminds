class Member:
    count = 0

    def __init__(self, name):
        self.__name = name

        Member.count += 1

    def get_name(self):
        return self.__name
