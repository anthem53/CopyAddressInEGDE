
import tkinter
from tkinter import scrolledtext
from tkinter.constants import COMMAND, S
from tkinter import *
from typing import Text
from threading import Thread
from timer import RepeatedTimer
from time import sleep
import copyAddress
import pyautogui
import clipboard as cb
import os
import subprocess

# GUI part

UI_LIST = None

def setAddress():
    list_file = []                                          #파일 목록 담을 리스트 생성
    files = tkinter.filedialog.askopenfilenames(initialdir="/",\
                 title = "파일을 선택 해 주세요",\
                   filetypes =(("EXE file","*.exe"), ("txt files","*.txt"),("all files","*.*")))
    #files 변수에 선택 파일 경로 넣기

    if files == '':
        tkinter.messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력
        return False
    else: 
        print(files, type(files),type(files[0]))    #files 리스트 값 출
        print(os.path.dirname(os.path.realpath(__file__)), type(os.path.dirname(os.path.realpath(__file__))))
        targetFile= files[0]
        currentDir = os.path.dirname(os.path.realpath(__file__))
        optionFile = currentDir + "/option.ini"
        
        f = open(optionFile, 'w')
        f.write(targetFile)

        f.close()

        return True


def openDownloader2():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    optionFile = currentDir + "/option.ini"
    if os.path.isfile(optionFile) == True:
        f = open(optionFile,'r')
        targetFile = f.readline()
        print('"'+targetFile+'"')
        os.startfile(targetFile)
        #os.system(targetFile)

        return True
    else:
        tkinter.messagebox.showwarning("경고", "아무런 파일이 세팅되어있지 않습니다.")    #파일 선택 안했을 때 메세지 출력
        return False
def openDownloader():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    optionFile = currentDir + "/option.ini"
    if os.path.isfile(optionFile) == True:
        f = open(optionFile,'r')
        targetFile = f.readline()
        print('"'+targetFile+'"')
        subprocess.Popen([targetFile])
        #os.system(targetFile)

        return True
    else:
        tkinter.messagebox.showwarning("경고", "아무런 파일이 세팅되어있지 않습니다.")    #파일 선택 안했을 때 메세지 출력
        return False

def openDownloadFolder():
    pass

def addMenu(root,UI_LIST):
    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    #filemenu.add_command(label="Exit",command=on_closing)

    menubar.add_cascade(label="run downloader", command = lambda: openDownloader())
    menubar.add_cascade(label="open download folder", command = lambda: openDownloader2())
    menubar.add_cascade(label="setting downloader", command = lambda: setAddress())
    
    #menubar.add_cascade(label="edit correct list", command = lambda: editCorrectList(UI_LIST))
    root.config(menu=menubar)
    return [(filemenu,"fileMenu")]
    
def getUIWithName(UI_LIST,UI_name):
    for (elem,name) in UI_LIST:
        if name == UI_name:
            return elem

    print("Wrong UI_name input. Check your code. Wrong UI_NAME : [",UI_name,"]")
    return None

def printAddress ():
    for s in copyAddress.addressList:
        print(s)

def nextAddress() :
    AList = copyAddress.addressList

    is_success= False
    
    if (len(AList) > 0):
        if(AList[0][-2:] == "#1"):
            cb.copy(AList[0])
            del AList[0]
            label = getUIWithName(UI_LIST, "restAddressNumLabel")
            label['text'] = "남은 작업량 : %d" % len(AList)
            
        else:
            del AList[0]
            nextAddress()
        
    else:
        cb.copy("")
        label = getUIWithName(UI_LIST, "restAddressNumLabel")
        label['text'] = "남은 작업량 : %d" % len(AList)
        
def customCopyAddress():
    copyAddress.copyAddress()
    label = getUIWithName(UI_LIST, "restAddressNumLabel")
    label['text'] = "남은 작업량 : %d" % len(copyAddress.addressList)
    pass

def addButtons(root):
    buttonFrame = tkinter.Frame(root)
    buttonFrame.pack(side="left")

    h = 5
    w = h * 3
    font_size = 15

    nextAddressButton= tkinter.Button(buttonFrame, width=w,height= h,bg='sky blue', repeatdelay=1000, repeatinterval=100, font=("Helvetica", font_size))
    nextAddressButton.config(text= "next Address", command= nextAddress)
    nextAddressButton.pack(side="left",padx=50, pady=25)


    copyAddressButton = tkinter.Button(buttonFrame, width=w,height= h,bg='sky blue', repeatdelay=1000, repeatinterval=100, font=("Helvetica", font_size))
    copyAddressButton.config(text= "Copy address", command= customCopyAddress)
    copyAddressButton.pack(side="left",padx=50, pady=25)



    return [(copyAddressButton,"copyAddressButton"),(nextAddressButton,"nextAddressButton")]

def addNumberInputBox(root):
    textFrame = tkinter.Frame(root)
    textFrame.pack(side="top")

    # inputFrame 
    inputFrame = tkinter.Frame(textFrame)
    inputFrame.pack(side="top")

    xInput = tkinter.Text(inputFrame,height= 1,width= 10,pady=10,font=("Helvetica", 32) )
    xInput.pack(side="left")

    yInput = tkinter.Text(inputFrame,height= 1,width= 10,pady=10,font=("Helvetica", 32) )
    yInput.pack(side="left")

    # show current mouse place text
    mousePlaceFrame = tkinter.Frame(textFrame)
    mousePlaceFrame.pack(side="top")


    currentMouseX = tkinter.Text(mousePlaceFrame,height= 1,width= 10, pady=10,bg="steel blue",state=DISABLED,font=("Helvetica", 32) )
    currentMouseX.pack(side="left")

    currentMouseY = tkinter.Text(mousePlaceFrame,height= 1,width= 10,pady=10,bg="steel blue",state=DISABLED,font=("Helvetica", 32))
    currentMouseY.pack(side="left")

    return [(xInput,"xInput"),(yInput,"yInput"),(currentMouseX,"currentMouseX"),(currentMouseY,"currentMouseY")]   

def addrestAddressNumLabel(root):
    
    restAddressNumLabel = tkinter.Label(root,text = "남은 작업량 : 0 ")
    restAddressNumLabel.pack(side="top")
    return [(restAddressNumLabel,"restAddressNumLabel")]

def hello(name):
    print ("Hello %s!" % name)

def getMousePlace(UI_LIST):
    currentMouseX = getUIWithName(UI_LIST,"currentMouseX")
    currentMouseY = getUIWithName(UI_LIST,"currentMouseY")

    cPos = pyautogui.position()
    currentMouseX.config(state="normal")
    currentMouseX.delete(1.0,"end")
    currentMouseX.insert(1.0,str(cPos.x))
    
    currentMouseY.config(state="normal")
    currentMouseY.delete(1.0,"end")
    currentMouseY.insert(1.0,str(cPos.y))
    currentMouseX.config(state="disabled")
    currentMouseY.config(state="disabled")

    #currentMouseX.config(text = str(cPos.x))
    #currentMouseY.config(text = str(cPos.y))

if __name__ == "__main__":
    
    root = tkinter.Tk()
    root.title("Copy Address")
    root.geometry("550x250")


    UI_LIST = []
    #UI_LIST = UI_LIST + addNumberInputBox(root)
    UI_LIST = UI_LIST + addrestAddressNumLabel(root)
    UI_LIST = UI_LIST + addButtons(root)
    UI_LIST = UI_LIST + addMenu(root,UI_LIST)
    
    print(UI_LIST)


    root.mainloop()

    print("TEST END")
    exit(0)