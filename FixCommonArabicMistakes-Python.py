# -*- coding: utf-8 -*-

"""
FCAM script (Fix Common Arabic Mistakes).
=========================================

 DESCRIPTION:
    Python Open/LibreOffice macro use Regex to fix common Arabic mistakes.

    What's it doing?
    - Removes any empty lines.
    - Removes Arabic Kashida (Tatweel "ـ").
    - Removes whitespaces after single WAW letter (و).
    - Removes whitespaces before Arabic punctuation (؛،.؟:!).
    - Removes whitespaces in parentheses  ... after "(" and before ")".
    - Removes any sequence of whitespaces and whitespaces at end of lines.
    - Replaces Latin comma (decimal separator) "," after Arabic words to Arabic comma "،".
    - Replaces Latin semicolon ";" after Arabic words to Arabic semicolon "؛".

 USING:
    1. Install.
      By default Open/LibreOffice supports Basic natively, and if you want to use python, you have to install an extra package.

      For Ubuntu:
      sudo apt-get install libreoffice-script-provider-python

      Then, copy the macro to scripts path.

      - Global to make it available for all users:
        /usr/lib/libreoffice/share/Scripts/python/

      - OR under your home:
        ~/.config/libreoffice/4/user/Scripts/python/

    2. Run.
     From the menu:
     Tools ▸ Macros ▸ Run Macro ▸ LibreOffice Macros ▸ FixCommonArabicMistakes-Python

 VERSION:
    v0.1 - November 2015.

 BY:
    Ahmed M. AbouZaid (http://tech.aabouzaid.com/) - Under GPL v2.0 or later.
"""
import uno

def FixCommonArabicMistakes():
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
    
    currentDoc = XSCRIPTCONTEXT.getDocument()
    findAndReplace = currentDoc.createReplaceDescriptor()
    findAndReplace.SearchCaseSensitive = True
    findAndReplace.SearchRegularExpression = True
    for replaceItem in replaceList:
        findAndReplace.SearchString = replaceItem
        findAndReplace.ReplaceString = replaceList[replaceItem]
        currentDoc.replaceAll(findAndReplace)
    return None
