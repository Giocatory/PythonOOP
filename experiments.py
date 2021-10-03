class St:
    name = 'Mike'

    def __init__(self):
        self.age = 20

    @classmethod
    def to_string(cls):
        return cls()


st = St.to_string()
print(st.name)
print(st.age)

print(type(st))
