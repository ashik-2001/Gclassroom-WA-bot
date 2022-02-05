from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import dataOrganizer, re

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False
	
	result = re.match('\d', incoming_msg)
	if 'help' in incoming_msg:
		msg.body("Type -Courses- for list courses. Enter its corresponding number (eg: 1) to see the assignments in it")
		responded = True
	elif 'courses' in incoming_msg:
		listCourses = dataOrganizer.courseAliases()
		if listCourses == "No courses found.":
			msg.body(listCourses)
			responded = True
			return str(resp)
		count = 0
		for courses in listCourses:
			count += 1
			msg.body(f"{count}. {courses}")
		responded = True
	elif result: #IF THE MESSAGE IS A INTEGER do--
		listCourses = dataOrganizer.courseAliases()
		if listCourses == "No courses found.":
			msg.body(listCourses)
			responded = True
			return str(resp)
		courseId = dataOrganizer.courseId(int(incoming_msg)-1)
		try:
			for topics in dataOrganizer.courseAssignments(courseId):
				msg.body(f"{topics} \n")
			responded = True
		except:
			msg.body("No Courses Found OR some error occured")
			responded = True
	else:
		msg.body("Please type 'help' for the list of commands")
		responded = True

	if not responded:
		msg.body("Sorry some error is occuring")
	return str(resp)

if __name__ == "__main__":
	app.run()