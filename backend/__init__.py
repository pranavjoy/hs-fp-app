def process_user_query(query_string):
    import urllib
    import webbrowser
    name_list = query_string.split(' ')
    greetings = []
    for name in name_list:
        if (name[0].isupper()==True):
            greetings.append(f'Hi {name}!\n')
    return greetings
    return 'No names found'
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    webbrowser.open_new(url)
