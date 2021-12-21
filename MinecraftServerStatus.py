from mcstatus import MinecraftServer
from PIL import Image 
import PIL 
import base64
from PIL import Image
from io import BytesIO
import re
server = MinecraftServer.lookup("server:25565")
status = server.status()

if status.favicon:
  print(status.favicon.split()[0])
  print(re.search(r",.*(=)", status.favicon))
  #im = Image.open(BytesIO(base64.b64decode("""""")))
  #im.save('image.png', 'PNG')