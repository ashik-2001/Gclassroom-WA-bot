import quickstart


getCourseDetails = quickstart.main()

def courseAliases():
    courseName = []
    results = getCourseDetails.list(pageSize=20).execute()
    courses = results.get('courses', [])

    if not courses:
        return('No courses found.')
    
    for course in courses:
        courseName.append(f"{course['name']}")
    return(courseName)

def courseId(index):
    results = getCourseDetails.list(pageSize=20).execute()
    courses = results.get('courses', [])
    if not courses:
        return('No courses found.')
    return(courses[index]["id"])

def courseAssignments(courseId):
    assignment = getCourseDetails.courseWork().list(courseId = courseId).execute()
    topics = []
    for assignments in assignment["courseWork"]:
        topics.append(f"{assignments['title']} Due date = {assignments['dueDate']['day']}/{assignments['dueDate']['month']}/{assignments['dueDate']['year']} Time = {assignments['dueTime']['hours']}:{assignments['dueTime']['minutes']}==============================")
    return topics

#print(courseAssignments(courseId(1)))