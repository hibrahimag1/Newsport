import PySimpleGUI as sg
import webbrowser
import News
import textwrap

sg.theme("Reddit")
sg.theme_button_color("#495452 on #a9d4cb")
sg.set_options(font=("Constantia", 16), background_color="#e1ede4", text_color="#495452", text_element_background_color="#e1ede4", scrollbar_color="#c7d4ca")
WINDOW_SIZE = (1300, 800)
ALL_URLS = []

def make_article_element(article_content: list):
    date = article_content[0]; title = textwrap.fill(article_content[1], 90); link = textwrap.fill(article_content[2], 130);
    article_column = [
        sg.Text(date, key='-DATE-', pad=((10, 5),(10,0)), auto_size_text=True), 
        sg.Text(title, key='-TITLE-', font=("Constantia", 18, "bold"), pad=((10, 5),(10,0)), auto_size_text=True),
        sg.Text(link, enable_events=True, tooltip="Klikni da odeš na stranicu", key=f'URL {link}', auto_size_text=True, font=("Constantia", 12, "italic"), pad=((130, 5),(0,20)))
    ]
    ALL_URLS.append(link)
    return article_column

def make_theme_window(number: int):
    clanci = News.get_news_on(number)
    lst = []
    for clanak in clanci:
        article_column = make_article_element(clanak)
        lst.append([article_column[0], article_column[1]]); lst.append([article_column[2]])

    lst.append([sg.Button("Nazad", key=f'-BTN{number}-', enable_events=True, size=(10, 2), auto_size_button=True, pad=((1100,0), (0,10)))])
    l = [[sg.Column(lst, scrollable=True, pad=(0,0), size=WINDOW_SIZE, vertical_scroll_only=True)]]
    return l

pozdrav = "Dobro došli na newsport, vaš personalni izbornik vijesti"
pitanje = "O čemu želite čitati danas?"
col1 = [  [sg.Text(pozdrav, enable_events=True, key="-TITLE-", font=("Constantia", 24), pad=((0,0), (150, 50)))] ]
col2 = [  [sg.Text(pitanje, enable_events=True, key="-SUBTIE2-", font=("Constantia", 18), pad=((0,0), (0, 150)))] ]
col3 = [
        [
        sg.Button("Zenica", key="-ZENICA-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Kultura", key="-KULTURA-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Zabava", key="-ZABAVA-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Politika", key="-POLITIKA-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Biznis", key="-BIZNIS-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        ],
        [
        sg.Button("Ljudi", key="-LJUDI-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Info", key="-INFO-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Crna hronika", key="-CRNAHRONIKA-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Sport", key="-SPORT-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        sg.Button("Licno", key="-LICNO-", enable_events=True, pad=((60, 60), (30,30)), size=(10, 2), auto_size_button=True),
        ]
]
l0 = [  
        [sg.Column(col1, justification="c", element_justification="c")],
        [sg.Column(col2, justification="c", element_justification="c")],
        [sg.Column(col3, justification="c", element_justification="c")],
     ]

# window za zenica tema
l1 = make_theme_window(1)
l2 = make_theme_window(2)
l3 = make_theme_window(3)
l4 = make_theme_window(4)
l5 = make_theme_window(5)
l6 = make_theme_window(6)
l7 = make_theme_window(7)
l8 = make_theme_window(8)
l9 = make_theme_window(9)
#l10 = make_theme_window(10)


'''l2 = [[sg.Text("Ovo je za Kulturu"), sg.Button("Nazad", key='-BTN2-')]]
l3 = [[sg.Text("Ovo je za Zabavu"), sg.Button("Nazad", key='-BTN3-')]]
l4 = [[sg.Text("Ovo je za Politiku"), sg.Button("Nazad", key='-BTN4-')]]
l5 = [[sg.Text("Ovo je za Biznis"), sg.Button("Nazad", key='-BTN5-')]]
l6 = [[sg.Text("Ovo je za Ljudi"), sg.Button("Nazad", key='-BTN6-')]]
l7 = [[sg.Text("Ovo je za Info"), sg.Button("Nazad", key='-BTN7-')]]
l8 = [[sg.Text("Ovo je za CHr"), sg.Button("Nazad", key='-BTN8-')]]
l9 = [[sg.Text("Ovo je za Sport"), sg.Button("Nazad", key='-BTN9-')]]'''

l10 = [[sg.Text("Ovo je za Licno"), sg.Button("Nazad", key='-BTN10-')]]

layout = [  
            [sg.Column(l0, key='-COL0-'), 
            sg.Column(l1, visible=False, key='-COL1-'),
            sg.Column(l2, visible=False, key='-COL2-'),
            sg.Column(l3, visible=False, key='-COL3-'),
            sg.Column(l4, visible=False, key='-COL4-'),
            sg.Column(l5, visible=False, key='-COL5-'),
            sg.Column(l6, visible=False, key='-COL6-'),
            sg.Column(l7, visible=False, key='-COL7-'),
            sg.Column(l8, visible=False, key='-COL8-'),
            sg.Column(l9, visible=False, key='-COL9-'),
            sg.Column(l10, visible=False, key='-COL10-')]
        ]


window = sg.Window("Newsport", layout, size=WINDOW_SIZE, finalize = True)

for url in ALL_URLS:
    window[f'URL {url}'].set_cursor("hand2")


TEME = {}
for i,v in enumerate("ZENICA KULTURA ZABAVA POLITIKA BIZNIS LJUDI INFO CRNAHRONIKA SPORT LICNO".split(), 1):
    s = f'-{v}-'
    TEME[s] = i

l = 0
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if TEME.get(event, -1) != -1:
        window.set_title("Newsport - " + event[1:-1].capitalize())
        window[f'-COL{l}-'].update(visible = False)
        l = TEME[event]
        window[f'-COL{l}-'].update(visible = True)
    elif event == f'-BTN{l}-':
        window[f'-COL{l}-'].update(visible = False)
        l = 0
        window[f'-COL{l}-'].update(visible = True)
        window.set_title("Newsport")
    elif event.startswith("URL "):
        webbrowser.open(event.split(' ')[1])




window.close()

'''Garbage code:
l1 = [*[*make_article_element(i) for i in clanci_zenica], [sg.Button("Nazad", key='-BTN1-')]]

'''