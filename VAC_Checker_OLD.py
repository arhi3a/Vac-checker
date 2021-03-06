import json
import time
import webbrowser

import requests

pause = ('-----------------------------')


def main():  # Main Menu Function
    print('1. API Options''\n''2. Steam options''\n''3. Check for vac banned accounts' '\n'
          '4. Check for trade banned accounts' '\n' '5. Check for Community banned accounts' '\n' '9. Exit program')  # Main menu option list
    main_menu_input = input('enter number: ')
    if main_menu_input == '1':
        api_options()
    elif main_menu_input == '2':
        steam_options()
    elif main_menu_input == '3':
        acc_check_vac()
    elif main_menu_input == '4':
        acc_check_trade()
    elif main_menu_input == '5':
        acc_check_community()
    elif main_menu_input == '6':
        process_data_vac()
    elif main_menu_input == '7':
        last_login()
    elif main_menu_input == '9':
        quit_program()
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


def steam_options():  # Steam options
    print(pause)
    print(
        '1. Add steam ID' '\n' '2. Remove Steam ID (NOT WORKING YET)''\n''3. Steam ID Converter''\n'
        '7. Advanced steam ID converter (another script)''\n' '8. Steam ID64 checker (external site)''\n''9. Main Menu')
    userinput2 = input('Enter number: ')
    if userinput2 == '1':
        print(pause)
        steamid = input('Enter Steam ID you want to add: ')
        file = open('Steam_id_list.txt', "a")
        file.write(steamid + ',')
        file.close()
        print('steam ID: ' + steamid + ' has been added!')
        steam_options()
    elif userinput2 == '2':
        print(pause)
        print('test')  # add removal
        steam_options()
    elif userinput2 == '3':  # STEAM ID CONVERTER
        steam_id_converter()
    elif userinput2 == '7':
        webbrowser.open_new('https://github.com/arhi3a/Steam-ID-Converter')
        steam_options()
    elif userinput2 == '8':  # Steam ID64 checker site
        webbrowser.open_new('https://steamid.io/lookup/')
        steam_options()
    elif userinput2 == '9':
        return_to_mm()
    else:  # If wrong number
        print('wrong number returning')
        steam_options()


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


def steam_id_converter():
    print(pause)
    print('1. Convert SteamID32 to SteamID64 (xxxxxxxx) ' '\n' '2. SteamID to SteamID64 (Steam_x:x:xxxxxxxx)'
          '\n' '3. Get SteamID64 from nickname (NOT WORKING YET)' '\n' '8. Return to Steam Options' '\n''9. Main Menu')
    userinput3 = input('Enter number: ')
    id_change_value = 76561197960265728
    if userinput3 == '1':  # ID32 to ID64 xxxxxxxxxxxxxxxxx(x= numbers)
        print(pause)
        userinput4 = input('Enter SteamID32: ')
        sum_id = int(userinput4) + int(id_change_value)
        print('SteamID64: {0} '.format(sum_id))
        userinput9 = input('Do you want to add SteamID64 to ban check list?' '\n' '1. Yes' '\n' '2. No' '\n' ': ')
        if userinput9 == '1':
            print(pause)
            file = open('Steam_id_list.txt', "a")
            file.write(str(sum_id) + ',')
            file.close()
            print('SteamID64: {0} '.format(sum_id), 'Has been saved')
            steam_id_converter()
        elif userinput9 == '2':
            steam_id_converter()
        else:
            steam_id_converter()
    elif userinput3 == '2':  # SteamID to ID64  STEAM_0:y:zzzzzzz
        print(pause)
        userinput6 = input('Enter Steam ID: ')  # User ID input
        y = userinput6[8:9]  # STEAM_0:y:zzzzzz
        z = userinput6[10:]  # STEAM_0:y:z
        steam_id32_conv = int(z) * int(2) + int(y)
        steam_id_64_conv = int(steam_id32_conv) + int(id_change_value)
        print('Steam ID32: ', steam_id32_conv)
        print('Steam ID64: ', steam_id_64_conv)
        userinput7 = input(
            'Do you want to add SteamID64 to ban checklist?' '\n' '1. Yes' '\n' '2. No' '\n' ': ')  # Save data?
        if userinput7 == '1':  # If yes
            print(pause)
            file = open('Steam_id_list.txt', "a")
            file.write(str(steam_id_64_conv) + ',')
            file.close()
            print('steam ID64: ', str(steam_id_64_conv) + ' has been added!')
            steam_id_converter()
        elif userinput7 == '2':  # If no
            steam_id_converter()
        else:
            print(pause)
            print('Wrong number returning')
            steam_id_converter()
    elif userinput3 == '4':  # Steam ID form URL
        print(pause)
        userinput8 = input('Write nickname: ')
        api_steam = open('api_config.txt', 'r+')
        nick_url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=' + api_steam.read() + \
                   '&vanityurl=' + userinput8
        webbrowser.open_new(nick_url)
        steam_options()  # temporary delete it!!
    elif userinput3 == '8':
        steam_options()
    elif userinput3 == '9':
        return_to_mm()
    else:  # if wrong number
        print('Wrong number')
        steam_id_converter()


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
    file_base = open('Data_bans.json', 'r+')
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    print('Checking data for: ', n, 'Entries')  # prints number of players to check
    print(pause)
    userinput10 = input('Do you want to see only vac banned accounts?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')  #
    print(pause)
    if userinput10 == '1':  # Only banned accounts
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
        direct_link_vac()
    elif userinput10 == '2':  # All accounts
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
        direct_link_vac()
    else:
        print('Wrong number')
        print(pause)
        process_data_vac()


