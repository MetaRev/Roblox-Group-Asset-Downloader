import requests
import requests, re, os
from requests.utils import quote
import emoji
from time import sleep

path = os.getcwd()

cookie = _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_6B7181A20281C96911B444CE1B2294EE92996EF81A4F61DBA81EC0192120D55628EDB8164C3F7927E91184ADC48447796664AC81AB8C0377DA1BBB6556136EBDCC49D8FCA32F0989CF0AED834F80CC2D4B2EA238A232D1D1DB7378631F149305AAF1CD8E366A898B24A67115643EB400CE3B30D766E367E160D7E456D2BFFDB472F567FE60396A6B1EB986AFEA817F6F3F5C35BE7404A14E881EE9BB6A599E4406A971FB163B3DAA30D01156743953BCD3AEE9AC6BF95ED0D278009B85B1657F74C1C1B0C907D736366317E4D2A2C01C0CB0B3B059642A915231EF92C08C98045B02519E4FAE86450595D359F576184042F90BD3859D4D77D30EF5DFC458551B88CDAD18F57E6015BA5748D775CC722D0D7D551378FBC8A7525773936FE0FAD0525AA5B5215D7E55993D404A69B3898C1A17CF77139281029D7D88CA6FFFAABF53DD035553D777EA888F445963956AE45467A06650AC893956476C3EBB8CA7659E7E0227C1DF607AC630029CEF3DA2B6535B4AD995A32EB165BA4053FE35AF2F13210EEEF3B83C88BE85D14864576A6E08D8AF507D9DD65111DB8E6BFCD2B4EAB791324CEFE5C343A641DF199F7A07AA526BFE54679CD8A0D056C9FBB1327E2E957099047679A886AA4C559ADE7D660CE8FBFFC681A938DB2277678E506298BBFE40CB91CD7CDDC3FFB7D83F7BFC2B5781E4B3C5E39FC8D3191B95659FC57CDCFDAB854DD2C1987462FD53AF2D9E706B05F70A8F08F0BE20E2EA4EE5866516B963C0CD2900555080F0C0B05FDBC47188C438DD52B48CA96D19E093CD561880A65965F5E6AD777F52B42173AF1139DBAACC361DDBE5FCC37E4A04AC7C7A4188FA809B63C607B2583DE060C34BD65C45263C522552483834F1C0DF4345F8D99620E5A477C50C9273399CF687E3171438C85164666AE3F432C38A3318A99C5B53269D76334A56BFFE50E533BE5687614324763135DC

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
