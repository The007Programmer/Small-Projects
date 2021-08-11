from WhiteHouse import p, vp
import random

while True:
    prezlist=["Gamefan586", "Epic Gamer"]
    randomprez=input("Keyword to start > ")
    if randomprez=="投票4プレズを開始":
        print("Starting Generator...")
        print(f"The President is {random.choice(prezlist)}")
    else:
        print(f"{randomprez} is the incorrect Starting Key...")