# SkillsForAll
# Python Essentials 2 - 4.3.10 LAB
# Evaluating students' results

class StudentsDataException(Exception):
    def __init__(self, messsage):
        Exception.__init__(self, messsage)


class BadLine(StudentsDataException):
    def __init__(self, line_num, line, message):
        self.line_num = line_num
        self.line = line
        StudentsDataException.__init__(self, message)


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self, message)

def parseline(line_num, line):
    try:
        student_data = line.split()

        if len(student_data) < 3:
            raise BadLine(line_num, line, "Not enough fields")

        student = (student_data[0], student_data[1])

        if student not in students:
            students[student] = 0

        students[student] += float(student_data[2])

    except BadLine as e:
        raise e

    except ValueError:
        raise BadLine(line_num, line, "Cannot parse score")

    except:
        raise BadLine(line_num, line, "Error parsing line")


fn = input("Select a Student file to compact: ")

students = {}

try:
    f_in = open(fn, "rt")

    line = f_in.readline()
    line_num = 0
    while line != '':
        line_num += 1
        parseline(line_num, line)

        line = f_in.readline()

    if students == {}:
        raise FileEmpty("No students found");

    f_in.close()

except IOError:
    print("File not found");

except BadLine as e:
    print("Error at line", e.line_num, ":", e.line.rstrip(), ",", e.args[0])

except FileEmpty as e:
    print(e.args[0])


except Exception as e:
    print(e)
else:
    for student in sorted(students.keys()):
        print(student[0], student[1], students[student], sep="\t")
