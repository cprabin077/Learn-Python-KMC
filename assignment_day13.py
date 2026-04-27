class School():
    def __init__(self, name, *marks):
        self.name = name
        self.marks = marks

    def avg(self):
        if len(self.marks)==0:
            return "Zero division Error", False
        return sum(self.marks)/len(self.marks), True
    
    def grade(self):
        grade_avg = self.avg()

        if grade_avg[1]:
            average = grade_avg[0]

            if average>=100:
                return "A+"
            else:
                return "Fail"
        else:
            return "Error"

    def display(self):
        if not self.avg()[1]:
            return self.avg()[0]
        else:
            return f'Name={self.name}\nMarks={self.marks}\nAverage={self.avg()}\nGrade={self.grade()}'


obj = School("Sudan")
obj1 = School("Sudan", 13,56,80)
print(obj.display())
print(obj1.display())
