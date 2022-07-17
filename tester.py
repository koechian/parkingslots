import eel

eel.init("frontend")


@eel.expose
def tester(param):
    print("Hello World", param)

    return "Hello Dunia"


eel.start("direction.html", size=(1920, 1080))
