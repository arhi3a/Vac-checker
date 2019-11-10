import json
import time
# import webbrowser
import requests
from os import path
from sys import argv


class VacChecker(object):
    """This class is used to gather data using steam API and return vac acccounts that has been banned"""

    def __init__(self):
        self.settings_file_name = 'Settings.json'
        self.steam_id_file_name = 'Steam_id_list.txt'
        self.pause = '-----------------------------'
        self.vac_banned = []
        self.community_banned = []
        self.economy_banned = []
        self.get_args()
        if path.isfile(self.settings_file_name) is False:
            self.first_start()

    def get_args(self):
        arguments = argv
        if len(arguments) >= 2:  # if more then 1 argument interpret it
            if arguments[1] == '-a':
                ids = arguments[2].split(',')
                self.add_steam_id(ids)
            elif arguments[1][1] == 's':
                if '-sa' in arguments:
                    self.api_options(1, arguments[2])
                else:
                    self.first_start()
            elif arguments[1] == '-r':
                ids = arguments[2].split(',')
                self.remove_steam_id(ids)
            elif arguments[1] == '-d':
                self.download_data()
            elif arguments[1] == '-f':
                return self.all()
            else:
                raise Exception('Unknown Argument')
        else:  # if no arguments given print help
            print('Please enter argument eg. Python3 vac_checker.py -a xxxx,yyy to add steam IDs to scan'
                  '\n -f run all needed functions'
                  '\n -a steamid,steamid... to add given steam ids'
                  '\n -r steamid,steamid... to remove given steam ids'
                  '\n -s To run first setup again'
                  '\n    -sa key add api key'
                  '\n -g download data')

    def first_start(self, step=0):
        """Asks user for needed information during first start of application"""
        if step == 0:
            self.api_options()
        print('FIRST SETUP IS COMPLETE')

    def api_options(self, userinput=None, api_key=None):  # API options
        print(self.pause)
        print('1. Add Steam API KEY''\n''8. Get API Key''\n''9. To continue first setup')
        if userinput is None:
            userinput1 = input('Enter number: ')
        else:
            userinput1 = userinput
        if userinput1 == '1':  # Add api
            print(self.pause)
            if api_key is None:
                api_input = input('Enter api: ')
            else:
                api_input = api_key
            settings = {'API KEY': api_input}
            with open(self.settings_file_name, 'w') as f:
                json.dump(settings, f)
            self.api_options()
        elif userinput1 == '8':  # API LINK
            print(self.pause)
            # webbrowser.open_new('https://steamcommunity.com/dev/apikey')
            print('Please visit\nhttps://steamcommunity.com/dev/apikey')
            print('In domain tab you can write whatever you want!!')
            self.api_options()
        elif userinput1 == '9':
            self.first_start(1)
        else:  # If wrong number
            print('Wrong number returning')
            self.api_options()

    def add_steam_id(self, steam_id, f=None):
        """Adds steam id to the list.
        if str is given adds 1 steam id
        if list is given adds multiple steam ids"""
        if steam_id == str:  # if it's single steam id make it a list so we can 'iterate' thorough it
            steam_id = [steam_id]
        if path.isfile(self.steam_id_file_name):  # If file exist append to it
            mode = 'a'
        else:  # if not create it
            mode = 'w'
        if f == 1:  # if flag is set to 1 force create it (overwrites old file)
            mode = 'w'
        with open(self.steam_id_file_name, mode) as file:  # opens file and adds values from list as new rows in file
            for row_id in steam_id:
                file.writelines('\n' + row_id)

    def read_steam_id(self):
        """Reads steam ID's and returns id list"""
        with open(self.steam_id_file_name, 'r') as file:
            file.readline()
            return file.read().splitlines()  # reads file and deletes \n at the end of each line

    def remove_steam_id(self, steam_id):
        """Removes steam id to the list.
        if str is given adds 1 steam id
        if list is given adds multiple steam ids"""
        if steam_id == str:  # if it's single steam id make it a list so we can 'iterate' thorough it
            steam_id = [steam_id]
        if path.isfile(self.steam_id_file_name) is False:  # if file is not found we can't delete given ids
            raise FileNotFoundError('FILE WITH STEAM ID WAS NOT FOUND')
        ids_in_file = self.read_steam_id()  # read data from file
        for id_to_remove in steam_id:  # Iterate through list of given ids
            if str(id_to_remove) in ids_in_file:  # if it's found in file
                ids_in_file.remove(str(id_to_remove))  # remove it
        self.add_steam_id(ids_in_file, 1)  # rewrite file without deleted ids

    def split_to_batches(self, data):
        """Splits steam_id data to batches of 99 because of 100 items per request limitation"""
        output = []
        cnt = 0
        tmp = []
        for i in data:
            if cnt < 99:
                tmp.append(i)
                cnt += 1
            else:
                cnt = 0
                output.append(tmp)
                tmp = []
                tmp.append(i)
        output.append(tmp)
        return output

    def api_format(self, data):
        """formats data to the format that can can be used in url query"""
        output = []
        for i in data:
            output.append(','.join(i))
        return output

    def download_data(self):
        data = self.read_steam_id()  # read data from file
        data = self.split_to_batches(data)  # split data to batches
        data_api_format = self.api_format(data)  # format batches to api format
        with open(self.settings_file_name) as api_steam_load:  # read api key from settings
            api_key = json.load(api_steam_load)['API KEY']
        cnt = 1
        for batch in data_api_format:  # Iterate through batches
            url_final = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + api_key + '&steamids=' + batch
            data_from_site = requests.get(url_final)
            print('Downloading batch {cnt} of {all}'.format(cnt=cnt, all=len(data_api_format)))
            # if str(data_from_site)[11:14] == '200':  # Check server response
            #     print('Data download: Success!')  # If data download is OK
            # else:
            #     print('Data download: Error' '\n' 'Code: ' + str(
            #         data_from_site))  # If data download fails
            print(self.pause)
            if cnt == 1:  # If it's first run
                mode = 'w'  # overwrite old file
            else:  # If it's not first run
                mode = 'a'  # append to the end
            with open('Data_bans.json', mode) as file:
                file.write(str(data_from_site.text))
            cnt += 1
            time.sleep(2)

    def process_ban_data(self):
        """Interprets downloaded data"""
        file_base = open('Data_bans.json', 'r+')
        data = json.load(file_base)
        file_base.close()
        n = (len(data['players']))  # Check number of lists
        print('Checking data for: ', n,
              'Entries')  # prints number of players to check
        for n in range(0, n):  # start of checking loop
            if (data['players'][n]['VACBanned']) == bool(
                    'True'):  # If player has vac ban
                banned_player = [data['players'][n]['SteamId'],
                                 data['players'][n]['NumberOfVACBans'],
                                 data['players'][n]['DaysSinceLastBan']]
                self.vac_banned.append(banned_player)
            if (data['players'][n]['EconomyBan']) == ('banned'):
                banned_player = (data['players'][n]['SteamId'])
                self.economy_banned.append(banned_player)
            if (data['players'][n]['CommunityBanned']) == bool('true'):
                banned_player = (data['players'][n]['SteamId'])
                self.community_banned.append(banned_player)

    def all(self):
        """runs all functions in correct order
        returns [vac_bans, community_bans, economy_bans] as lists"""
        self.download_data()
        self.process_ban_data()
        print(self.vac_banned, self.community_banned, self.economy_banned)
        return [self.vac_banned, self.community_banned, self.economy_banned]


a = VacChecker()
