import wget, pathlib
import time
from instabot import Bot
import random, os
import shutil, asyncio, aiohttp
from PIL import Image

isExist = os.path.exists("config")
if isExist:
    shutil.rmtree("config", ignore_errors=True)

#instagram login
bot = Bot()
bot.login (username = "pythonmemebot", password = "Hacker4ever@0112358")

async def get_post_meme():
    tags_for_post = ["#meme", "#memes", "#funny", "#dankmemes", "#memesdaily", "#funnymemes", "#lol", "#follow", "#humor", "#like", "#dank", "#love", "#instagram", "#memepage", "#dankmeme", "#tiktok", "#comedy", "#lmao", "#fun", "#anime", "#lol", "#dailymemes", "#edgymemes", "#offensivememes", "#memestagram", "#bhfyp", "#instagood", "#funnymeme", "#memer",
                     "#reddit", "#shitpost", "#funnyvideos", "#explorepage", "#followforfollowback", "#jokes", "#viral", "#haha", "#likeforlikes", "#art", "#f", "#youtube", "#memesespa" "#memeita", "#explore", "#gaming", "#covid", "#minecraft", "#likes", "#memez", "#laugh", "#followme", "#edgy", "#trending", "#life", "#music", "#india", "#dankmemesdaily", 
                     "#gamer", "#cute"]

    async with aiohttp.ClientSession() as cs:
            async with cs.get('https://meme-api.herokuapp.com/gimme/memes/50') as r:
               res = await r.json()
               final = {}
               last = {}
               end = {}
            for i in enumerate(res["memes"]):
                final[res["memes"][i[0]]["postLink"]] = res["memes"][i[0]]["ups"]
                last[res["memes"][i[0]]["url"]] = res["memes"][i[0]]["ups"]
                end[res["memes"][i[0]]["title"]] = res["memes"][i[0]]["ups"]
                link = [k for k, v in final.items() if v == max(final.values())]
                image = [l for l, h in last.items() if h == max(last.values())] 
                title = [a for a, b in end.items() if b == max(end.values())] 
            link = link[0]
            image = image[0]
            title = title[0]
            ups = final[link]
            
    file_ext=pathlib.Path(image).suffix
    for i in range (1,50):
        tagstring = ""
        for i in range(15):
            rand_tag = random.choice(tags_for_post)
            tagstring = tagstring + rand_tag + " "           
    wget.download(image,'meme'+file_ext)
    try:
        im = Image.open("meme"+file_ext)  
        newsize = (1080, 1080) 
        im = im.resize(newsize) 
        im.save('meme'+file_ext)
    except:
        print("ERROR | Couldn't Resize Image [Unsupported Format]")
    try:
        if file_ext == 'png':
            img = Image.open('meme'+file_ext)
            img.save(f'meme.jpg')
            bot.upload_photo('meme.jpg',caption = f'{title}' + f"\nUpvotes: {ups} 👍" + "\nImage Credits: Dank Memes 📷" "\n \n \n" + tagstring)
        else:
            bot.upload_photo(f'meme{file_ext}',caption = f'{title}' + f"\nUpvotes: {ups} 👍" + "\nImage Credits: Dank Memes 📷" "\n \n \n" + tagstring)
    
    except:
        print("ERROR | Couldn't Resize Image [Unsupported Format]")

    time.sleep(15)
    if os.path.exists('meme'+file_ext):
        os.remove ('meme'+file_ext)
    time.sleep(1800)
       
while True:
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(get_post_meme())

