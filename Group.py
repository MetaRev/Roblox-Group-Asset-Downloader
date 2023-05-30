import requests
import requests, re, os
from requests.utils import quote
import emoji
from time import sleep

path = os.getcwd()

cookie = "Your roblox security token goes here."

session = requests.Session()
session.cookies[".ROBLOSECURITY"] = cookie

req = session.post(
    url="https://auth.roblox.com/"
)

if "X-CSRF-Token" in req.headers: 
    session.headers["X-CSRF-Token"] = req.headers["X-CSRF-Token"] 
req2 = session.post(
    url="https://auth.roblox.com/"
)

try:
    getuser = session.get("https://users.roblox.com/v1/users/authenticated")
    getuser2 = getuser.json()
    getuser3 = getuser2['id']
    getuser4 = getuser2['name']
    print(f"Logged in as {getuser4}\n")

except:
    print(f"Your cookie is invalid")
    input()

name = input("Enter The Group Name: ")
"\n"

quote = quote(name)
cursor_page = 0

url = f"https://catalog.roblox.com/v1/search/items?category=All&creatorName={quote}&creatorType=Group&limit=120&salesTypeFilter=1"

a = requests.get(url)
nextpagecursor = a.json()

try:
    nextpagecursor = nextpagecursor["nextPageCursor"]
except:
    print("Issue getting next page, try different key words/different sort - restart program")
    input()

ids_and_item_types = a.json()["data"]

if len(ids_and_item_types) == 0:
    print("No items found (bad keywords)")
    input()

friendslist = [datum["id"] for datum in ids_and_item_types]
cursor_page+=1

while True:
    cursor_page+=1
    abx = "https://catalog.roblox.com/v1/search/items?category=All&creatorName={quote}&creatorType=Group&cursor={nextpagecursor}&limit=120&salesTypeFilter=1"
    thelinks = abx
    a = requests.get(thelinks)
    nextpagecursor = a.json()
        
    try:
        nextpagecursor = nextpagecursor["nextPageCursor"]
    except:
        print(f"Max page limit of {cursor_page} has been reached")
        break
        
    ids_and_item_types = a.json()["data"]
    haha = [datum["id"] for datum in ids_and_item_types]
    friendslist.extend(haha)

print(friendslist)

print("\nYou may close the program once you have enough, or program will continue till limit.")
"\n"
def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)
            
amount = 0   

for i in friendslist:
    try:
        r = requests.get(re.findall(r'<url>(.+?)(?=</url>)', requests.get(f'https://assetdelivery.roblox.com/v1/asset?id={i}').text.replace('http://www.roblox.com/asset/?id=', 'https://assetdelivery.roblox.com/v1/asset?id='))[0]).content
        data = {
        "items": [
            {
            "itemType": "Asset",
            "id": i
            }
        ]
        }       
        a = session.post("https://catalog.roblox.com/v1/catalog/items/details",json=data)
        a=a.json()
        a=a['data'][0]['name']
        b=a
        b = remove_emoji(b)
        if len(r) >= 7500:
            print(f'Downloaded: {amount}')
            with open(f'Group/{b}.png', 'wb') as f:
                f.write(r)
            amount+=1
            sleep(60)
        else:
            print(f'Unable to download this asset, retrying')
    except:
        print(f'Unable to download asset')
        pass
print(f"Completed, downloaded {amount} clothes")