class Student:
    _how_many_class_created = 0

    def __init__(self, id_student):
        self.id = id_student  # instance attribute
        Student._how_many_class_created += 1

    @staticmethod
    def How_many_class_created():
        print(Student._how_many_class_created)

    @staticmethod
    def create_student(id_student):
        return Student(id_student)

    @classmethod
    def new_student(cls, id_student):
        return cls(id_student)


st1 = Student.new_student(12)
st2 = Student.new_student(13)
st3 = Student.new_student(55)
st4 = Student.new_student(102)
st5 = Student.create_student(75)

Student.How_many_class_created()
st1.How_many_class_created()
