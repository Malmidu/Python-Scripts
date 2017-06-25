from Tkinter import *
import platform
import os

CompTypes = ['RSCB', 'RTCB', 'SCCB', 'SWCB01', 'SWCB02', 'SWCB03', 'SRX', 'Broadband', 'VSAT']
def makeWindow():
	global storeNum
	global compType
	global ResponseBox
	global ResponseLines 
	ResponseLines = [' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	win = Tk()
	
	textsFrame = Frame(win)
	textsFrame.pack()
	Label(textsFrame, text="Store Number").grid(row=0, column=0, sticky=W)
	storeNum = StringVar()
	storeText = Entry(textsFrame, textvariable=storeNum)
	storeText.grid(row=0, column=1, sticky=W)
	# Label(textsFrame, text="Comp").grid(row=1, column=0, sticky=W)
	# compType = StringVar(textsFrame)
	# compType.set("Rest")
	
	# compText = OptionMenu(textsFrame, compType, "Rest", "Ret", "SCCB", "SWCB01", "SWCB02", "SWCB03", "All")
	# compText.grid(row=1, column=1, sticky=W)
	
	bFrame = Frame(win)
	bFrame.pack()
	b1 = Button(bFrame, text = "Ping", command=ping)
	b2 = Button(bFrame, text ="Quit", command=exit)
	b3 = Button(bFrame, text ="Clear", command=reset)
	b1.pack(side=LEFT)
	b3.pack(side=LEFT)
	b2.pack(side=LEFT)
	
	mFrame = Frame(win)
	mFrame.pack()
	ResponseBox = Message(mFrame, text=(ResponseLines[0] + '\n' + ResponseLines[1] + '\n' + ResponseLines[2] + '\n' + ResponseLines[3] + '\n' + ResponseLines[4] + '\n' + ResponseLines[5] + '\n' + ResponseLines[6] + '\n' + ResponseLines[7] + '\n' + ResponseLines[8] + '\n' + ResponseLines[9]))
	ResponseBox.pack()

	
	

	
	return win
	
def ProcessNumber(store):
	if len(store) == 1:
		processedStore = "00"+store
		return processedStore
	elif len(store) == 2:
		processedStpre == "0"+store
		return processedStore
	else:
		return store
		
def reset():
	ResponseBox.configure(text=' ')
def determineHost(comp, store):
	
	if comp == "RSCB":
		host = "rscb0"+store+".crackerbarrel.com"
		return host
	elif comp == "RTCB":
		host = "rtcb0"+store+".crackerbarrel.com"
		return host
	elif comp == "SCCB":
		host = "sccb0"+store+".crackerbarrel.com"
		return host
	elif comp == "SWCB01":
		host = "swcb010"+store+".crackerbarrel.com"
		return host
	elif comp == "SWCB03":
		host = "swcb030"+store+".crackerbarrel.com"
		return host
	elif comp == "SWCB02":
		host = "swcb020"+store+".crackerbarrel.com"
		return host
	elif comp == "SRX":
		host = "srx0"+store+".crackerbarrel.com"
		return host
	elif comp == "Broadband":
		host = "sccb0"+store+".bb.crackerbarrel.com"
		return host
	elif comp == "VSAT":
		host = "sccb0"+store+".vsat.crackerbarrel.com"
		return host
	elif comp == "All":
		host = "All"
		return host

def pingResponse(host):
	
	paramaters = "-n 1 " if platform.system().lower()=="windows" else "-c 1"
	
	return os.system('ping '+paramaters+' '+host)
def ping():
	global storeNum
	global compType
	global CompTypes
	global ResponseLines
	x = 1
	store = ProcessNumber(storeNum.get())
	ResponseLines[0] = "Store Number: " + store
	
	for i in CompTypes:
		print i
		host = determineHost(i, store)
		print host
		hostResponse = pingResponse(host)
		if hostResponse == 0:
			ResponseLines[x] = i +":     Response: Up"
		else:
			ResponseLines[x] = i +":     Response: Down"
		x += 1
	ResponseBox.configure(text=(ResponseLines[0] + '\n' + ResponseLines[1] + '\n' + ResponseLines[2] + '\n' + ResponseLines[3] + '\n' + ResponseLines[4] + '\n' + ResponseLines[5] + '\n' + ResponseLines[6] + '\n' + ResponseLines[7] + '\n' + ResponseLines[8] + '\n' + ResponseLines[9]))
		
		
win = makeWindow()	
	
win.mainloop()	
