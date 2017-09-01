import time
import webbrowser
import json
import requests

pause = ('-----------------------------')


def main():  # Main Menu Function
    print('1. API Options''\n''2. Steam options''\n''3. Check for vac banned accounts' '\n' 
          '4. Check for trade banned accounts' '\n' '5. Check for Community banned accounts')  # Main menu option list
    Main_menu_input = input('enter number: ')
    if Main_menu_input == '1':
        api_options()
    elif Main_menu_input == '2':
        Steam_options()
    elif Main_menu_input == '3':
        acc_check_vac()
    elif Main_menu_input == '4':
        acc_check_trade()
    elif Main_menu_input == '5':
        acc_check_community()
    elif Main_menu_input == '6':
        process_data_vac()
    else:
        print('Wrong number returning to Main Menu')
        return_to_mm()


def api_options():  # API options
    print(pause)
    print('1. Add Steam API KEY''\n''2. Remove Steam API''\n''8. Get API Key''\n''9. Return To Main Menu')
    userinput1 = input('Enter number: ')
    if userinput1 == '1':  # Add api
        print(pause)
        api_input = input('Enter api: ')
        settings = {'API KEY': api_input}
        with open('Api.json', 'w') as f:
            json.dump(settings, f)
        api_options()
    elif userinput1 == '2':  # Remove API
        print(pause)
        settings = {'API KEY': ''}
        with open('Api.json', 'w') as f:
            json.dump(settings, f)
        api_options()
    elif userinput1 == '8':  # API LINK
        print(pause)
        webbrowser.open_new('https://steamcommunity.com/dev/apikey')
        print('In domain tab you can write whatever you want!!')
        api_options()
    elif userinput1 == '9':
        return_to_mm()
    else:  # If wrong number
        print('Wrong number returning')
        api_options()


def Steam_options():  # Steam options
    print(pause)
    print(
        '1. Add steam ID' '\n' '2. Remove Steam ID (NOT WORKING YET)''\n''3. Steam ID Converter''\n'
        '7. Advanced steam ID converter (another script) ''8. Steam ID64 checker (external site)''\n''9. Main Menu')
    userinput2 = input('Enter number: ')
    if userinput2 == '1':
        print(pause)
        steamid = input('Enter Steam ID you want to add: ')
        file = open('Steam_id_list.txt', "a")
        file.write(steamid + ',')
        file.close()
        print('steam ID: ' + steamid + ' has been added!')
        Steam_options()
    elif userinput2 == '2':
        print(pause)
        print('test')  # add removal
        Steam_options()
    elif userinput2 == '3':  # STEAM ID CONVERTER
        Steam_ID_converter()
    elif userinput2 == '7':
        webbrowser.open_new('https://github.com/arhi3a/Steam-ID-Converter')
        Steam_options()
    elif userinput2 == '8':  # Steam ID64 checker site
        webbrowser.open_new('https://steamid.io/lookup/')
        Steam_options()
    elif userinput2 == '9':
        return_to_mm()
    else:  # If wrong number
        print('wrong number returning')
        Steam_options()


def return_to_mm():  # If wrong number
    print(pause)
    time.sleep(1)
    main()


def acc_check_vac():
    print(pause)
    get_data()
    process_data_vac()
    print(pause)
    return_to_mm()


def acc_check_trade():
    print(pause)
    get_data()
    process_data_trade()
    print(pause)
    return_to_mm()


def acc_check_community():
    print(pause)
    get_data()
    process_data_community()
    print(pause)
    return_to_mm()


def Steam_ID_converter():
    print(pause)
    print('1. Convert SteamID32 to SteamID64 (xxxxxxxx) ' '\n' '2. SteamID to SteamID64 (Steam_x:x:xxxxxxxx)'
          '\n' '3. Get SteamID64 from nickname (NOT WORKING YET)' '\n' '8. Return to Steam Options' '\n''9. Main Menu')
    userinput3 = input('Enter number: ')
    ID_change_value = 76561197960265728
    if userinput3 == '1':  # ID32 to ID64 xxxxxxxxxxxxxxxxx(x= numbers)
        print(pause)
        userinput4 = input('Enter SteamID32: ')
        sum = int(userinput4) + int(ID_change_value)
        print('SteamID64: {0} '.format(sum))
        userinput9 = input('Do you want to add SteamID64 to ban check list?' '\n' '1. Yes' '\n' '2. No' '\n' ': ')
        if userinput9 == '1':
            print(pause)
            file = open('Steam_id_list.txt', "a")
            file.write(str(sum) + ',')
            file.close()
            print('SteamID64: {0} '.format(sum), 'Has been saved')
            Steam_ID_converter()
        elif userinput9 == '2':
            Steam_ID_converter()
        else:
            Steam_ID_converter()
    elif userinput3 == '2':  # SteamID to ID64  STEAM_0:y:zzzzzzz
        print(pause)
        userinput6 = input('Enter Steam ID: ')  # User ID input
        y = userinput6[8:9]  # STEAM_0:y:zzzzzz
        z = userinput6[10:]  # STEAM_0:y:z
        Steam_ID_32_conv = int(z) * int(2) + int(y)
        Steam_ID_64_conv = int(Steam_ID_32_conv) + int(ID_change_value)
        print('Steam ID32: ', Steam_ID_32_conv)
        print('Steam ID64: ', Steam_ID_64_conv)
        userinput7 = input(
            'Do you want to add SteamID64 to ban checklist?' '\n' '1. Yes' '\n' '2. No' '\n' ': ')  # Do you want to save data question
        if userinput7 == '1':  # If yes
            print(pause)
            file = open('Steam_id_list.txt', "a")
            file.write(str(Steam_ID_64_conv) + ',')
            file.close()
            print('steam ID64: ', str(Steam_ID_64_conv) + ' has been added!')
            Steam_ID_converter()
        elif userinput7 == '2':  # If no
            Steam_ID_converter()
        else:
            print(pause)
            print('Wrong number returning')
            Steam_ID_converter()
    elif userinput3 == '4':  # Steam ID form URL http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=APIKEY&vanityurl=Nick
        print(pause)
        userinput8 = input('Write nickname: ')
        api_steam = open('api_config.txt', 'r+')
        nick_url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=' + api_steam.read() + '&vanityurl=' + userinput8
        webbrowser.open_new(nick_url)
        Steam_options()  # temporary delete it!!
    elif userinput3 == '8':
        Steam_options()
    elif userinput3 == '9':
        return_to_mm()
    else:  # if wrong number
        print('Wrong number')
        Steam_ID_converter()


