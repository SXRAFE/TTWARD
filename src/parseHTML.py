import html.parser
import requests
import dotenv

acceptedValues = ['5', '4', '3', '2', '1', 'A', 'MA']
config = dotenv.dotenv_values(".env")

print(str(config))

# Due to the architecture of this library, the parsing has to be done like this with
# these boolean values that indicate if we're in certain sections of the HTML page.
# For example, if the overriden handle_starttag method detects that the parser has
# entered a grade_container section of the page, it sets the gradeContainer flag to True
# so that handle_data adds the next occurring data to the grades dictionary 

class GradePageParser(html.parser.HTMLParser):

    gradesTable = False
    gradesRowHeader = False
    gradeContainer = False
    grades = {}
    currentSubject = []
    currentSubjectName = str()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if (tag == "tbody"):
            self.gradesTable = True
        if (self.gradesTable):
            if (tag == "tr"):
                self.currentSubject = []
                self.currentSubjectName = ""
            elif (tag == "th"):
                self.gradesRowHeader = True
            elif (len(attrs) > 0):
                if attrs[0][1] == "grade_container":
                    self.gradeContainer = True

    def handle_endtag(self, tag: str) -> None:
        if (tag == "table"):
            self.gradesTable = False
        if (tag == "tr"):
            self.currentSubject = []
            self.currentSubjectName = ""

    def handle_data(self, data: str) -> None:
        # print("Data: " + data)
        if self.gradesTable:
            if data.rstrip() != "":
                if self.currentSubject == [] and self.currentSubjectName == "":
                    self.currentSubjectName = data
                if self.gradesRowHeader:
                    if not data in self.grades.keys():
                        self.grades[data] = []
                    self.gradesRowHeader = False
                if self.gradeContainer:
                    if data in acceptedValues:
                        self.grades[self.currentSubjectName].append(data)
                    self.gradeContainer = False
                #print("Data: " + data)

def fetchGrades() -> dict:


    # HTTP headers for login request
    loginHeaders = {
        "Host": config["STUUDIUM_BASE_URL"].removeprefix("https://"),
        "user-agent": "insomnia/2022.6.0",
        "cookie": "",
        "accept": "*/*",
        "accept-language": "en-GB,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "",
        "origin": "https://tamme.ope.ee",
        "referer": "https://tamme.ope.ee/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "te": "trailers",
        "x-requested-with": "XMLHttpRequest",
        "content-length": "105"
    }

    # Form data payload
    loginPayload = "_auth_ui_version=3&data%5BUser%5D%5Busername%5D=" + config["STUUDIUM_USERNAME"].replace(" ", "+") + "&data%5BUser%5D%5Bpassword%5D=" + config["STUUDIUM_PASSWORD"]

    loginResponse = requests.post(config["STUUDIUM_BASE_URL"] + "/auth/?lang=et", headers=loginHeaders, data=loginPayload)

    # print(loginResponse.headers)
    sessionCookie = str() 

    for cookie in loginResponse.headers.get('set-cookie').split(' '):
        if "_stdmss=" in cookie:
            sessionCookie = cookie.strip(';')

    # print(sessionCookie)
    loginHeaders["cookie"] = sessionCookie
    del loginHeaders["content-type"]
    del loginHeaders["content-length"]

    loginHeaders["Sec-Fetch-Dest"] = "document"
    loginHeaders["Sec-Fetch-Mode"] = "navigate"
    loginHeaders["Sec-Fetch-User"] = "?1"
    loginHeaders["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"

    # print(loginHeaders)

    # We will be redirected if we just GET the Stuudium base URL, so we'll have to
    # get our Student ID from this redirect
    # redirectResponse = requests.get(config["STUUDIUM_BASE_URL"], headers=loginHeaders)

    # print(redirectResponse.status_code, redirectResponse.headers)
    # print(redirectResponse.text)

    # studentNumber = redirectResponse.headers["location"].split("/")[-1]

    # Finally request the grades page
    gradesResponse = requests.get(config["STUUDIUM_BASE_URL"] + "/grades/student/" + config["STUUDIUM_STUDENT_ID"], headers=loginHeaders)

    # Raw HTML from the response
    rawHTML = gradesResponse.text

    parser = GradePageParser()
    parser.grades = {}

    parser.feed(rawHTML)

    return parser.grades