def direct_link_vac():
    print(pause)
    input_direct = input('Do you want to get direct link to banned accounts' '\n' '1. Yes' '\n' '2. No' '\n')
    print(pause)
    file_base = open('Data_bans.json', 'r+')
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    if input_direct == '1':
        for n in range(0, n):
            if (data['players'][n]['VACBanned']) == bool('True'):
                print('http://steamcommunity.com/profiles/' + data['players'][n]['SteamId'])
        return_to_mm()
    if input_direct == '2':
        return_to_mm()
    else:
        print('Wrong number')
        direct_link_vac()


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
            direct_link_trade()
    elif userinput11 == '2':
        for n in range(0, n):
            if (data['players'][n]['EconomyBan']) == ('banned'):
                print(data['players'][n]['SteamId'], 'Trade Banned')
            else:
                print(data['players'][n]['SteamId'], 'Clean')
        direct_link_trade()
    else:
        print('wrong number')
        print(pause)
        process_data_trade()


def direct_link_trade():
    print(pause)
    input_direct = input('Do you want to get direct link to banned accounts' '\n' '1. Yes' '\n' '2. No' '\n')
    print(pause)
    file_base = open('Data_bans.json', 'r+')  # change file name
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    if input_direct == '1':
        for n in range(0, n):
            if (data['players'][n]['EconomyBan']) == ('banned'):
                print('http://steamcommunity.com/profiles/' + data['players'][n]['SteamId'])
        return_to_mm()
    if input_direct == '2':
        return_to_mm()
    else:
        print('Wrong number')
        direct_link_trade()


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
        direct_link_community()
    elif userinput12 == '2':
        for n in range(0, n):
            if (data['players'][n]['CommunityBanned']) == bool('true'):
                print(data['players'][n]['SteamId'], 'Community ban')
            else:
                print(data['players'][n]['SteamId'], 'Clean')
        direct_link_community()

    else:
        print('Wrong number')
        process_data_community()


def direct_link_community():
    print(pause)
    input_direct = input('Do you want to get direct link to banned accounts' '\n' '1. Yes' '\n' '2. No' '\n')
    print(pause)
    file_base = open('Data_bans.json', 'r+')  # change file name
    data = json.load(file_base)
    file_base.close()
    n = (len(data['players']))  # Check number of lists
    if input_direct == '1':
        for n in range(0, n):
            if (data['players'][n]['CommunityBanned']) == bool('true'):
                print('http://steamcommunity.com/profiles/' + data['players'][n]['SteamId'])
        return_to_mm()
    if input_direct == '2':
        return_to_mm()
    else:
        print('Wrong number')
        direct_link_community()


def last_login():
    get_data()  # Downloads new ban data
    time.sleep(3)
    file_base = open('Data_bans.json', 'r+')  # Load new ban data
    data = json.load(file_base)
    file_base.close()

    file_base_old = open('Data_bans_old.json', 'r+')  # Loads old ban data
    data_old = json.load(file_base_old)
    file_base_old.close()

    n_new = (len(data['players']))  # Number of users in old ban data
    n_old = ((len(data_old['players'])))  # Number of users in new ban data
    n = n_new  # Lazy way :D

    if n_new == (n_old):  # Check if number of profiles to check matches
        print(pause)
        for n in range(0, n):  # loop to print diffrences in vac ban status
            if (data['players'][n]['VACBanned']) != (data_old['players'][n]['VACBanned']):
                print(data['players'][n]['SteamId'] + ' Vac Banned since last login || ',
                      data['players'][n]['DaysSinceLastBan'], ' Days ago')
            if (data['players'][n]['EconomyBan']) != (data_old['players'][n]['EconomyBan']):
                print(data['players'][n]['SteamId'] + ' Trade Banned since last login')
            if (data['players'][n]['CommunityBanned']) != (data_old['players'][n]['CommunityBanned']):
                print((data['players'][n]['SteamId'] + ' Community Banned since last login'))
        print(pause)
    else:  # If number of profiles to check does not match
        print('Data does not match skipping banned since last login')
    return_to_mm()


def quit_program():
    data_new = open('Data_bans.json', 'r+')
    data_old = open('Data_bans_old.json', 'w')
    data_old.write(str(data_new.read()))
    data_old.close()
    print(pause)
    print('Goodbye')
    print(pause)
    quit()


def startup():
    main()


startup()
