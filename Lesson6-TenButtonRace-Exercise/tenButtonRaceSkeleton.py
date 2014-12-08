#! /usr/bin/evn python

import wx #import the graphical library
import time #import the time module
import random

class TenButtonFrame(wx.Frame):
	
	
	
	def __init__(self, parent):
		self.f = open("score.txt", "r+")
		self.record = self.f.readlines()
		
		self.number = int(raw_input("How many buttons do you want? Your final score \
would be recorded as the average time of each button."))
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race", size = (900, 600), pos = (25, 25))
		
		self.panel = wx.Panel(self)  #Make a new Panel
		
		self.buttons = []
		self.highestScore = wx.StaticText(self.panel, label = "This is a button clicking game.\
\nAll time high score: {}s, by {}.\nIf you win, you can enter your name in the terminal after clicking the last button.".format((self.record[0])[:4],self.record[1]), pos = (300,325))
		self.btnStart = wx.Button(self.panel, label="Start", pos=(425, 300)) #Make the start button
		
		for i in range(10):
			a = random.randint(100, 800)
			b = random.randint(100, 500)
			
			self.currentbtn = wx.Button(self.panel, label="Button " + str(i+1), pos=(a, b))
			self.currentbtn.Show(False)
			self.buttons.append(self.currentbtn)
			self.currentbtn.Bind(wx.EVT_BUTTON, self.OnAnyButton)
		
		self.btnStart.Bind(wx.EVT_BUTTON, self.OnClickStart)
		
		
		
	def OnClickStart(self, e):       # Event handler for the start button
		self.btnStart.Show(False)
		self.buttons[0].Show(True)
		self.startTime = time.time()
		self.highestScore.Show(False)
		
	
	def OnAnyButton(self, e):                      #Other event handlers
		self.clickedButton = e.GetEventObject()
		self.clickedButton.Show(False)
		for i in range(self.number-1):			
			if self.clickedButton == self.buttons[i]:
				self.buttons[i+1].Show(True)
		if self.clickedButton == self.buttons[self.number-1]:
			finalTime = time.time()
			timePass = finalTime - self.startTime
			self.time = wx.StaticText(self.panel, label = "Great job! Your final time is "\
			 + str(round(timePass, 2)) + "s.", pos = (100,100))
			averageTime = timePass / self.number
			self.averageTime = wx.StaticText(self.panel, label = "Your average time is " \
			+ str(round(averageTime, 2))  + "s per bottom", pos = (100,115))
			
			if averageTime <= self.record[0]:
				
				self.winner = wx.StaticText(self.panel, label = "And congratulation! You are the best score! Your name is already recorded.", pos = (100,130))
				
				self.f.seek(0)
				self.f.truncate()
				self.f.write(str(round(averageTime, 2)) + "\n")
				
				win = raw_input("Please enter your name:")
				self.f.write(win)

'''
		clickedIndex = buttons.index(clickedButton)
		buttons[clickedIndex].Show(False)
		buttons[clickedIndex+1].Show(True)
'''
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()