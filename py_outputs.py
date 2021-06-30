from sierra import *

title('Documentation | Sierra - 2.0.0')

# writeWA("\n"r'<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
# writeWA("\n"r'<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
# writeWA("\n"r'<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')


# CSS

with cTags('p') as p_tag:
    p_tag.css(font_family="'Ubuntu', sans-serif;", line_height='28px')
with cTags('pg_title') as pg_title:
    pg_title.css(font_family="'Signika Negative', sans-serif", font_size='25px', margin_top='30px', display='block')
writeCSS('pre', {"background-color": "whitesmoke", "margin-left": "0.1%"})


# CONTENT

addFont("https://fonts.googleapis.com/css2?family=Titillium+Web&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Ubuntu&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Oswald&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap")
addFont("https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@300&display=swap")

with image('white_sierra.JPG', attr='href="https://github.com/BrainStormYourWayIn/sierra" alt="Sierra"') as i:
    i.show()
    i.css(margin_left='35%')

head('Documentation - Sierra v2.0.0', type='h1', font_family="'Titillium Web', sans-serif", 
    color="#1d37e0")
openBody()

with div(div_class='python_out'):
    with open_tag('pg_title'):
        writeWA('Working with Python Loops, Functions, Variables and Conditions')
    
    p(r'''Displaying Python outputs on your web applications are actually pretty simple with Sierra. 
    To work with this, you can use <code>writeWA()</code> or <code>p()</code> , which has been covered on the main page of the 
    documentation. You can print variables, output functions, use loops, conditions or anything.''')

    p(f'''Say you've loaded in a .csv file with pandas and write some quick code for displaying 
    each row as a list: ''')

    with open_tag('pre'):
        writeWA(r'''
        
    import pandas as pd
    from sierra import *

    df = pd.read_csv('path/to/the/file.csv')
    df

        this      is        a          csv

    0   word      word1     word2      word3
    1   test1     test2     test3      test4
    2   foo1      foo2      foo3       foo4

    for i in range(0, 3):
        for g in range(1, 4):
            if i+1==g:
                a = f'r{g} = {list(df.iloc[i])}{br}'       # var 'br' stands for &lt;br> See 'Other Functions'
            
                writeWA(a)

                # or if you want it on a paragraph

                p(a)



        # Output on the web application:
        # r1 = ['word', 'word1', 'word2', 'word3']
        # r2 = ['test1', 'test2', 'test3', 'test4']
        # r3 = ['foo1', 'foo2', 'foo3', 'foo4']
        
        ''')

with div(div_class='img-map'):

    p(f'''Say you want to create an image map, with which you can perform different actions by clicking on 
    shape and subsequently coordinate-secified parts of the shape on the image. {br}
    See <a href="https://www.w3schools.com/html/html_images_imagemap.asp" target='blank'>image map</a>. 
    You can use f-strings and <code>for loop</code> to make it easy: ''')

    with open_tag('pre'):
        writeWA(r'''

    with image(src='workplace.jpg', attr="usemap='#workmap'") as i:
        i.show()

    with open_tag('map', attr='name="workmap"'):
        shape = ['rect', 'rect', 'circle']
        coords = ["34,44,270,350", "290,172,333,250", "337,300,44"]
        alt = ['Computer', 'Phone', 'Coffee']
        href = ['computer.htm', 'phone.htm', 'coffee.htm']

        for shape, coord, alt, href in zip(shapes, coords, alt, href):
            with open_tag('area', attr=f'shape="{shape}" coord="{coord}" alt="{alt}" href="{href}"'):
                pass

    autoPrettify()

        ''')
    p(f'''Here, you first display the image and give it an attribute <code>usemap</code>, then you enter in four lists 
    that contain the attributes of the three areas to be covered, open the &lt;map> tag and map it to the 
    attribute <code>usemap</code> given to the image. Then you do a simple for loop and 
    unpack each item in the lists with <code>zip()</code>, open the &lt;area> tag and simply use 
    f-strings to enter in four different attributes to three different &lt;area> tags which all come under &lt;map>! 
    So instead of manually entering in every single tag and attribute, you've used Python's <code>list</code> 
    and <code>for loop</code> to get the job done.''')

with div(div_class='funcs'):

    p(f'''With Sierra, using and displaying outputs of Python functions on your web application
    is made easy as cake''')
    p(f'''Here's an example of scraping a webpage with requests, given it's URL, and displaying 
    all text within the &lt;p> tag: ''')

    with open_tag('pre'):
        writeWA(r'''
        
    from sierra import *
    import re
    import urllib3

    def ExtractpText(url):

        http = urllib3.PoolManager()
        req = http.request('GET', url)
        respData = RemoveThrashText(str(req.data))
        regex = '&lt;p>(.*?)&lt;/p>'
        paragraphs = re.findall(regex, respData)
        return paragraph

    title('Extracting text from the &lt;p> tag given a URL')
    openBody()

    writeWA("\n"ExtractpText("http://example.com/"))

    autoPrettify()


    # OR you could enclose it in a div/p/section/anything and style it, if you like


    title('Extracting text from the &lt;p> tag given a URL')

        # Font
    addFont("https://fonts.googleapis.com/css2?family=Roboto&display=swap")

    openBody(background_color="#161a21")

    p(writeWA("\n"ExtractpText("http://example.com/")), attr="class='p_class'")

        # CSS
    with cTags('.p_class') as p_class:
        p_class.css(color="#dfe3eb", font_family="'Roboto', sans-serif")

    autoPrettify()

        
        ''')

    p(f'''Simple as that! You just use <code>writeWA()</code> for getting the job done!
    {br} Or you could just do <code>p(ExtractpText("http://example.com/"))</code>, both work''')
    p(f'''Similarly, variables and conditional statements can be added too''')

    with open_tag('pre'):
        writeWA(r'''
        
    some_variable = 'doggo'

    p(doggo)

    # or use f-strings

    p(f'This is my {some_variable}!')

    # or use writeWA (even with f-strings, if the use case suits you)

    if some_variable == 'dog':
        writeWA(f'Grrr! This is NOT my {some_variable}')
    else:
        writeWA(f'Grrr! This is MY {some_variable}! I'd like you to come just a little closer.')

        
        ''')



autoPrettify()

# import webbrowser as wb
# wb.open('index.html')
