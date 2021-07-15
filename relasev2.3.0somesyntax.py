from sierra import *


title('Documentation | Sierra - 2.3.0')

# writeWA("\n"r'<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
# writeWA("\n"r'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
# writeWA("\n"r'<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')

### CSS ###

with cTags('p') as p_tag:
    p_tag.css(font_family="'Ubuntu', sans-serif;", line_height='28px')
with cTags('pg_title') as pg_title:
    pg_title.css(font_family="'Signika Negative', sans-serif", font_size='25px', margin_top='30px', display='block')
writeCSS('pre', {"background-color": "whitesmoke", "margin-left": "0.1%"})
writeCSS('license', {"font-family":"'Oswald', sans-serif", "font-size":"30px"})
writeCSS('#pagelinks', {"font-family":"'Josefin Sans', sans-serif", "opacity":"0.8"})



# CONTENT

addFont("https://fonts.googleapis.com/css2?family=Titillium+Web&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Ubuntu&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Oswald&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@300&display=swap")

with image(src='white_sierra.JPG', attr='href="https://github.com/BrainStormYourWayIn/sierra", alt="Sierra"') as i:
    i.show()
    i.css(margin_left='35%')

head('Documentation - Sierra v2.3.0', 'h1', font_family="'Titillium Web', sans-serif", 
    color="#1d37e0")

openBody()

with div(None, attr="id='first_up'"):

    p(
    f'''Wecome to the documentation of Sierra - A skeletal micro templating library for Python. With Sierra, you 
    can develop your web applications purely in Python with simple and elegant syntax. You can use this along with another 
    templating engine, or use it standalone - even without a web framework, if you like. This is recommended to use 
    as an alternative to jinja or any other templating engine if you're developing web applications sans JS, since Sierra 
    doesn't have support for JS and even for very advaced usage (as of yet). This is relatively new, so features are being added at a quick pace. 
    If you have any specific requests, open a discussion/issue on our <a href="https://github.com/BrainStormYourWayIn/sierra">GitHub page</a>. 
    Any contributions can also be made there. <br>''')
    
    p(f'''Please read our <a href="https://github.com/BrainStormYourWayIn/sierra/blob/main/LICENSE">LICENSE</a> before moving forward''')


page_links = ['<a href="#tags">Using tags</a><br>', '<a href="#css-ing">Using CSS</a><br>', 
'<a href="#tTags">Working with div, section and p tags</a><br>', '<a href="#add_img">Adding images</a><br>', 
'<a href="#tables">Working with tables (Pandas supported)</a><br>', '<a href="#bullets_and_lists">Bulleted lists (ordered and unordered)</a><br>', 
'<a href="#des_lists">Adding a description list</a><br>', '<a href="#other_funcs">Other functions</a><br>']

with bullets(ul=True, points=page_links, attr="id='pagelinks'") as bt:
    pass


