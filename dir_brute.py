from requests_html import HTMLSession

session = HTMLSession()

dirs = ['/',
 'news',
 'news/article?id=1',
 'news/article?id=1',
 'contact',
 'customers',
 'customers/login.',
 'customers/login',
 'customers/signup',
 'customers/reset',
 'customers',
 'customers/ticket/new',
 'customers/account',
 'customers/logout']

def brute_force(target, directory_list):
    for directory in directory_list:
                
        r = session.get(f'{target}/{directory}')
        print(r)

