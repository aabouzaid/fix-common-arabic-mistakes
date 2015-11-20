REM  *****  BASIC  *****

Sub FixCommonArabicMistakes
    oDoc = thisComponent
    aFind = Array("(\p{script=arabic}\W?)([ ]?;)", "(\p{script=arabic}\W?)([ ]?,)", "\([ ]+", "[ ]+\)", "^[\ ]*$", "^[\ ]*", "[\ ]*$", "[ ]+", " :", " ؛", " ،", " \.", " !", " ؟", " و ", "^و ", "ـ")
    aReplace = Array("$1؛", "$1،", "(", ")", "", "", "", " ", ":", "؛", "،", ".", "!", "؟", " و", "و", "")
    aRayCount = 0
    FandR = oDoc.createReplaceDescriptor
    FandR.SearchCaseSensitive = true
    FandR.SearchRegularExpression = true
    While aRayCount <= uBound(aFind)
        FandR.setSearchString(aFind(aRayCount))
        FandR.setReplaceString(aReplace(aRayCount))
        aRayCount = aRayCount + 1
        oDoc.ReplaceAll(FandR)
    Wend
End Sub
