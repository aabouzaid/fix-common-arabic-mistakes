#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Common Arabic Mistakes - Standalone version.
=========================================

 DESCRIPTION:
    Standalone version of Python Open/LibreOffice macro use Regex to fix common Arabic mistakes.
    This version useful with bulk files or so, it maybe not that cool, but it maybe help someone :-)

    This script not works as a macro but will connect to Opne/LibreOffice and open file passed to it, and fix common mistakes.
    It will not save the file automatically, but it will wait you to do save as a final action.

 USING:
    ./FixCommonArabicMistakes-Standalone.py file_name.odt

 MORE:
    https://github.com/AAbouZaid/fix-common-arabic-mistakes

 BY:
    Ahmed M. AbouZaid (http://tech.aabouzaid.com/) - Under GPL v2.0 or later.
"""
import re
import os
import sys
import uno
import time
import unohelper

if len(sys.argv) == 1:
   print("Please write odt file name/path.")
   sys.exit(1)

file_path = sys.argv[1]
os.popen('soffice --accept="socket,host=localhost,port=2015;urp;StarOffice.ServiceManager" --norestore  --nologo  &')
time.sleep(3)
localcontext = uno.getComponentContext()
resolver = localcontext.getServiceManager().createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localcontext)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.getServiceManager().createInstanceWithContext("com.sun.star.frame.Desktop", context)
url = unohelper.systemPathToFileUrl(os.path.abspath(file_path))

currentDoc = desktop.loadComponentFromURL(url, "_blank", 0, () )
findAndReplace = currentDoc.createReplaceDescriptor()
findAndReplace.SearchCaseSensitive = True
findAndReplace.SearchRegularExpression = True

replaceList = {
    "(\p{script=arabic}\W?)([ ]?;)": "$1؛",
    "(\p{script=arabic}\W?)([ ]?,)": "$1،",
    "\([ ]+": "(",
    "[ ]+\)": ")",
    "^[\ ]*$": "",
    "^[\ ]*": "",
    "[\ ]*$": "",
    "[ ]+": " ",
    " :": ":",
    " ؛": "؛",
    " ،": "،",
    " \.": ".",
    " !": "!",
    " ؟": "؟",
    " و ": " و",
    "^و ": "و",
    "ـ": ""
}

for replaceItem in replaceList:
    findAndReplace.SearchString = replaceItem
    findAndReplace.ReplaceString = replaceList[replaceItem]
    currentDoc.replaceAll(findAndReplace)
