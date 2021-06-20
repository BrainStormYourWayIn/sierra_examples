from sierra import *

c = '<code>'                                            # As mentioned in the documentation, Python variables can be used in f-strings to be displayed on the 
cc = '</code>'                                          # web application.

if __name__ == "__main__":

    title('Documentation - Sierra -- 1.0.1')
    addFont(font_link='https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap')
    x = addImg(src="white_sierra.JPG", alt="Sierra logo_white", img_class="logo", href="https://github.com/BrainStormYourWayIn/sierra")
    x.show()
    x.css(margin_left='35%', margin_top='0px')
   

    a = tTags(True)
    a.css(color='black', font_family="'Roboto Mono', monospace")

    head('Documentation - Sierra -- 1.0.1', font_size='30px', color='blue', text_align='left', font_family="'Prompt', sans-serif")
    openBody(background_color='white', opacity=0.8)    
    openTags('pg_title')
    n = cTags('pg_title')
    n.css(font_family="'Prompt', sans-serif", font_size="20px", margin_top='10px')
    writeHTML('Working with Python Outputs')
    closeTags('pg_title')
    

    m = tTags(div_class='py_outputs')
    m.start_div()

    a.start_p(f""" Displaying Python outputs on your web applications are actually pretty simple with
    Sierra. To work with this, you can use <code>'writeHTML()'</code>, which has been covered on the
    main page of the documentation. Using f-strings is an easier way to print variables onto your
    work. <code>writeHTML(f'''{{var}}''')</code> or <code>a.start_p(f'''{{var}}''')</code>, both 
    work.{b}{b} Say you've used <code>getTable()</code> to load in
    a .csv file with pandas and write some quick code for displaying each row as a list:""", True)
    
    openTags('pre')
    text = r"""
  
        this      is        a          csv
    0   word      word1     word2      word3
    1   test1     test2     test3      test4
    2   foo1      foo2      foo3       foo4

    for i in range(0, 3):
    for g in range(1, 4):
        if i+1==g:
            a = f'''r{g} = {list(df.iloc[i])}{b}'''            # var 'b' stands for &lt;br> See 'Other Functions'
            writeHTML(a)
            # or if you want it on a paragraph
            a = tTags(True)
            a.start_p(a)

            Output:
            # r1 = ['word', 'word1', 'word2', 'word3']
            # r2 = ['test1', 'test2', 'test3', 'test4']
            # r3 = ['foo1', 'foo2', 'foo3', 'foo4']

        """

    writeHTML(text)
    writeCSS('pre', {"font-size": "15px", "background-color": "whitesmoke"})
    closeTags('pre')
    a.start_p(f'''The output is now displayed on the webpage! Of course, you can style it
    the way you want depending on the tag you enclosed it in.''', True)
    closeTags('div')
    autoPrettify()
    