p("Let's get started")
with div(None, "id='starting_off'"):

    writeWA("\n<code>pip install sierra</code>")
    p(f'''can be done as an easier way of installing. You can see the README on the GitHub page for the <code> pip install git+git</code> method.
    <br><br>
    To import the library, simply use''')
    writeWA("\n<code>from sierra import *</code>")
    p("Once imported, the first line of syntax is mandatory: ")

    with Tag('pre'):
        writeWA(f'''
        
    title(Title, icon=False)

    # Args:
    # Title(str, compulsory)   : Title of the HTML file.
    # icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.

''')

    p(f'''You can add a header with <code>head()</code>. Of the arguments, either <code>type</code> or 
    <code>font_size</code> must be entered. Using both results in preference to <code>arg font_size</code> by CSS by default. 
    <br>Start the body of the web application with <code>openBody()</code>''')

    with Tag('pre'):
        writeWA(f'''

    head(Head, 
    type='header', font_size=False, font_family="Arial", color='black', text_align='left', background_color=False, 
    padding=False, height=False, width=False, line_break=False, line_height=False, border=False, margin=False)
    
    # head('Sierra', type='h1', color='#4287f5')

    # Head (str, compulsory)           : Caption header.
    # type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
    # color (str, optional)            : CSS Color (in any color code or name). Defaults to 'black'.
    # font_family (str, optional)      : CSS font-family. Defaults to Arial.
    # text_align (str, optional)       : CSS text-align parameter. left|right|center|justify|initial|inherit. Defaults to 'left'.
    # font_size (str, optional)        : CSS font-size parameter (in any valid measure). Leave blank, if not valid.
    # background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
    # padding (str, optional)          : CSS padding parameter. Defaults to False.
    # height (str, optional)           : CSS Height parameter. Defaults to False.
    # width (str, optional)            : CSS Width parameter. Defaults to False.
    # line_break (str, optional)       : CSS Line-break parameter. Defaults to False.
    # line_height (str, optional)      : CSS line-height parameter. Defaults to False. 
    # border (str, optional)           : CSS border parameter. Defaults to False.
    # margin (str, optional)           : CSS margin parameter. Defaults to False.


    openBody(
    background='False', background_color='white', background_image=False, opacity=False, background_size='cover', 
    background_attachment='fixed', background_position=False, background_repeat=False)

    # openBody()

        ''')

    p(f'''You may notice styling is a bit complicated with <code>head()</code> and <code>openBody()</code>, 
    but this method only applies to these tags. Styling gets much easier, especially with <code>.css()</code> and 
    <code>writeCSS()</code> or <code>writeCSS_raw()</code> for custom styling arguments. <br>''')
    p(f'''Fonts can be added with <code>addFont()</code> which takes only one argument, which is the link to the font.''')
    with Tag('pre'):
        writeWA(f'''
        
    addFont(font_link)

    # If you're using Google Fonts, take only the href attribute
    # If &lt;link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet">
    # is the the font tag to Roboto, take only the href attribute, then use
    
    # addFont("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap") 
     
    # You can then add "'Roboto', sans-serif" to the CSS as the font_family argument/font-family attribute, depending on the method 
    # of CSS used (See 'Using CSS')
      
        ''')



with div(None, attr="id='tags'"):
    with Tag('pg_title'):
        writeWA("Using tags")
    
    p(f'''Tags can be opened with <code>Tag('tag_name')</code>, and CSS can be added with <code>.css()</code>
    Any code within that tag can be entered with a context manager approach under <code>with</code>''')

    with Tag('pre'):
        writeWA(f'''
    
    with Tag('tag_name', attr=None) as t:
        t.css(font_color='rgb(11, 176, 89)')

        #  ---  Any content  ---  

        ''')
    p(f'''Coming out of <code>with</code> automatically closes the tag <br>
    <code>attr=None</code>, which is the second argument in <code>Tag()</code>, enables the user
    to add attributes to their HTML tag.''')
    with Tag('pre'):
        writeWA(f'''
    
    with Tag('tag_name', attr="class='someClass' id='some_id'") as t:

        t.css(font_color='rgb(11, 176, 89)')

        #  ---  Any content  ---  

        ''')
    p(f'''This is the equivalent of''')
    writeWA("<code>&lt;tag_name class='someClass' id='some_id'></code>")

    

