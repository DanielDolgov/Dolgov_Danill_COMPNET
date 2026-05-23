import subprocess


import pandas as pd


def DNS(domain):
    ip = subprocess.run(
        ["nslookup", domain],
        capture_output=True,
        text=True,
        timeout=10
    ).stdout.split()[-1]

    return ip


def traceroute(ip):
    traceroute = subprocess.run(
        ["tracert", "-d", "-h", "50", "-w", "1000", ip],
        capture_output=True,
        text=True,
        timeout=300,
        encoding="cp866"
    ).stdout.strip()

    return traceroute


def fill_csv():
    domains = ['google.com', 'github.com', 'cccstore.ru', 'yandex.ru', 'kaggle.com']
    df = []
    for domain in domains:
        ip = DNS(domain)
        df.append([domain, ip, traceroute(ip)])
        print(f'Трассировка {domain} завершена.')

    pd.DataFrame(df, columns=['domain', 'ip', 'traceroute']).to_csv('traceroute.csv', index=None)


fill_csv()