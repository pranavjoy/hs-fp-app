import urllib
def process_user_query(query_string):
    name_list = query_string.split(' ')
    greetings = []
    for name in name_list:
        if (name[0].isupper()==True):
            greetings.append(f'Hi {name}!\n')
    return greetings
    return 'No names found'

fun open():
    return urllib.urlopen('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
