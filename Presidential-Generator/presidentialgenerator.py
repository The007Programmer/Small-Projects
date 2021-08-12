from WhiteHouse import p, vp
import random
from utils import jsonloader

while True:
    prezlist=["Gamefan586", "Epic Gamer"]
    randomprez=input("Keyword to start > ")
    secret_file = jsonloader.read_json("prezsecrets")
    keyword=secret_file["PrezGenTOKEN"]
    if randomprez==keyword:
        print("Starting Generator...")
        print(f"The President is {random.choice(prezlist)}")
        break
    else:
        print(f"{randomprez} is the incorrect Starting Key...")