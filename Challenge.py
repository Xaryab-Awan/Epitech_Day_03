def occurences(text):
    count=0
    text=text.lower()
    count+=text.count("cat")
    count+=text.count("garden")
    count+=text.count("mice")
    count+=text.count("tac")
    count+=text.count("nedrga")
    count+=text.count("ecim")
    return count
print(occurences("the CataCat attaCk a Cat"))
print(occurences("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))
