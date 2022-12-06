import os
import telebot
import requests
import json
import csv

apiKey = os.getenv("APIID")
botID = os.getenv("PYTELE")

baseURL = "http://www.omdbapi.com/?apikey=" + apiKey + "&t="

bot = telebot.TeleBot(botID)
botRunning = True


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am Cassiopeia, a bot that will show movie information for you and export it in a CSV file.\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a great day!')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1. You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie and even '+\
         'some TV shows. For eg: \"/movie Arcane\"\n2. You can use \"/export\" command to export all the movie data in CSV format.\n'+\
         '3. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global filename

    bot.reply_to(message, 'Getting movie info...')

    reqURL = baseURL + str(message.text).lstrip("/movie ")

    req = requests.get(url=reqURL)
    json_obj = req.json()
    
    try:

        msg = "Title: " + json_obj['Title'] + "\nReleased: " + json_obj['Released'] + "\nGenre: " + json_obj['Genre'] + \
            "\nActors: " + json_obj['Actors'] + "\nLanguage: " + \
            json_obj['Language'] + "\nIMDb Rating: " + json_obj['imdbRating']

        bot.send_photo(message.chat.id, json_obj['Poster'], caption=msg)

    except KeyError:

        bot.send_message(message.chat.id, "Could not find movie. Please try another query.")

    rows = [["Title:", json_obj['Title']], ["Released ", json_obj['Released'] + json_obj['Year']], ["Genre: ", json_obj['Genre']],
            ["Actors:", json_obj['Actors']], ["Language:", json_obj["Language"]], ["IMDb Rating:", json_obj['imdbRating']]]

    filename = json_obj['Title'] + " Info.csv"

    with open(filename, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

    with open(filename, "r") as file:
        bot.send_document(message.chat.id, file)


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')


bot.infinity_polling()
