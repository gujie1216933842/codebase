from datetime import date, datetime

'''
@property 把方法当成类属性



'''


class User():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    '''
    允许用属性的方式设值
    '''

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User('tom', date(year=1990, month=11, day=7))
    print(user.age)
    user._age = 11
    print(user._age)
    print(user.age)
