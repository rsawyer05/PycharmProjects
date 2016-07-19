# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

dicts = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(dicts):

    max_teacher = ""
    max_classes = 0

    for teacher in dicts:
        if len(dicts[teacher]) > max_classes:
            max_classes = len(dicts[teacher])
            max_teacher = teacher

    return max_teacher

def num_teachers(dicts):
    return len(dicts)

def stats(dicts):
    teacher_classes = []
    for name, value in dicts.items():
        new_string = [name, len(value)]
        teacher_classes.append(new_string)
    return teacher_classes

def courses(dicts):
    courses = []
    for value in dicts.values():
        courses += value

    return courses







