import parseHTML
# import TTWARD
import schedule
import time
import threading
import asyncio
import subprocess

currentState = dict()


# This function should be run in an interval
def updateCycle() -> None:
    global currentState
    fetchedState = parseHTML.fetchGrades()
    # print(currentState)
    # print()
    print(fetchedState)
    for key in currentState.keys():
        if (currentState[key] != fetchedState[key]):

            # For some f-ing reason the Discord bot won't run correctly unless
            # we do this... 
            file = open("./src/gradeText.txt", "w", encoding="UTF-8")
            file.write("Uus hinne aines " + key + ": " + fetchedState[key][0])
            file.close()

            subprocess.run(["python", "./src/TTWARD.py"])


    currentState = fetchedState

def run() -> None:
    global currentState
    currentState = parseHTML.fetchGrades()
    # print(currentState)

    # TTWARD()

    # TTWARD.sendMessage("What is a ni?")
    # discordThread = threading.Thread(target=TTWARD.sendMessage, args=["what is a n?"])
    # discordThread.start()

    del currentState["Ajalugu"][0]

    schedule.every(1).minutes.do(updateCycle)
    # print(parseHTML.fetchGrades())

    while True:
        schedule.run_pending()
        time.sleep(0.1)

# Entry point for this program
if __name__ == "__main__":
    run()