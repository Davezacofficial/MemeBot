# -*- coding: utf-8 -*-
"""
Created on Wed July 14th 11:17:00 2021

@author: Dave Zachariah

"""
import time
import aiohttp
import asyncio, requests

async def meme():
    async with aiohttp.ClientSession() as cs:
            async with cs.get('https://meme-api.herokuapp.com/gimme/dankmemes/') as r:
               res = await r.json()
               title = res['title']
               image = res['url']
               ups = res['ups']
            # Store your password in 'TOKEN.txt'
            TOKEN = open("TOKEN.txt", "r").read()

            url = 'https://api.telegram.org/bot'+TOKEN+'/sendMessage?chat_id=-1001535046778&text={}'.format(f'{title} \nUpvotes: {ups}👍\nImage Credits: DankMemes\n{image}')
        
            requests.get(url)
            print(f'Title: {title}\nUpvotes: {ups}')
            # Frequency of posting memes[ in seconds ]
            time.sleep(60) 
                

while True:
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(meme())