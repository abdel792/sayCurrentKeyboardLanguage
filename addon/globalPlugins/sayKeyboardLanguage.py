# -*- coding: UTF-8 -*-
# sayKeyboardLanguage.py
# Copyright 2017-2018 Abdelkrim Bensaïd, Noelia Ruiz-Martinez and other contributors, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Authors:
# Abdel <abdelkrim.bensaid@gmail.com>
# Noelia <nrm1977@gmail.com>
# This addon was created for Georgi, following a request on the nvda-addons mailing list.
# Inspired by the following solution, on the forum Stack Overflow:
# https://stackoverflow.com/questions/42047253/how-to-detect-current-keyboard-language-in-python

import globalPluginHandler
import ui
import locale
from scriptHandler import script
import versionInfo

# Category for the input gestures.
from globalCommands import SCRCAT_INPUT
from typing import Callable

# For translations.
import addonHandler
addonHandler.initTranslation()
_: Callable[[str], str]

# To ensure backward compatibility of speakOnDemand.
speakOnDemand = {"speakOnDemand": True} if versionInfo.version_year > 2023 else {}


class GlobalPlugin (globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_INPUT

	@script(
		# Translators: Message presented in input help mode.
		description=_("Gives the language of the keyboard in use. "
		              "If pressed twice, gives the default language of the system."),
		**speakOnDemand
	)
	def script_sayCurKeyboardLanguage(self, gesture):
		import winUser
		import scriptHandler
		import ctypes
		import languageHandler
		# Getting the handle of the foreground window.
		curWindow = winUser.getForegroundWindow()
		# Getting the threadID.
		threadID = winUser.getWindowThreadProcessID(curWindow)[1]
		# Getting the keyboard layout iD.
		klID = winUser.getKeyboardLayout(threadID)
		# Extract language ID from klID.
		lID = klID & (2**16 - 1)
		# Getting the current keyboard language description from ctypes.windll.kernel32.GetLocaleInfoW.
		# Some language IDs are not available in the local.windows_locale dictionary,
		# It is best to search their description directly in Windows itself
		buf = ctypes.create_unicode_buffer(1024)
		ctypes.windll.kernel32.GetLocaleInfoW(lID, (
			languageHandler.LOCALE_SLANGUAGE if hasattr(languageHandler, "LOCALE_SLANGUAGE")
			else languageHandler.LOCALE.SLANGUAGE),
			buf, 1024
			)
		desc = buf.value
		defaultOsl = locale.getdefaultlocale()[0]
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if repeatCount == 0:
			ui.message(desc)
		else:
			ui.message(languageHandler.getLanguageDescription(defaultOsl))
