import parseHTML
import TTWARD
import schedule
import time

currentState = dict()

# This function should be run in an interval
async def updateCycle() -> None:
    global currentState
    fetchedState = parseHTML.fetchGrades()
    for key in currentState.keys:
        print(currentState)
        print()
        print(fetchedState)
        if (currentState[key] != fetchedState[key]):
            TTWARD.appiArgoAnnabPeksa("Uus hinne aines " + key + ": " + fetchedState[key][0])
    currentState = fetchedState

def run() -> None:
    # TTWARD.run()
    global currentState
    currentState = parseHTML.fetchGrades()

    del currentState["Programmeerimine"][0]

    schedule.every(1).minutes.do(updateCycle)
    # print(parseHTML.fetchGrades())

    while True:
        schedule.run_pending()
        time.sleep(0.1)

# Entry point for this program
if __name__ == "__main__":
    run()