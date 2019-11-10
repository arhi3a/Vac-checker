# How to use:
1. Add api key
2. Add steam accounts **(SteamID64 ONLY)[There is a converter you can use](CSGO console gives you SteamID to convert to steam ID64 use option 2 in Steam ID converter]**
3. Run 'Check for banned accounts'<br /><br />
Additional info:<br />
If you want to get steamID of players profile during game you can write status in game console<br />
If you want to remove steamID go to Steam_ID_list.txt and delete it manually (SteamID removal will be added later) <br/>
If you want  want to use 'banned since last login' add ``last_login()`` in ``def startup()`` <br/>
**If you want banned since last login function to work properly you must exit program using ``9. Exit program`` in main menu** <br/>
I will improve banned since last login function in some time <br/>
*sometimes it works sometimes steam gives steamID in different order and because program doesn't read actual steamIDs but their order in data base it causes error sometimes. I will change it in future updates* 
### How it looks: 
Main menu:<br />
![](http://i.imgur.com/A3VSawn.png)<br />
API Options:<br />
![](http://i.imgur.com/tauU5ko.png)<br />
Steam options:<br />
![](http://i.imgur.com/NpZxfmm.png)<br />
Steam ID converter:<br />
![](http://i.imgur.com/qqk0BZK.png)<br />
Results of check for banned accounts:<br />
xxxxxxxxxxx Vac Banned || 1 time || Last time: 1202 Days ago<br />
xxxxxxxxxxx clean<br />
xxxxxxxxxxx clean<br />
etc.
# To do:
- repair delete options
- ~~add community ban checker~~
- ~~add trade ban checke~~r
- move API key and other options like banned since last login to single Database
- make simple GUI
- ~~make banned since last login~~
- ~~show only banned people~~
- Get SteamID64 just by writing nickname
- ~~Direct link to banned ppl profile~~
- Move acc to check and api key to same file
- Remove limmitation of checking max 100acc 
- Automatically convert SteamID to SteamID64 while adding new acc to check  
