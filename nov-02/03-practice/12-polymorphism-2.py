class Teacher:
    def readsub(self):
        print("Teacher advises to read 2 hours")


class LazyStudent(Teacher):
    def readsub(self):
        print("LazyStudent never read at all")


class PerfectStudent(Teacher):
    def readsub(self):
        print(" Perfect Student 2hrs reading and practicing")


ls=LazyStudent()
ls.readsub()

ps=PerfectStudent()
ps.readsub()