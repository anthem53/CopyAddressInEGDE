import pyautogui as ex
import clipboard as cb

def testMousePos ():
    try:
        while True:
            a = ex.position()
            print("mouse place:",a)
    except KeyboardInterrupt:
        pass

    print("TEST end")


#testMousePos()
#cb.copy("test")
#cb.copy("")

a = "1234567"

b = a[-2:]
print(b)
