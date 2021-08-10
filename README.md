# MemeBots 🤖

## MemeBot for Instagram
This program relies on **instabot** library which is neither affiliated or sponsored by Instagram or Facebook therefore **use it at your own risk.**
And please disable `two-factor authentication` before running this programm otherwise you will run it some errors.

### Working ⚙
It works by finding the **most upvoted** meme on the [dankmemes](https://www.reddit.com/r/dankmemes/) page, downloads it and then posts it on your page along with defined captions and random hashtags. Since *instabot* can only post files with the `.jpg` or `.jpeg` extensions and a square image with the dimensions of `1080x1080` therefore images the program utilizes **Pillow** to convert and resize the images into the desired format and thereafter posts it. Since it's an unoffical API, it works by making requests as a phone 📱 by altering the headers with which it makes the requests.

### Steps 

- Replace `pythonmemebot` with the username of IG account you want to use and put your password in *password.txt*
```py
bot = Bot()
bot.login (username = "pythonmemebot", password = PASS)
```
- You can alter the hashtags used along with your post
```py
async def get_post_meme():
    tags_for_post = ["#meme", "#memes", "#funny", "#dankmemes", "#memesdaily", "#funnymemes", "#lol", "#follow", "#humor", "#like", "#dank", "#love", "#instagram", "#memepage", "#dankmeme", "#tiktok", "#comedy", "#lmao", "#fun", "#anime", "#lol", "#dailymemes", "#edgymemes", "#offensivememes", "#memestagram", "#bhfyp", "#instagood", "#funnymeme", "#memer",
                     "#reddit", "#shitpost", "#funnyvideos", "#explorepage", "#followforfollowback", "#jokes", "#viral", "#haha", "#likeforlikes", "#art", "#f", "#youtube", "#memesespa" "#memeita", "#explore", "#gaming", "#covid", "#minecraft", "#likes", "#memez", "#laugh", "#followme", "#edgy", "#trending", "#life", "#music", "#india", "#dankmemesdaily", 
                     "#gamer", "#cute"]
```
- You can also replace the caption used along with your posts:
```py
bot.upload_photo('meme.jpg',caption = f'{title}' + f"\nUpvotes: {ups} 👍" + "\nImage Credits: Dank Memes 📷" "\n \n \n" + tagstring)
```
The above line would give you this caption 👇
```
He's too smart to be kept alive
Upvotes: 69361 👍
Image Credits: Dank Memes 📷
```

- You can also change the frequency at the bot post memes by altering the time within this parenthesis [in seconds ⌛]
```py
 time.sleep(1800)
```

- Voila! And you're good to go, this is what the final results looks like:

![finalresult](https://user-images.githubusercontent.com/83908831/128918920-2b6d2afe-fa4c-4d17-9019-dbf5e2446607.jpg)


