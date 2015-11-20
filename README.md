FCAM script (Fix Common Arabic Mistakes).
=========================================

Open/LibreOffice macros (Basic and Python) use Regex to fix common Arabic mistakes. For now both of Basic and Python versions do the same thing, but I will go with Python from now on.

What's it doing?
-------------------
- Removes any empty lines.
- Removes Arabic Kashida (Tatweel "ـ").
- Removes whitespaces after single WAW letter (و).
- Removes whitespaces before Arabic punctuation (؛،.؟:!).
- Removes whitespaces in parentheses  ... after "(" and before ")".
- Removes any sequence of whitespaces and whitespaces at end of lines.
- Replaces Latin comma (decimal separator) "," after Arabic words to Arabic comma "،".
- Replaces Latin semicolon ";" after Arabic words to Arabic semicolon "؛".

Python version.
-------------------
By default Open/LibreOffice supports Basic natively, and if you want to use python, you have to install an extra package.

For Ubuntu:
```
sudo apt-get install libreoffice-script-provider-python
```

### Install
Copy the macro to scripts path.

Global path to make it available for all users:
```
/usr/lib/libreoffice/share/Scripts/python/
```

**OR** under your home:
```
~/.config/libreoffice/4/user/Scripts/python/
```

### Run
From the menu:
```
Tools ▸ Macros ▸ Run Macro ▸ LibreOffice Macros ▸ FixCommonArabicMistakes-Python
```

Standalone version.
-------------------
I made a Standalone version of script too, it useful with bulk files or so, it maybe not that cool, but maybe help someone :-)

This script not works as a macro but will start Opne/LibreOffice on a specific local port and connect to it, then open the file passed to it, and fix common mistakes. It will not save the file automatically, but it will wait you to do save as a final action.

### Run:
```
./FixCommonArabicMistakes-Standalone.py file_name.odt
```