with div(None, attr="id='css-ing'"):
    with Tag('pg_title'):
        writeWA('Using CSS')

    p(f'''There are four ways you can add CSS to tags. The first one is with <code>.css()</code>, which 
    takes in pre-defined styling arguments that are the most used ones, and can only be used within the context 
    manager of an open tag''')
    with Tag('pre'):
        writeWA(f'''
        
    .css( 
        color='black', font_family='Arial', font_weight=False, text_align=False, font_size=False, 
        background_color=False, background=False, margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, 
        border=False, display=False, padding=False, height=False, width=False, line_break=False, line_height=False, overflow=False, margin=False, box_shadow=False)
        
        ''')

    p(f'''The second way is to use <code>cTags()</code>. It is also a context manager based approach, but 
    there is more freedom, in the sense that any tag can be styled with this, and the context manager 
    does not have to be within another <code>with</code> to be executed. You can use this anywhere, provided 
    it comes after <code>title()</code>, which is a mandatory function.''')
    with Tag('pre'):
        writeWA(r'''
        
    with cTags(tag_name) as anything:
        anything.css()

    The pre-defined .css() arguments are the same as the arguments under the .css() which is bound to a specific 
    place in the document, except that color defaults to False instead of 'black' (To provide for image CSS in case an atribute like
    a class or an id is used)
        
        ''')

    p(f'''The third way is to use <code>writeCSS()</code>. It takes in a dictionary of CSS attributes, and adds 
    them to the tag mentioned as the first argument in <code>writeCSS().</code>''')
    with Tag('pre'):
        writeWA(r'''
        
    writeCSS(tag, *args)

    # *args takes in a dictionary of styling attributes

    # writeCSS('pre', {"background-color": "#edf7f7", "margin-left": "0.1%"})
    # This adds the specified CSS attributes in the dictionary to the tag &lt;pre>
        
        ''')

    p(f'''The fourth way to do this, is to use <code>writeCSS_raw()</code>. Any text you specify in <code>writeCSS_raw()</code> 
    gets written into the CSS file''')
    with Tag('pre'):
        writeWA(r'''
        
    writeCSS_raw(r"
    pre {
        background-color: #edf7f7;
        margin-left": "0.1%;
    }")
    
    # This writes the exact text in writeCSS_raw() to style.css
        ''')

with div(None, attr="id='tTags'"):
    with Tag('pg_title'):
        writeWA('Working with div, section and p tags')

    p(f'''Division and section tags can be opened the same way as <code>Tag()</code>, except the syntax is 
    <code>div()</code> and <code>section()</code> respectively, and the first arguments are their classes.
    CSS and tag attributes can be added the same way as any other tag, except that the first argument must 
    exist to add CSS. Or if you want to add CSS to the <code>id</code> attribute, use one of the four options 
    for CSS specified before, simply use <code>'#name_of_id'</code> as the tag name. The same applies to if 
    you want to use custom CSS attributes to the <code>class</code> attribute, use <code>'.class_name'</code> 
    as the name of the tag''')
    with Tag('pre'):
        writeWA(r'''
        
    div(div_class=None, attr=None)
    section(sec_class=None, attr=None)

    # with div(div_class='newClass') as d:
    #     d.css(background_color="#e0e330")
    #     with section(None, attr="id='some_id'"):
    #         p("This is a paragraph inside a section which is inside a div")

    # with cTags('#some_id') as styling_section_tag_with_id:
    #     styling_section_tag_with_id.css(margin_top='20px')
        
        ''')

    p(f'''<code>p</code> tags can be added with <code>p()</code>. The text to be added goes into 
    the <code>text</code> attribute, and tag attributes, as usual, can be added to <code>attr</code>. 
    However, <code>p()</code> is not a context manager based approach, as shown above under the section tag, and 
    closes upon argument exit''')
    with Tag('pre'):
        writeWA(r'''
        
    p(text, attr=None)

    # p('This is some text that goes inside a paragraph. Atrributes can be added to attr', attr="class='someClass'")
        
        ''')

