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
        message, 'Hello there! I am Cassiopeia, a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, '1. You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie Inception\"\n\n2. You can use \"/export\" command to export all the movie data in CSV format.\n\n3. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRunning
    global filename
    botRunning = True

    bot.reply_to(message, 'Getting movie info...')

    reqURL = baseURL + str(message.text).lstrip("/movie ")

    req = requests.get(url=reqURL)
    json_obj = req.json()
    parsed = json.dumps(json_obj)
    data = json.loads(parsed)

    try:

        msg = "Title: " + data['Title'] + "\nReleased: " + data['Released'] + "\nGenre: " + data['Genre'] + \
            "\nActors: " + data['Actors'] + "\nLanguage: " + \
            data['Language'] + "\nIMDb Rating: " + data['imdbRating']

        bot.send_photo(message.chat.id, data['Poster'], caption=msg)

    except KeyError:

        bot.send_document(message.chat.id, "Could not find movie. Please try again.")

    rows = [["Title:", data['Title']], ["Released ", data['Released'] + data['Year']], ["Genre: ", data['Genre']],
            ["Actors:", data['Actors']], ["Language:", data["Language"]], ["IMDb Rating:", data['imdbRating']]]

    filename = data['Title'] + " Info.csv"

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
