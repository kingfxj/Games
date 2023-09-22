class Countdown:
    def __init__(self):
        self.a = 1
        self.b = 2

    def europe(self):
        self.b = self.b + 1

    def final(self):
        print(self.a + self.b)


c = Countdown()
c.europe()
c.final()


class Person:
    def __init__(self, age, grade):
        self.age = age
        self.grade = grade

    def update(self):
        self.grade *= 2
        return self.grade


student = Person(16, '10')
print(student.update())

