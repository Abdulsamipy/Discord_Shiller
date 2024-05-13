import time
import discum
import re
import threading
import os
from discum.utils.embed import Embedder
import schedule


message = """
** **
:t_bolt::Crown:  __**THE TATTOO SHOP**__ **│** __**NFT**__  :Crown::t_bolt:

 
:t_redalert:  **We are a verified community of people who  :fbheart: TATTOOS & ART!**
 
:TTS_Sparkle: The collaboration of 6 Tattoo Artists who are legends in the worldwide tattoo industry
:TTS_Sparkle: The community is centered around TATTOOS, ART, and the quest for the HOLY GRAIL!
 
 
:t_pin: **Eye-catching NFT collection with each NFT having rarities from all 6 artists.** __Over :Giveawayadnimated: **+250 **rarities!__
 
**Holder Perks: **
:TTS_BulletArrow2_Right: Be entered to win a **1 of 6 DREAM** tattoo giveaway!
:TTS_BulletArrow2_Right: Access to **__THE TATTOO SHOP__** to have their avatar tattooed by the community at `tattooawards.com`
:TTS_BulletArrow2_Right: Awarded access to private channels!
 
:TTS_BulletArrowRight: **__Fully doxxed management team, dev team, abs Artists__**! :TTS_BulletArrowLeft:
 
```
 
```
` > ` Line Gif: https://tenor.com/view/rainbow-color-line-colorful-change-color-gif-17422882
` > ` Banner: https://media.discordapp.net/attachments/868889879218622484/959446736324149278/Join_TTS_Discord.png
` > ` **Invite**: https://discord.gg/dEsbWGJw2T

"""




def dm(tokens, url, username):

    bot= discum.Client(token=tokens, log={"console": True,"file": False })
    for u in url:
        channel_id = re.findall("https+?:+?//+?discord\.com/channels/+?\d+/+?(\d+)", str(u))
        c_id = channel_id[0]
        messa = (bot.sendMessage(f"{c_id}", message))
        print(messa)
        if "<Response [200]>" in str(messa):
            print(str(threading.current_thread().name) + f" - {username} - Message sent to: " + str(u))
            time.sleep(20)

def main():
    path = "Discord bots\\Shiller\\Shilling_Channels"
    files = os.listdir(path)


    for file in files:
        with open(path+"/" + file, 'r') as f:
            url = f.readlines()
        login = re.findall('([\s\S]+?)\.txt+?', str(file))

        login_split=str(login[0]).split('-')
        username = login_split[0].strip()
        token = login_split[1].strip()
        print(username, token)
        dm(token, url, username, )
        # th = threading.Thread(target=dm, args=(tokens[0], url, username[0], tokens[0]))
        # th.start()

main()


# schedule.every(5).hours.do(main)

# while True:
#     schedule.run_pending()
    

