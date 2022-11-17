from requests_html import HTMLSession
session = HTMLSession()

def brute_force(target, directories):
    with open(directories, 'r') as dirs:
        for directory in dirs:
            directory = directory.strip() #avoid false 404 http status
            request = session.get(f'{target}/{directory}')
            print(request, f'{target}/{directory}')



