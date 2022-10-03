from abc import ABC, abstractmethod


class User:
    pass


class Course(ABC):
    @abstractmethod
    def display(self, user):
        ...


class AccessCourse(Course):
    def display(self, user):
        print(f'Loading all courses for user {user.name}...')


class AccessCourseProxy(Course):
    def __init__(self, proxy):
        self.proxy = proxy

    def display(self, user):
        if user.fee > 0:
            print(f'{user.name} has to pay a fee.')
            return
        return self.proxy.display(user)


user_with_no_fee = User()
user_with_no_fee.fee = 0
user_with_no_fee.name = 'Jack'

user_with_fee = User()
user_with_fee.fee = 100
user_with_fee.name = 'David'

course = AccessCourse()
course_proxy = AccessCourseProxy(proxy=course)

course_proxy.display(user_with_no_fee)
course_proxy.display(user_with_fee)

# Loading all courses for user Jack...
# David has to pay a fee.
