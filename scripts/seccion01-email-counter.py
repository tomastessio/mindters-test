import re

def email_counter(file):
    reg_exp = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'    
    counter = 0
    with open(file, 'r') as file:
        for line in file:
            coincidences = re.findall(reg_exp, line)
            counter += len(coincidences)
    return counter

file_name = 'mails.txt'
print(f'Número de correos electrónicos válidos: {email_counter(file_name)}')