# This global plugin was created for Georgi, following a request on the nvda-addons list.
# Author: Abdel <abdelkrim.bensaid@gmail.com>
# Inspired by the following solution, on the forum Stack Overflow:
# https://stackoverflow.com/questions/42047253/how-to-detect-current-keyboard-language-in-python

import globalPluginHandler
import ui
import locale 

class GlobalPlugin (globalPluginHandler.GlobalPlugin):

	def script_getCurKeyboardLanguage (self, gesture):
		# # Importing the ctypes module.
		import ctypes
		# Importing the languageHandler module.
		import languageHandler
		# Importing scriptHandler.
		import scriptHandler
		# Getting the user32 object. 
		user32 = ctypes.WinDLL('user32', use_last_error=True) 
		# Getting the handle of the foreground window. 
		curWindow = user32.GetForegroundWindow() 
		# Getting the threadId. 
		threadId = user32.GetWindowThreadProcessId(curWindow, 0) 
		# Getting the keyboard layout id. 
		klId = user32.GetKeyboardLayout(threadId) 
		# Extract language ID from klId. 
		lId = klId & (2**16 - 1) 
		# Getting the current keyboard language from the locale.windosw_locale dictionary. 
		curKbl = locale.windows_locale [lId]
		defaultKbl = locale.getdefaultlocale()[0]
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if repeatCount == 0:
			ui.message (languageHandler.getLanguageDescription(curKbl))
		else:
			ui.message (languageHandler.getLanguageDescription (defaultKbl))

	__gestures={
		"kb:nvda+f4":"getCurKeyboardLanguage"
	}