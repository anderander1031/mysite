class Student:
    sid = 'unknown'
    name = 'unknown'
    gender = 'unknown'
    height = 0
    weight = 0
    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
    def set_height(self, h):
        self.height = h
    def set_weight(self, w):
        self.weight = w
    def info(self):
        return '{:10}{:10}{:10}{:10}{:10}'
class BmiReport:
    name = 'unknown'
    sts = []
    def __init__(self,name):
        self.name = name
    def add_student(self, st):
        self.sts.append(st)
    def save_file(self):
        with open('result.txt', 'w') as f:
            f.write(self.name)
            f.write('\n')

def test1():
  report = BmiReport("Class A")

  # or just call report.import_file("bmi-input.txt")
  input()
  for line in sys.stdin:
    arr = line.split()

    st = Student(arr[0], arr[1], arr[2])
    st.set_height(float(arr[3]))
    st.set_weight(float(arr[4]))
    report.add_student(st)

  report.save_file("class-a.db")

def test2():
  report = BmiReport("")
  report.read_file("class-a.db")
  report.print_report()

def test3():
  report = BmiReport("")
  report.read_file("class-a.db")
  report.remove_student("A01") 
  st = Student("A10", "Easter", "M")
  st.set_height(160)
  st.set_weight(65)
  report.add_student(st)
  report.save_file("result2.txt")

def test4():
  report = BmiReport("")
  ...
  opts = {
    'height': 170,
    'weight': 75
  }
  report.update_student("A10", opts)
  ...

def read_file():
    with open('student.txt') as f:
        first = f.readline()
        report = BmiReport(first)
        for line in f:
            ts = line.split(',')
            st = Student(ts[0], ts[1], ts[2])
            st.set_height = float(ts[3])
            st.set_weight = float(ts[4])
            report.add.
read_file()
