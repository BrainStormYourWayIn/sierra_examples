# from cTags import cTags
# from main_htm import *                                # To be imported if the repo has been cloned 
# from table import startTable
# from tags import *
# from write import *

from sierra import *

c = '<code>'                                            # As mentioned in the documentation, Python variables can be used in f-strings to be displayed on the 
cc = '</code>'                                          # web application.

if __name__ == "__main__":

    title('Documentation - Sierra -- 1.0.1')
    addFont(font_link='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap')
    addFont("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap")
    addFont("https://fonts.googleapis.com/css2?family=Oswald&display=swap")
    x = addImg(src="white_sierra.JPG", alt="Sierra logo_white", img_class="logo", href="https://github.com/BrainStormYourWayIn/sierra")
    x.show()
    x.css(margin_left='35%', margin_top='0px')
   

    a = tTags(True)
    a.css(color='black', font_family="'Roboto Mono', monospace")
    a.start_p(f'''This is the documentation of Sierra - A lightweight Python3 framework for building and integrating web applications. 
    Sierra is a Python3 library for building and integrating web applications with HTML and CSS using simple enough syntax. You can develop your web 
    applications purely in Python, taking advantage of its functionalities and integrating them to the fullest. Regular web dev added with Python3 is 
    a stream being explored by sierra. The documentation will elaborate on the syntax for this. In future releases, integration with Flask will be 
    available, and support might be extended for <a href="https://brython.info/static_doc/en/intro.html">brython over JS</a>''', True)

    head('Documentation - Sierra -- 1.0.1', font_size='30px', color='blue', text_align='left', font_family="'Prompt', sans-serif")
    openBody(background_color='white', opacity=0.8)    
    a.start_p(f'''Welcome to Sierra's documentation. The installation process is pretty simple, and is explained in the README of <a href="https://github.com/BrainStormYourWayIn/sierra">Sierra's GitHub</a> page.{b} <code>pip install sierra</code> can be done as a simpler way of installing. Any contributions to this project can also be made on the same page. {b}{b} Please view our <a href="https://github.com/BrainStormYourWayIn/sierra/blob/main/LICENSE">LICENSE</a> before moving forward.''')
    

    m = tTags(div_class='starting_off')
    m.start_div()

    a.start_p(f'''First, let us import the library {b}{b}
    <code>from sierra import *</code>{b}{b}
    If Sierra is manually being cloned from the repository, do make sure to use <code>pip install -r requirements.txt</code>{b}{b}
    Once imported, the first two lines of syntax are mandatory.''', True)
    
    openTags('pre')
    text = f'''
    
    if __name__ == "__main__":
        title('Your page title')

    # title(Title, icon='False') takes two arguments:
    # Title(str, compulsory)   : Title of the HTML file.
    # icon(str, optional)      : Tab icon to be displayed. Should be a .ico file. Defaults to no icon.
        '''

    writeHTML(text)
    writeCSS('pre', {"font-size": "15px", "background-color": "whitesmoke"})
    closeTags('pre')

    a.start_p(f'''head() is used to add a header to your page, and it takes multiple arguments for styling.
    {b} It is recommended to only use arg 'type' or arg 'font_size' at once. Using both defaults to ignoring arg type''', True)
    
    openTags('pre')
    text = f'''
    
    head(Head, font_size=False, font_family="Arial", type='header', color='black', text_align='left', background_color=False, padding=False, {b}height=False, width=False, line_break=False, line_height=False, border=False, margin=False)
    
    
    # Head (str, compulsory)           : Caption header.
    # font_size (str, optional)        : Font size in any valid measure. Leave blank, if not valid.
    # font_family (str, optional)      : any possible Font family. Defaults to Arial.
    # type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
    # color (str, optional)            : Color of Font in hex code. Defaults to 'black'.
    # text_align (str, optional)       : left|right|center|justify|initial|inherit. Defaults to 'left'.
    # background_color (str, optional) : Background color. Defaults to 'white'.
    # padding (str, optional)          : Padding. Defaults to False.
    # height (str, optional)           : Height of text. Defaults to False.
    # width (str, optional)            : Width of text. Defaults to False.
    # line_break (str, optional)       : Line break. Defaults to False.
    # line_height (str, optional)      : Line height. Defaults to False. 
    
        '''

    writeHTML(text)
    closeTags('pre')

    a.start_p(f'''The body of your web application which contains the main content can be started with {c}openBody(){cc}, and it can be styled using optional arguments. {b}{b}
    {c}openBody(background='False', background_color='white', background_image=False, opacity=False, background_size='cover', background_attachment='fixed', background_position=False, background_repeat=False){cc}{b}{b}It can similarly be closed using {c}closeBody(){cc} which takes no arguments.{b}{b}Initialization of CSS can be done using addInitc() and it is not mandatory.{b}{b}{c}addInitc(box_sizing='False', margin=False, padding=False, border=False, position='relative'){cc}{b}{b}Font links can be added using addFont(font_link)''')
    openTags('pre')

    text = f'''

    addFont(font_link="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap")

    # addFont() takes in one argument, which is the font link. It is the href to the font specified.
    # If the font is being taken from Google Fonts, copy only the href.
    # For example if the embed for the font 'Roboto' is &lt;link href="https://fonts.googleapis.com/css2
    # ?family=Roboto&display=swap" rel="stylesheet">, copy only the href on it, which is
    # "https://fonts.googleapis.com/css2?family=Roboto&display=swap".
    # Specify the font family as "'Roboto', sans-serif" (only in double quotes, since there are single 
    # quotes inside) in the argument <code>font_family</code> in the CSS function

    '''
    
    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='tags')
    m.start_div()

    openTags('pg_title')
    n = cTags('pg_title')
    n.css(font_family="'Prompt', sans-serif", font_size="20px")
    writeHTML('Tags - Open and close')
    closeTags('pg_title')
    a.start_p(f'''Multiple tags can be opened and closed simply by using openTags() and closeTags(). closeTagBefore() can be used to close any tag before the opening of another. This is intended to rectify unclosed tags is an easier manner.''', True)

    openTags('pre')
    text = f'''
    
    openTags(any_tag, *args)
    # openTags('tag1', 'tag2', 'tag3')
    closeTags(any_tag, *args)
    # closeTags('tag2', 'tag3')
    closeTagBefore(tag_to_close, tag_to_close_before)
    # closeTagBefore('tag1', 'tag3')
        '''

    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='cTags')
    m.start_div()

    openTags('pg_title')
    writeHTML('Working with CSS for XML tags')
    closeTags('pg_title')
    a.start_p(f'''XML tags can be opened with openTags(). The CSS for these tags can be done using <code>class cTags()</code>, where <code>css</code> is an object. <code>cTags</code> stand for 'cssTags' as a simpler way of adding CSS to non-native HTML tags. <code>cTags()</code> takes in one argument <code>tag</code> for which the CSS is to be applied.''', True)

    openTags('pre')
    text = f'''
    
    a = cTags('tag1')
    a.css(color='blue', font_family="Times New Roman", font_size="20px")

    # The object css takes in multiple arguments and applies them to the tag mentioned inside of cTags().
    a.css(color='black', font_family='Arial', font_weight=False, text_align=False, font_size=False, background_color=False, background=False, {b}margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, border=False, display='block', padding=False, height=False, {b}width=False, line_break=False, line_height=False, overflow=False, margin=False, box_shadow=False)
    
    # color (str, optional)            : CSS Color parameter. Defaults to 'black'.
    # font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
    # font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
    # text_align (str, optional)       : CSS Text-align parameter. Defaults to False.
    # font_size (str, optional)        : CSS Font-size parameter. Defaults to False.
    # background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
    # background (str, optional)       : CSS background parameter. Defaults to False.
    # margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
    # margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
    # margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
    # margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
    # border (str, optional)           : CSS border parameter. Defaults to '0px'.
    # display (str, optional)          : CSS display parameter. Defaults to 'block'.
    # padding (str, optional)          : CSS padding parameter. Defaults to False.
    # height (str, optional)           : CSS height parameter. Defaults to False.
    # width (str, optional)            : CSS width parameter. Defaults to False.
    # line_break (str, optional)       : CSS line-break parameter. Defaults to False.
    # line_height (str, optional)      : CSS line-height parameter. Defaults to False.
    # overflow (str, optional)         : CSS overflow parameter. Defaults to False.
    # margin (str, optional)           : CSS margin parameter. Defaults to False.
    # box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.

        '''

    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='tTags')
    m.start_div()

    openTags('pg_title')
    writeHTML(f'''Using division, section and p tags''')
    closeTags('pg_title')
    a.start_p(f'''Division, section and paragraph tags can be used with <code>class tTags()</code>, <code>tTags()</code> standing for 'titleTags', since the division and section tags basically stand for titles to identify areas within a page. {b} <code>tTags()</code> takes in three parameters. With the exception of the <code>p</code> tag, both the division and the section tags need to be closed manually. However, the <code>p</code> tag can be closed manually if desired so by simply leaving the second argument on <code>object start_p</code> blank, and auto closing of that tag defaults to bool False. Entering bool True closes the tag immediately after text is entered.''', True)

    openTags('pre')
    text = f'''
    
    tTags(p=False, div_class='False', sec_class='False')

    # p is a bool value, the name of the class is given to &lt;div> and &lt;section> in the second and third arguments respectively, if required

    a = tTags(p=True)
    a.start_p('Hello World!', close=True)
    a.css(color='green', font_family="Times New Roman", font_size="10px")

    # a.start_p(text, close=bool(False)) is used to start the paragraph and takes in one mandatory argument 'text', which is the paragraph content. {b}   # Arg close, if True, closes the paragraph once text is entered. Arg 'close' is set to False by default
    
    '''
    writeHTML(text)
    closeTags('pre')


    a.start_p(f'''CSS automatically applies to the tag whose argument has been mentioned in tTags().
    Multiple tags can be opened at once in any combination too but if this is done, CSS automatically applies the same arguments in a.css() to all tTags being used. It is hence recommended to open tags one at a time. {b} Once the required tags are opened, <code>a.start_div(takes no args)</code> or <code>a.start_sec(takes no args)</code> or <code>a.start_p()</code> is used to open the tag mentioned in tTags().''', True)

    openTags('pre')

    text = f'''

    a = tTags(div_class='newClass')
    a.start_div()                   # Takes no argument
    a.css(color='rgb(61, 37, 49)', font_family="Arial")

         # ---Content of the division---

    closeTags('div')                 # Close &lt;div>

    a = tTags(sec_class='anotherClass')
    a.start_sec()                    # Takes no argument
    a.css(color='rgb(38, 62, 89)', font_family="Times New Roman")

         # ---Content of the section---

    closeTags('section')              # Close &lt;section>


    # The object css takes in multiple arguments and applies them to the tag(s) mentioned inside of cTags().
    a.css(color='black', font_family='Arial', font_weight='False', text_align='False', font_size='False', background_color='False', {b}background='False', margin_top='False', margin_bottom='False', margin_left='False', margin_right='False', border='False', display='block', {b}padding='False', height='False', width='False', line_break='False', line_height='False', overflow='False', margin='False', box_shadow='False')
    
    # color (str, optional)            : CSS Color parameter. Defaults to 'black'.
    # font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
    # font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
    # text_align (str, optional)       : CSS Text-align parameter. Defaults to False.
    # font_size (str, optional)        : CSS Font-size parameter. Defaults to False.
    # background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
    # background (str, optional)       : CSS background parameter. Defaults to False.
    # margin_top (str, optional)       : CSS margin-top parameter. Defaults to 'False'.
    # margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to 'False'.
    # margin_left (str, optional)      : CSS margin-left parameter. Defaults to 'False'.
    # margin_right (str, optional)     : CSS margin-right parameter. Defaults to 'False'.
    # border (str, optional)           : CSS border parameter. Defaults to 'False'.
    # display (str, optional)          : CSS display parameter. Defaults to 'block'.
    # padding (str, optional)          : CSS padding parameter. Defaults to False.
    # height (str, optional)           : CSS height parameter. Defaults to False.
    # width (str, optional)            : CSS width parameter. Defaults to False.
    # line_break (str, optional)       : CSS line-break parameter. Defaults to False.
    # line_height (str, optional)      : CSS line-height parameter. Defaults to False.
    # overflow (str, optional)         : CSS overflow parameter. Defaults to False.
    # margin (str, optional)           : CSS margin parameter. Defaults to False.
    # box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.

        '''

    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='image')
    m.start_div()

    openTags('pg_title')
    writeHTML(f'''Adding images''')
    closeTags('pg_title')
    a.start_p(f'''Images can be added using <code>class addImg()</code> which takes in four arguments: {c}src{cc}, {c}href{cc}, {c}alt{cc} and {c}img_class{cc}, arg {c}src{cc} being mandatory, as it is the location of the image. {c}href{cc} if used, links the image to any specified location on click. {c}alt{cc} is the alternate text that is displayed if for some reason, the image is not displayed. {c}img_class{cc} is the class of the image, which is recommended if there are multiple images and multiple combinations of styling are needed.''', True)

    openTags('pre')
    text = f'''

    # a = addImg(src:str, href="False", alt="This is an image", img_class='False')        # Defaults
    a = addImg("location/to/the/image.jpeg", href="https://google.com", alt="Some image", img_class="newImg")

    a.show()                    # Takes no argument and displays the image with the conditions given

    a.css(height='30px', width='20px')

    # It is recommended to use arg img_class if multiple combinations of styling is used for multiple images

    a.css(self, height='False', width='False', margin='False', vertical_align='False', display='False', border='False', margin_top='False', {b}margin_bottom='False', margin_left='False', margin_right='False', opacity=False, {b}filter='False')

    margin_top (str, optional)       : CSS image margin-top parameter. Defaults to 'False'.
    margin_bottom (str, optional)    : CSS image margin-bottom parameter. Defaults to 'False'.
    margin_left (str, optional)      : CSS image margin-left parameter. Defaults to 'False'.
    margin_right (str, optional)     : CSS image margin-right parameter. Defaults to 'False'.
    border (str, optional)           : CSS image border parameter. Defaults to 'False'.
    display (str, optional)          : CSS image display parameter. Defaults to 'block'.
    height (str, optional)           : CSS image height parameter. Defaults to False.
    width (str, optional)            : CSS image width parameter. Defaults to False.
    margin (str, optional)           : CSS image margin parameter. Defaults to False.
    vertical-align (str, optional)   : CSS image vertical-align parameter. Defaults to False.
    opacity (int/float, optional)    : CSS image opacity parameter. Defaults to False.
    filter (str, optional)           : CSS image filter parameter. Defaults to False.

    '''
    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='tables')
    m.start_div()

    openTags('pg_title')
    writeHTML(f'''Adding a table (pandas supported)''')
    closeTags('pg_title')
    a.start_p(f'''Adding a table could never have been easier with {c}class startTable(){cc} which takes no arguments and has objects {c}createTable{cc} and {c}getTable(){cc}. {b}Sierra is compatible with Pandas, meaning just enter enter the path to the CSV file in {c}arg dataframe{cc} in {c}getTable(){cc}, and the table will display!''', True)

    openTags('pre')
    text = f'''
    
    a = startTable()
    a.getTable("path/to/file.csv")

    '''
    writeHTML(text)
    closeTags('pre')

    a.start_p(f'''A table can also be added using {c}createTable(){cc}. It takes in two arguments: {c}cols:list{cc} and {c}rows{cc}, where {c}rows{cc} is a list of lists. {c}cols{cc} is a list that contains the header row, which is basically the title of each column. {c}rows{cc} is a list of lists that contains the rows to be entered''', True)

    openTags('pre')
    text = f'''
    
    a = startTable()
    c = ['england', 'best', 'eight', 'euros']
    r1 = ['kane', 'grealish', 'sancho', 'foden']
    r2 = ['mount', 'rice', 'chilwell', 'stones']
    r = [r1, r2]
    a.createTable(cols=c, rows=r)

    # Outputs table:

    # england   best       eight     euros

    # kane      grealish   sancho    foden
    # mount     rice       chilwell  stones

    '''
    writeHTML(text)
    closeTags('pre')

    a.start_p(f'''Of course, CSS can be added with {c}a.css(){cc}''', True)

    openTags('pre')
    text = f'''
    
    a.css(border=False, width=False, height=False, border_collapse=False, color='black',
    font_family="Arial", font_weight=False, text_align=False, font_size=False, margin=False,
    background_color='white')

    '''
    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='other_funcs')
    m.start_div()

    openTags('pg_title')
    writeHTML(f'''Other functions''')
    closeTags('pg_title')
    a.start_p(f'''These are a list of other functions that can be used''', True)

    openTags('pre')
    text = f'''
    
    autoPrettify()
    # Improve overall look of HTML code and close all tags automatically (if not already done)
    # Warning: Auto prettifying also involves auto closing HTML tags which may not be accurate if not already closed and 
    # are not recommended. Further development may run into issues. Please close tags manually if unsure.
    # autoPrettify() at the moment seems to not work when sierra is pip installed. Hence please use this function 
    # only if the repository is cloned. This will be recitified in future versions.
    
    href(link:str, text:str)
    # Links any text to a specified location

    code(codeblock:str)
    # Shows any given text inside as code

    writeHTML(text)
    # Enters any text inside into the web application

    writeCSS(tag, *args)
    # Enters custom CSS arguments into any given tag

    # writeCSS('marquee', {{"font-size": "15px", "background-color": "whitesmoke"}})
    # Output in style.css
    # marquee {{
    #  font-size: 15px;
    #  background-color: whitesmoke;
    #  }}

    closeHTML()
    # Closes the HTML tag

    '''
    writeHTML(text)
    closeTags('pre', 'div')

    m = tTags(div_class='copyrights')
    m.start_div()

    openTags('copyrights')
    writeHTML(f'''Copyright Licenses Used''')
    closeTags('copyrights')
    b = cTags('copyrights')
    b.css(font_family="'Oswald', sans-serif;", margin_top="35px", font_size="25px")
    
    openTags('pre')
    text = f'''

Pandas (pandas) -- table


Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.

Copyright (c) 2011-2020, Open source contributors.

    '''
    writeHTML(text)
    closeTags('pre', 'div')

    closeBody()
    closeHTML()
    
    # autoPrettify()                                                   # See 'Other Functions'                       
