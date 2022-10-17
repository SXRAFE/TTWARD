import html.parser

gradesTable = False
gradesRowHeader = False
gradeContainer = False
grades = {}
currentSubject = []
currentSubjectName = str()

class GradePageParser(html.parser.HTMLParser):

    # TODO: refactor because this is absolutely horrible
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        global gradesTable
        global grades
        global currentSubject
        global currentSubjectName
        global gradesRowHeader
        global gradeContainer

        if (tag == "tbody"):
            gradesTable = True
        if (gradesTable):
            if (tag == "tr"):
                currentSubject = []
                currentSubjectName = ""
            elif (tag == "th"):
                gradesRowHeader = True
            elif (len(attrs) > 0):
                if attrs[0][1] == "grade_container":
                    gradeContainer = True


    
    def handle_endtag(self, tag: str) -> None:
        global gradesTable
        global currentSubject
        global currentSubjectName
        if (tag == "table"):
            gradesTable = False
        if (tag == "tr"):
            currentSubject = []
            currentSubjectName = ""

    def handle_data(self, data: str) -> None:
        global grades
        global gradesTable
        global currentSubject
        global currentSubjectName
        global gradesRowHeader
        global gradeContainer
        # print("Data: " + data)
        if gradesTable:
            if data.rstrip() != "":
                if currentSubject == [] and currentSubjectName == "":
                    currentSubjectName = data
                if gradesRowHeader:
                    if not data in grades.keys():
                        grades[data] = []
                    gradesRowHeader = False
                if gradeContainer:
                    grades[currentSubjectName].append(data)
                    gradeContainer = False
                #print("Data: " + data)
        


file = open("grades.html", encoding="UTF-8")
rawHTML = ""

for line in file:
    rawHTML += line
file.close()

parser = GradePageParser()

parser.feed(rawHTML)

print(grades)