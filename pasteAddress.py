import pyautogui as ex
import clipboard as cb
import time
import copyAddress

#-153.106
#-400,106

def pasteAddress(addressList, buttonX,buttonY):
    textX = buttonX
    #textX = buttonX - 250
    textY = buttonY
    ex.moveTo(textX,textY,0.5)

    for a in addressList:
        cb.copy(a)    
        time.sleep(0.2)
        ex.mouseDown()
        time.sleep(0.1)
        ex.mouseUp()
        
        ex.hotkey('ctrl','a')
        ex.hotkey('ctrl','v')
        ex.hotkey('enter')
        print(a)
        break
    print("paste End")
 
 

    
def testMousePos ():
    try:
        while True:
            a = ex.position()
            print("mouse place:",a)
    except KeyboardInterrupt:
        pass

    print("TEST end")



if __name__ == "__main__":
    #testMousePos()
    
    copyAddress.copyAddress()
    aList = copyAddress.addressList

    pasteAddress(aList,-50, 70 )
    
    