def get_data():
    api_steam_load = open('Api.json', 'r+')
    api_steam = json.load(api_steam_load)
    api_steam_load.close()
    ac = open('Steam_id_list.txt', 'r+')  # steam account read
    url_final = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + api_steam[
        'API KEY'] + '&steamids=' + ac.read()  # REPAIR API KEY READ
    data_from_site = requests.get(url_final)
    file = open('Data_bans.json', 'w')  # change file name
    file.write(str(data_from_site.text))  # Puts data from site to file
    file.close()
    if str(data_from_site)[11:14] == '200':  # Check server response
        print('Data download: Success!')  # If data download is OK
    else:
        print('Data download: Error' '\n' 'Code: ' + str(data_from_site))  # If data download fails
    print(pause)


def process_data_vac():
    file_base = open('Data_bans.json', 'r+')  # change file name
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    print('Checking data for: ', n, 'Entries')  # prints number of players to check
    print(pause)
    userinput10 = input('Do you want to see only vac banned accounts?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ') #
    print(pause)
    if userinput10 == '1': #Only banned accounts
        for n in range(0, n):  # start of checking loop
            if (data['players'][n]['VACBanned']) == bool('True'):  # If player has vac ban
                if data['players'][n]['NumberOfVACBans'] == int(1):  # grammar thing
                    print(data['players'][n]['SteamId'] + ' Vac Banned ||', data['players'][n]['NumberOfVACBans'],
                          'time || Last time:', data['players'][n]['DaysSinceLastBan'],
                          'Days ago')  # Grammar thing option 1
                else:
                    print(data['players'][n]['SteamId'] + ' Vac Banned ||', data['players'][n]['NumberOfVACBans'],
                          'times || Last time:', data['players'][n]['DaysSinceLastBan'],
                          'Days ago')  # grammar thing option 2
    elif userinput10 == '2': #All accounts
        for n in range(0, n):  # start of checking loop
            if (data['players'][n]['VACBanned']) == bool('True'):  # If player has vac ban
                if data['players'][n]['NumberOfVACBans'] == int(1):  # grammar thing
                    print(data['players'][n]['SteamId'] + ' Vac Banned ||', data['players'][n]['NumberOfVACBans'],
                      'time || Last time:', data['players'][n]['DaysSinceLastBan'],
                      'Days ago')  # Grammar thing option 1
                else:
                    print(data['players'][n]['SteamId'] + ' Vac Banned ||', data['players'][n]['NumberOfVACBans'],
                      'times || Last time:', data['players'][n]['DaysSinceLastBan'],
                      'Days ago')  # grammar thing option 2
            else:
                print(data['players'][n]['SteamId'] + ' Clean')  # Players is clean


def process_data_trade():
    file_base = open('Data_bans.json', 'r+')  # change file name
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    print('Checking data for: ', n, 'Entries')  # prints number of players to check
    print(pause)
    userinput11 = input('Do you want to see only banned accounts?' '\n' '1. yes' '\n' '2. No' '\n' 'Answer: ')
    if userinput11 == '1':
        for n in range(0, n):
            if (data['players'][n]['EconomyBan']) == ('banned'):
                print(data['players'][n]['SteamId'], 'Trade Banned')
    elif userinput11 == '2':
        for n in range(0, n):
            if (data['players'][n]['EconomyBan']) == ('banned'):
                print(data['players'][n]['SteamId'], 'Trade Banned')
            else:
                print(data['players'][n]['SteamId'], 'Clean')


def process_data_community():
    file_base = open('Data_bans.json', 'r+')  # change file name
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    print('Checking data for: ', n, 'Entries')  # prints number of players to check
    print(pause)
    userinput12 = input('Do you want to see only banned accounts?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
    if userinput12 == '1':
        for n in range(0, n):
            if (data['players'][n]['CommunityBanned']) == bool('true'):
                print(data['players'][n]['SteamId'], 'Community ban')
    elif userinput12 == '2':
        for n in range(0, n):
            if (data['players'][n]['CommunityBanned']) == bool('true'):
                print(data['players'][n]['SteamId'], 'Community ban')
            else:
                print(data['players'][n]['SteamId'], 'Clean')


main()
