import subprocess
import re


domens = [
    'Google.com',
    'YouTube.com',
    'Facebook.com',
    'Instagram.com',
    'X.com',
    'Yandex.ru',
    'Wikipedia.org',
    'Yahoo.com',
    'Reddit.com',
    'Amazon.com'
]

with open('t1.csv', 'w') as file:
    file.write('IP_address,bytes,RTT,TTL\n')

for i in range(10):
    output = subprocess.run(['ping', domens[i], '-n', '1'], \
                            capture_output=True, \
                            text=True, \
                            encoding='cp866').stdout
    print(output)

    second_str = output.split('\n')[2]
    params = re.findall(r'[0-9.]+', second_str)
    if len(params) != 4:
        params = ['Error']
    
    with open('t1.csv', 'a') as file:
        file.write(','.join(params) + '\n')