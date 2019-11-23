# Star Wars Celebration

import unittest
import urllib.request
import json


class Solution:

    def run(self, film, character):
        #
        # Some work here; return type and arguments should be according to the problem's requirements
        #
        params_film = film.replace(' ', '%20')
        url_film = (
            'https://challenges.hackajob.co/swapi/api/films/?search=%s' % params_film)
        request_film = urllib.request.urlopen(url_film)
        data_film = request_film.read()
        data_film_json = json.loads(data_film.decode('utf-8'))
        # print(data_film_json['results'])
        characters_film = []
        for data in data_film_json['results']:
            for character_film in data['characters']:
                characters_film.append(character_film)
        characters_name = []

        for character_in_film in characters_film:
            url = character_in_film
            request = urllib.request.urlopen(url)
            data = request.read()
            data_json = json.loads(data.decode('utf-8'))
            characters_name.append(data_json['name'])
        characters_name.sort()

        characters_name_f = (', '.join(characters_name))

        params_character = character.replace(' ', '%20')
        url = ('https://challenges.hackajob.co/swapi/api/people/?search=%s' %
               params_character)
        request = urllib.request.urlopen(url)
        data = request.read()
        data_json = json.loads(data.decode('utf-8'))

        films = []
        for data in data_json['results']:
            for film_url in data['films']:
                films.append(film_url)

        films_name = []
        for film_url_name in films:
            url = film_url_name
            request = urllib.request.urlopen(url)
            data = request.read()
            data_json = json.loads(data.decode('utf-8'))
            films_name.append(data_json['title'])
        films_name.sort()

        films_name_f = (', '.join(films_name))
        # print(film,':',characters_name_f,';', character,':',films_name_f)
        if films:

            filmsAndCharacters = film+': '+characters_name_f+"; "+character+': '+films_name_f
        else:
            filmsAndCharacters = film+': '+characters_name_f+"; "+character+': none'
        print(filmsAndCharacters)
        return filmsAndCharacters


class SolutionMethods(unittest.TestCase):
        ##
        # /!\ Unit Tests are optional but highly recommended /!\
        ##
        # First Example
        ##
        # def test_example(self):
        #	self.assertEqual("this is an example", "this is an example")

        ##
        # Second Example
        ##
    def test_run(self):
        solution = Solution()
        self.assertEqual(solution.run("A New Hope", "Raymus Antilles"), "A New Hope: Beru Whitesun lars, Biggs Darklighter, C-3PO, Chewbacca, Darth Vader, Greedo, Han Solo, Jabba Desilijic Tiure, Jek Tono Porkins, Leia Organa, Luke Skywalker, Obi-Wan Kenobi, Owen Lars, R2-D2, R5-D4, Raymus Antilles, Wedge Antilles, Wilhuff Tarkin; Raymus Antilles: A New Hope, Revenge of the Sith")


if __name__ == "__main__":
    unittest.main()
