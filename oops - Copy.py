"""defining the class for college data"""
final_record = {}
def set_record(name, roll, course, age):
    final_record[name] = {"roll_no": roll, "course": course, "age": age}

teacher_record = {}
def set_teacher_record(teachername, teachersubject):
    teacher_record[teachername] = {"teachersubject": teachersubject}

class College:
    """Defining the class"""

    def __init__(self, studentsname, rollno, courses, age, teachername, teachersubject):
        self.name = studentsname
        self.rollno = rollno
        self.course = courses
        self.age = age
        self.teachername = teachername
        self.teachersubject = teachersubject
        set_record(self.name, self.rollno, self.course, self.age)
        set_teacher_record(self.teachername, self.teachersubject)

    def get_studentsname(self):
        """Returns the student's name"""
        return self.name

    def get_rollno(self):
        """Returns the roll number of the student"""
        return self.rollno

    def get_course(self):
        """Returns the student's course"""
        return self.course

    def update_get_course(self, course):
        """Updates the student's course"""
        self.course = course

    def get_age(self):
        """Returns the student's age"""
        return self.age

    def get_teachername(self):
        """Returns the teacher's name"""
        return self.teachername

    def get_teachersubject(self):
        """Returns the subject taught by the teacher"""
        return self.teachersubject

    def update_get_teachersubject(self, subject):
        """Updates the teacher's subject"""
        self.teachersubject = subject

# Create the object instances for the College class
pankaj = College("pankaj", 1, "MCA", 21, "ashwani", "python")
manas = College("manas", 2, "MCA", 21, "ashwani", "python")
mohak = College("mohak", 3, "BCA", 20, "deepak", "nord")
gorv = College("gorv", 4, "BSC", 22, "dippika", "j.s")

# Print the list of student names
print(list(final_record.keys()))
print(final_record)
print(teacher_record)