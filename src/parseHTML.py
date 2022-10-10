import html.parser

gradesTable = False
grades = {list()}

class GradePageParser(html.parser.HTMLParser):

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        global gradesTable
        if (len(attrs) > 0):
            if (attrs[0][1] == "student_lessons_grades  not_separate_summary_lessons"):
                gradesTable = True
    
    def handle_endtag(self, tag: str) -> None:
        global gradesTable
        if (tag == "table"):
            gradesTable = False

    def handle_data(self, data: str) -> None:
        # print("Data: " + data)
        if gradesTable and data.rstrip() != "":
            print("Data: " + data)


file = open("grades.html", encoding="UTF-8")
rawHTML = ""

for line in file:
    rawHTML += line
file.close()

parser = GradePageParser()

parser.feed(rawHTML)