with div(None, attr="id='add_img'"):
    with Tag('pg_title'):
        writeWA('Adding images')
    p(f'''Images can be added with <code>image()</code> as context manager based approach, <code>.show()</code> 
    which takes no arguments is used to display the image and <code>.css()</code> can be used to add CSS, or 
    one of the other three methods''')
    with Tag('pre'):
        writeWA(r'''
        
    image(src:str, href="False", attr=None)

    with image('sierra.jpg', "https://www.google.com", attr="alt='Sierra'") as i:
        i.show()
        i.css(opacity=1.1, width='50px')



    # margin_top (str, optional)       : CSS image margin-top parameter. Defaults to 'False'.
    # margin_bottom (str, optional)    : CSS image margin-bottom parameter. Defaults to 'False'.
    # margin_left (str, optional)      : CSS image margin-left parameter. Defaults to 'False'.
    # margin_right (str, optional)     : CSS image margin-right parameter. Defaults to 'False'.
    # border (str, optional)           : CSS image border parameter. Defaults to 'False'.
    # display (str, optional)          : CSS image display parameter. Defaults to 'block'.
    # height (str, optional)           : CSS image height parameter. Defaults to False.
    # width (str, optional)            : CSS image width parameter. Defaults to False.
    # margin (str, optional)           : CSS image margin parameter. Defaults to False.
    # vertical-align (str, optional)   : CSS image vertical-align parameter. Defaults to False.
    # opacity (int/float, optional)    : CSS image opacity parameter. Defaults to False.
    # filter (str, optional)           : CSS image filter parameter. Defaults to False.
        
        ''')

