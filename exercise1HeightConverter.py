#!/usr/bin/env python
import wx

class heightConverter(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Height Converter", size = (400,200))
		
		self.panel = wx.Panel(self)
		
		self.prompt = wx.StaticText(self.panel, label="Please enter your height:", pos=(40, 10))
		self.feetTxt = wx.StaticText(self.panel, label="feet", pos=(243, 10))
		self.inches = wx.StaticText(self.panel, label="inches", pos=(315, 10))

		self.response = wx.StaticText(self.panel, pos=(40, 100))
		
		
		self.feet = wx.TextCtrl(self.panel, pos = (200, 10), size = (40,20))
		self.inches = wx.TextCtrl(self.panel, pos = (273, 10), size = (40,20))
		self.cbRound = wx.CheckBox(self.panel, label='Round off the result to integer.', pos=(40, 30))
		self.cbRound.SetValue(False)

		self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(150, 50))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmitHeight)
		
		self.Centre()
		self.Show()
		
		
	def OnSubmitHeight(self, e):
		
		feet = self.feet.GetValue()
		inches = self.inches.GetValue()

		try:
			feet = int(feet)
			inches = float(inches)
			centimeter = 30.48 * feet + 2.54 * inches
			isChecked = self.cbRound.GetValue()
			if isChecked:
				centimeter = int(centimeter)
			self.response.SetLabel("Your height is " + str(centimeter) + "cm.")

		except ValueError:
			wx.MessageBox("You need to enter a integer for \"feet\" and a real number for \"inches\".", "Info", wx.OK | wx.CANCEL)

		


app = wx.App(False)

# Create a regular old wx.Frame
frame = heightConverter(None)

# Show the frame


# Make the app listen for clicks and other events
app.MainLoop()