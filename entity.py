import desc
import imageloader

isContainer = False
EntityID = ['chest']
CollidedEntityID = ''
#------------------------------------
# Formating For Items
#ID,Name,Graphic,Desc,DescImage,Type,xpos,ypos
Entity = {
  EntityID[0]:{'Name':"Chest",'Graphic':'ê','Desc':desc.descLoad("ent_chest"),"DescImage":imageloader.images("desc_chest") ,'Type':"container",'Xpos':7000,'Ypos':7000}
  }
#------------------------------------
#Colliding Tiles AKA walls
#---------------------------------
TileLength = 0
