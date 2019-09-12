#!/usr/bin/python
import time
import datetime 

pirm=  ['', '', 'English HL', 'English HL', 'IP', 'Lithuanian Literature SL', 'Lithuanian Literature SL', 'CS SL', 'CS SL' ]
antr=  ['CS SL', 'CS SL', 'Mathematics SL', 'Mathematics SL', 'IP', 'Physics SL', 'Physics SL', 'Economics SL', 'Economics SL' ]
trec=  ['St. Mess', 'English HL', 'English HL', 'Mathematics HL', 'Mathematics HL', 'IP', 'Religion', 'Physics SL', 'Physics SL' ]
ketv=  ['Lithuanian Literature SL', 'Lithuanian Literature SL', 'Economics SL', 'Economics SL', 'IP', 'TOK', 'TOK', 'CS HL', 'CS HL' ]
penkt=  ['Mathematics SL', 'Mathematics SL', 'English HL', 'English HL', '', '', '', '', '']

time = ['8:00-8:45', '8:55-9:40', '9:50-10:35', '10:40-11:25', '11:30-12:15', '12:25-13:10', '13:20-14:05', '14:15-15:00', '15:05-15:50']
time_r = [7*60, 8*60+55, 9*60+50, 10*60+40, 11*60+30, 12*60+25, 13*60+20, 14*60+15, 15*60+5] 

pirm_kab = ['', '', '408', '408', '', '402', '402', 'B205', 'B205']
antr_kab = ['B205', 'B205', '107', '107', '', 'B203', 'B203', '509', '509']
trec_kab = ['', '408', '408', '107', '107', '', '107', 'B203', 'B203']
ketv_kab = ['406', '406', '511', '511', '', '408', '408', 'B205', 'B205']
penkt_kab = ['107', '107', '408', '408', '', '', '', '', '']

class Pamoka(object):
    name = ""
    classroom = ""
    time = ""
    number =""

    def __init__(self, name, classroom, time, number):
        self.name = name
        self.classroom = classroom
        self.time = time
        self.number = number

def make_lesson(name, classroom, time, number):
    Lesson = Pamoka(name, classroom, time, number)
    if checktime() < time_r[number] and checktime() > time_r[number - 1]:
        if Lesson.name != '':
            print(Lesson.name + "  " + Lesson.classroom + "  " + Lesson.time)
            
def make_lesson_table(name, classroom, time, number):
    Lesson = Pamoka(name, classroom, time, number)
    if Lesson.name != '':
        print(Lesson.name + "  " + Lesson.classroom + "  " + Lesson.time)

#check time
def checktime():
    deftime = datetime.datetime.now()
    hour = deftime.hour
    minutes = deftime.minute
    time = hour*60+minutes
    return time

def checkday():
    weekday = datetime.datetime.today().weekday()
    return weekday
    
def output(day):
    if day == 0:
        for lesson in range(9):
            make_lesson(pirm[lesson], pirm_kab[lesson], time[lesson], lesson)
    elif day == 1:
        for lesson in range(9):
            make_lesson(antr[lesson], antr_kab[lesson], time[lesson], lesson)
    elif day == 2:
        for lesson in range(9):
            make_lesson(trec[lesson], trec_kab[lesson], time[lesson], lesson)
    elif day == 3:
        for lesson in range(9):
            make_lesson(ketv[lesson], ketv_kab[lesson], time[lesson], lesson)
    else:
        for lesson in range(9):
            make_lesson(penkt[lesson], penkt_kab[lesson], time[lesson], lesson)

def output_table(day):
    if day == 0:
        for lesson in range(9):
            make_lesson_table(pirm[lesson], pirm_kab[lesson], time[lesson], lesson)
    elif day == 1:
        for lesson in range(9):
            make_lesson_table(antr[lesson], antr_kab[lesson], time[lesson], lesson)
    elif day == 2:
        for lesson in range(9):
            make_lesson_table(trec[lesson], trec_kab[lesson], time[lesson], lesson)
    elif day == 3:
        for lesson in range(9):
            make_lesson_table(ketv[lesson], ketv_kab[lesson], time[lesson], lesson)
    else:
        for lesson in range(9):
            make_lesson_table(penkt[lesson], penkt_kab[lesson], time[lesson], lesson)

output(checkday())
print("---")
output_table(checkday())