import os
import telebot
import requests
import json
import csv

yourkey = os.getenv("APIID")
bot_id = os.getenv("PYTELE")

url = "http://www.omdbapi.com/?apikey=86c601ea&t="
bot = telebot.TeleBot(bot_id)
botRunning = True
chat_id = "5649898188"
    
filename = "movie.csv"

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    
@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRunning
    botRunning = True
    
    bot.reply_to(message, 'Getting movie info...')
    
    nUrl = url + str(message.text).lstrip("/movie ")

    r = requests.get(url=nUrl)
    json_obj = r.json()
    parsed = json.dumps(json_obj)
    data = json.loads(parsed)
    print(data)

    try:
        msg = "Title: " + data['Title'] + "\nReleased: " + data['Released'] + "\nGenre: " + data['Genre'] + "\nActors: " + data['Actors'] + "\nLanguage: " + data['Language']+ "\nIMDb Rating: " + data['imdbRating']
        bot.send_photo(chat_id, data['Poster'], caption=msg)
    except KeyError:
        bot.send(chat_id, "Could not find movie. Please try again.")
    # TODO: 2.1 Create a CSV file and dump the movie information in it

    rows = [["Title:", data['Title']], ["Released ", data['Released'] + data['Year']], ["Genre: ", data['Genre']], ["Actors:", data['Actors']], ["Language:", data["Language"]], ["IMDb Rating:", data['imdbRating']]]
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
    
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    with open(filename, "r") as csvfile:
        bot.send_document(message.chat.id, csvfile)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
