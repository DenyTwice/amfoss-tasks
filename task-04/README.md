# CineBot

I am a bit embarrassed by how long it took me to complete this task. I believe I should have done it in a day.

Anyhow, this was a fun task to do regardless. I have some experience working with discord bots so I did not have too much trouble
figuring out the outline of the program.

I had to figure out how to set environment variables in Linux since it's completely different from how Windows does it.

Getting the movie information from the API and sending it in the chat was easy enough. However, the API seems to be a bit 
inconsistent and I had to implement try-except to prevent the script from breaking when it can't find a movie. 

I also found the pyTelegram docs a bit bland and I ended up scouring open source telegram bots to figure out the easiest way to 
embed a picture along with the message. This took a while because I was looking for functions named like "embed" or "captioned 
picture" rather than just send_photo that took caption as an argument.

Working with CSV files was part of our syllabus in +2 so that was a breeze. I was also a bit suprised at how easy sending the 
file was. I thought I'd have to upload it somewhere online temporarily, get it's URL, pass it to the bot and so on.

![Video](CassioBot.mp4)
