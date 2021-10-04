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
st2 = Student(22)
st3 = Student.create_student(75)
st4 = st1.create_student(1)
st5 = st2.new_student(2)

Student.How_many_class_created()  # 5
st1.How_many_class_created()  # 5
