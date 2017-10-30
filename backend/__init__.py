def process_user_query(query_string):
    name_list = query_string.split(' ')
    greetings = []
    for name in name_list:
        greetings.append(f'Hi {name}!')
    # result = 'Hi There, Pranav \nHi There, Joy'
    return greetings
