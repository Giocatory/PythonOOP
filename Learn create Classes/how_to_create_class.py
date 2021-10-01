class Counter:
    def start_from(self, count=0):
        self.counter = count

    def increment(self):
        self.counter += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.counter}")

    def reset(self):
        self.start_from()


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

c2 = Counter()
c2.start_from(3)
c2.display()
c2.increment()
c2.display()
c2.increment()
c2.display()
