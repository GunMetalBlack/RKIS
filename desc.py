import main
descNames = []
descFile =[]

def descLoad(name):
    if name in (descNames):
      fileIndex = descNames.index(name)
    else:
      main.logging.error("NO DESC")
    return descFile[fileIndex]

descFile.append("A dark oak chest filled with various items.")
descNames.append("ent_chest")


    