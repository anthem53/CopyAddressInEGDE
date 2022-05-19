import pyautogui as ex
import clipboard as cb
import time

# 위치 65,7
# 주소창 위치 360 50

addressList = []
firstTab = None
delayTime = 0



def clickAddressAndCopy():
    ex.moveTo(360,50)
    ex.click()
    ex.hotkey('ctrl','a')
    ex.hotkey('ctrl','c')
    address = cb.paste()
    return address

def CheckAndAppend(tab):
    if tab[-2:] == "#1":
        addressList.append(tab)
    else:
        pass

def selectFirstTab():
    #초기 
    ex.moveTo(60,15)
    ex.click()
    time.sleep(delayTime)

    firstTab = clickAddressAndCopy()
    addressList.append(firstTab)
    #CheckAndAppend(firstTab)
    print("firstTab : ", (firstTab))

def selectNextTab():
    ex.hotkey('ctrl','tab')
    ex.moveTo(360,50)
    time.sleep(delayTime)

    currentTab = clickAddressAndCopy()
    addressList.append(currentTab)
    #CheckAndAppend(currentTab)
    print("current Tab :", (currentTab))

    return currentTab
    
def copyAddress ():
    global addressList

    addressList = []
    old_clipboard = cb.paste()

    selectFirstTab()
    time.sleep(0.1)
    
    i = 0
    count  = 0
    while True : 
        currentTab = selectNextTab()
        if currentTab == addressList[0]:
            del addressList[-1]
            break

        
    print("func finish")
    return addressList

def testST():
    ex.moveTo(60,15)
    ex.click()
    
    time.sleep(0.1)


def testMousePos ():
    try:
        while True:
            a = ex.position()
            print("mouse place:",a)
    except KeyboardInterrupt:
        pass

    print("TEST end")


if __name__ == "__main__":
    addressList = copyAddress()
    for s in addressList:
        print("address : ", s)
    #testST()
    #testMousePos()