with div(None, attr="id='tables'"):
    with Tag('pg_title'):
        writeWA('Working with tables (Pandas supported)')

    p(f'''Adding a table could never have been easier with a context manager approach on <code>Table()</code>, which takes no arguments and 
    has objects <code>createTable()</code> and <code>getTable()</code>. 
    Sierra is compatible with Pandas, meaning just enter the path to the CSV file in <code>arg dataframe</code> 
    in <code>getTable()<code> , and the table will display!''')
    with Tag('pre'):
        writeWA(r'''
        
    getTable(self, dataframe:str, attr=None)

    with Table() as st:
        st.getTable("path/to/file.csv", attr=None)
        st.css(font_family='Times New Roman')


    # CSS styling arguments for getTable() and Table()

    .css(border=False, width=False, height=False, border_collapse=False, color='black',
    font_family="Arial", font_weight=False, text_align=False, font_size=False, margin=False,
    background_color='white')
        
        ''')
    p(f'''As mentioned, you can also add a table with <code>createTable()</code>''')
    with Tag('pre'):
        writeWA(f'''
        
    createTable(self, heads:list, rows:list, attr=None)

    # heads(list, compulsory): Adds table headers
    # rows(list, compulsory) : Takes in a list of lists, each list representing a row
    # attr(str, optional)    : Adds attributes to <table>

    with Table() as st:
        c = ['foo', 'foo1', 'foo2']
        r1 = ['united states', 'croatia', 'austria']
        r2 = ['czech', 'denmark', 'canada']
        r3 = ['netherlands', 'scotland', 'england']
        r = [r1, r2, r3]

        st.createTable(heads=c, rows=r, attr="id='table_id'")

    # Adding CSS

    with cTags('#table_id') as t:
        t.css(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')

        Output:
        
        ''')

    with Table() as st:
        c = ['foo', 'foo1', 'foo2']
        r1 = ['united states', 'croatia', 'austria']
        r2 = ['czech', 'denmark', 'canada']
        r3 = ['netherlands', 'scotland', 'england']
        r = [r1, r2, r3]

        st.createTable(heads=c, rows=r, attr="id='table_id'")
        
    with cTags('#table_id, th, td') as t:
        t.css(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')

with div(None, "id='bullets_and_lists'"):
    with Tag('pg_title'):
        writeWA('Bulleted lists (ordered and unordered)')

    p(f'''Ordered and/or unordered lists can be added with <code>bullets()</code> using <code>with</code>. 
    Just enter a list into the argument <code>points</code>, specify the type of the list (ordered or unordered), 
    attributes if necessary, and you're good to go. It doesn't have a <code>.css()</code> function - use one of the four methods 
    to add CSS to it''')
    with Tag('pre'):
        writeWA(r'''
        
    bullets(ul:bool, points:list, attr=None)

    a = ['pt1', 'pt2', 'pt3']
    b = ['pt4', 'pt5']
    c = ['pt6']

    with bullets(ul=False, points=a, attr="start='1' type='i'"):
        with bullets(True, b, attr="type='square'"):
            pass
    with bullets(ul=False, points=c, attr="start='4' type='I'"):
        pass
        
    Outputs:

        ''')

    a = ['pt1', 'pt2', 'pt3']
    b = ['pt4', 'pt5']
    c = ['pt6']

    with bullets(ul=False, points=a, attr="start='1' type='i'"):
        with bullets(True, b, attr="type='square'"):
            pass
    with bullets(ul=False, points=c, attr="start='4' type='I'"):
        pass

with div(None, attr="id='des_lists'"):
    with Tag('pg_title'):
        writeWA('Adding a description list')

    p(f'''Description lists can be added with <code>des_lists()</code>, which takes in argument <code>des_list</code> 
    and of course, attributes can be added with <code>attr</code>. Just enter in a list of lists as the 
    first argument, and it will show as a description list. It is not a context manager besed approach.''')
    with Tag('pre'):
        writeWA(r'''

    writeCSS('#d_list', {"margin-left":"40px"})

    a = [[['foo'], ['foo1', 'foo2']], [['py', 'py1'], ['PEP', 'PEP8']]]
    des_lists(a, "id='d_list'")


    Outputs:
        
        ''')

    writeCSS('#d_list', {"margin-left":"40px"})

    a = [[['foo'], ['- foo1', '- foo2']], [['py', 'py1'], ['- PEP', '- PEP8']]]
    des_lists(a, "id='d_list'")

    p(f'''Here, <code>[['foo'], ['- foo1', '- foo2']]</code> is the first description list, and 
    <code>[['py', 'py1'], ['- PEP', '- PEP8']]</code> is the second. These two are separated by commas and 
    are subsets of a list that contains them both. The attribute <code>id='d_list'</code> was added to the 
    description list, and CSS was added to the id with <code>writeCSS()</code>. 
    <br>So get careful with the list arrangement!''')

with div(None, attr="id='other_funcs'"):
    with Tag('pg_title'):
        writeWA('Other functions')

    p(f'''Python functions/variables or anything can be added onto the web application using Sierra with much 
    ease. However keep in mind, that every function/CSS/tag, or anything that is to be added to the HTML must 
    come only after <code>title()</code> <br>Here's a list of other functions you can use with Sierra: ''')
    with Tag('pre'):
        writeWA(r'''
        
    writeWA(text)
    # writeWA() can be used to add any text/code onto the web application. Here's an example: 

    with Tag('pre):
        writeWA(r"
    This appears inside the &lt;pre> tag
        ")

    # Or say you want to add some Bootstrap to your page:

    title()
    # Some CSS stuff for the HTML

    # Content starts from here

    #  addFont('Any font link(s)')
    #  Bootstrap link tags: 
    #  writeWA("\n"r'&lt;link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
    #  writeWA("\n"r'&lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
    #  writeWA("\n"r'&lt;script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
    

    Regular HTML escape sequences and glyphs and regular tags like &lt;a> can be used within the context manager
    or any functions that involve displaying on the web application, like

    p('HTML &lt;a href="some_link>tag&lt;a/> within a paragraph"')


    closeBody()
    # Closes the &lt;body> tag

    closeHTML()
    # Closes the &lt;html> tag

    autoPrettify()
    # It closes unclosed tags and improves overall look of the HTML code.
    # Use this at the end of all development outside all context managers. Using it inside or at a working 
    # stage will not work well
    # You can use this to avoid using closeHTML() and closeBody()

        
        ''')

with Tag('License'):
    writeWA('License')
with Tag('pre'):
    writeWA(r'''
        
See <a href="https://github.com/BrainStormYourWayIn/sierra/blob/main/LICENSE">LICENSE</a>

Pandas (pandas) -- table


Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
Copyright (c) 2011-2020, Open source contributors.
        
        ''')
    


autoPrettify()

