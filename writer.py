"""Program to convert text to handwriting in Python and HTML
"""


__author__ = 'BugBoy'   # https://github.com/bannyvishwas2020
__version__ = '1.0.0'   # Possibly; change if incorrect


# Import module `random` for function `random`
# for a random floating point between 0 and 1
import random


# Globally declare variables
letter_color = 'rgba(4, 16, 196, 1)'
letter_set = 'set0'
trcolor = False
letter_type = ''

htmlc = ['<html><head><style>.lines{width:100%;height:auto;float:left;}\
#paper{background:white;background-image:url("images/texture.png");\
height:auto;float:left;padding:50px 50px;width:90%;}img,span\
{height:25px;width:10px;float:left;margin-top:5px;margin-bottom:10px;}\
.clblack{filter:brightness(30%);}.clblue{filter:brightness(100%);}\
</style></head><body><div id="paper">']

with open('content.txt', 'r') as textfile:
    for line in textfile:
        
        # Strips the newline character
        curst = line.strip()
        htmlc.append('<div class="lines">')
        
        for ch in curst:
            # Get char ASCII Code of char
            chcode = ord(ch)
            
            # max 10 sets of letters
            random_letter = round(random.random()*10)
            
            # Enable the below statement if 10 sets of letters available
            # letter_set = 'set{}'.format(random_letter)
            if chcode == 35:
                if trcolor:
                    letter_color = 'rgba(4, 16, 196, 1)'
                    trcolor = False
                
                else:
                    letter_color = 'rgba(0, 0, 0, 1)'
                    trcolor = True
            
            elif chcode >= 65 and chcode <= 90:
                letter_type = 'caps'
                ch = ch.lower()
                
            elif chcode >= 97 and chcode <= 177:
                letter_type = 'small'
                
            elif chcode >= 48 and chcode <= 57:
                letter_type = 'others'
                ch = '{}'.format(chcode)
                
            elif(chcode == 32 or chcode == 36):
                htmlc.append('<span></span>')
                
            else:
                letter_type = 'others'
                ch = '{}'.format(chcode)
                
            if chcode != 35 and chcode != 32 and chcode != 36:
                htmlc.append('<img src="images/letters/{}/{}/{}/{}.png" />'\
                             .format(letter_set, letter_color,
                                     letter_type, ch))
        htmlc.append('</div>')

htmlc.append('</div></body></html>')

with open('page.html', 'w') as page_html:
    page_html.writelines(htmlc)
