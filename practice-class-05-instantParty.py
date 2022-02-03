# Practice In Class 05 - Kattiana R.
# 02/01/2022

import sys
import webbrowser
import os

def insert_1(): # Disco Ball GIF
    discoBall = '<img width="300" height="400" src="https://c.tenor.com/lv08gSQ01yUAAAAM/disco-ball-bola-disco.gif" alt="Disco Ball">'

    return discoBall

def insert_2(): # Dancing People GIF
    dancingPeople = '<img src ="https://i.pinimg.com/originals/25/fb/a8/25fba81675f3b5afbbe6f69b0f9c7b56.gif" alt="Party!">'

    return dancingPeople

def insert_3(): # Lyric
    lyric = '<marquee width="300" height="315" behavior="scroll" direction="up"> Wise man said just walk this way * To the dawn of the light * Wind will blow into your face * As the years pass you by * Hear this voice from deep inside * Its the call of your heart * Close your eyes and you will find * Passage out of the dark * Here I am (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star * Wise man said just find your place * In the eye of the storm * Seek the roses along the way * Just beware of the thorns * Here I am (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star * Wise man said just raise your hand * And reach out for the spell * Find the door to the promised land * Just believe in yourself * Hear this voice from deep inside * Its the call of your heart * Close your eyes and you will find * The way out of the dark * Here I am (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star (Here I am) * Will you send me an angel? * Here I am (Here I am) * In the land of the morning star * </marquee> '

    return lyric

def insert_4(): # Today's Quote
    dailyQuote = '<script type="text/javascript" src="https://www.brainyquote.com/link/quotebr.js"></script> <small><i><a href="/quote_of_the_day" target="_blank" rel="nofollow"></a></i></small>'

    return dailyQuote

def insert_5(): # Music Video
    musicVideo = '<iframe width="600" height="315" src="https://www.youtube.com/embed/hwfErYUoqx8?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

    return musicVideo

def insert_6(): # Car GIF
    carImg = '<img width="300" height="315" src="https://64.media.tumblr.com/e35c794a8eba48b080682bec70b31c9f/tumblr_osl9ayXtil1v9ctwdo1_640.gifv" alt="Car">'

    return carImg

listOfFunctions = [insert_1(), insert_2(), insert_3(), insert_4(), insert_5(), insert_6()]

def make_table(row, col):
    counter = 0
    col_count = 0
    row_count = 0
  
    print('<table style="margin: 0 auto 0 auto;">')

    print('<h1><marquee behavior="scroll" direction="left">Welcome Humans &#129485 AND Robots &#129302 !</marquee></h1>')
  
    while row_count < row:
        print("<tr>")
        while col_count < col:
            print("<td>" + listOfFunctions[counter]+ "</td>")
            col_count += 1
            counter += 1
        print("</tr>")
        row_count += 1
        col_count = 0
     
    print("</table>")

def main():

    # Calling the Table + Templates
    make_table(2, 3)

    # Saving display into HTML file
    sys.stdout= open("InstantParty.html","w")
    make_table(2, 3)
    sys.stdout.close()

    # Pop-Up of the HTML File
    webFilePopUp = 'file:///'+os.getcwd()+'/' + 'InstantParty.html'
    webbrowser.open_new_tab(webFilePopUp)

main()
