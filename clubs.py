class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")


class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, student):
        self.members.append(student)
        print(f"{student.name} Joined {self.name}!")

    def show_members(self):
        print(f"Members in {self.name}:")
        for member in self.members:
            print(member.name)


student_1 = Student("Joseph", 19)
student_2 = Student("Kulankash", 23)
student_3 = Student("Sienna", 18)
student_4 = Student("Enock", 22)

student_1.introduce()
student_2.introduce()
student_3.introduce()
student_4.introduce()

chess_club = Club("Chess Club")
drama_club = Club("Drama Club")
gaming_club = Club("Gaming Club")

chess_club.add_member(student_1)
chess_club.add_member(student_2)
drama_club.add_member(student_3)
gaming_club.add_member(student_4)

chess_club.show_members()
drama_club.show_members()
gaming_club.show_members()