#split query
def process_user_query(query_string):
    name_list = query_string.split(' ')

#convert split query to string

def convert_to_string(student_names):
    result =''
    for name in name_list:
        result = result + ' ' + name

#add greeting to split query
name_list2 = convert_to_string(student_names)
result = f'Hi There, {name_list2}'
return result
