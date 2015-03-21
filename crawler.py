#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import requests


QUESTION_URL = 'http://140.131.93.223/apig/himexam/exam1.asp'
ANSWER_URL = 'http://140.131.93.223/apig/himexam/exam2.asp'
LOOP_ANSWER = ['A', 'B']
RANGE = range(1001, 1501)
HTML_FILE = str(RANGE[0]) + '-' + str(RANGE[-1]) + '.html'
probno = 10000


### Get list of questions
for exam_number in RANGE:
	payload = {'ID':'A123456789', 'ProbNO':exam_number}
	result = requests.post(QUESTION_URL, data=payload)

	print 'question:' + str(exam_number)

	correct_answer = ''
	for ans in LOOP_ANSWER:  # A,B
		payload = {'ID':'A123456789',
				   'probno': probno + exam_number,
				   'ans': ans}  #10001
		answer = requests.post(ANSWER_URL, data=payload)
		
		if len(answer.content) != 255:
			correct_answer = answer.content
			break

	#print correct_answer	
	### Write everything we got to html files
	with open(HTML_FILE, 'a') as the_file:
		the_file.write(result.content)
		the_file.write('<br><br><font color="red"> %s </font><br><hr>' % correct_answer)

	the_file.closed
