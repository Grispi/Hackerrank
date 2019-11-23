import unittest
import urllib.request
import json


class Solution:

    def run(self, teamKey):
        #
        # Some work here; return type and arguments should be according to the problem's requirements
        #
        url = (
            'https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json')
        request = urllib.request.urlopen(url)
        data_request = request.read()
        data_json = json.loads(data_request.decode())
        # print(data_json['rounds'][0]['matches'][0]['team1']
        #       ['key'], data_json['rounds'][0]['matches'][0]['score1'])
        data = data_json['rounds']
        goals = 0
        for i in range(len(data)):
            # print(data[i]['matches'])
            for x in range(len(data[i]['matches'])):
                teamName = data[i]['matches'][x]
                print("este es el", x, ":", teamName)
                if(teamName['team1']['key']) == teamKey:
                    # print(teamName['team1']['key'])
                    goals = goals + teamName['score1']
                    # print(goals)
                elif(teamName['team2']['key']) == teamKey:
                    # print(teamName['team2']['key'])
                    goals = goals + teamName['score2']
                    # print(goals)

        print(goals)
        return goals


so = Solution()
so.run("arsenal")
