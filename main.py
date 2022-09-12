import sqlite3
from time import sleep
from segredo import passw
pw_god = passw
try:
    senha = str(input('Insira sua senha: '))
    if senha != pw_god:
        print('\033[31mSenha inválida! Encerrando...\033[m')
        sleep(3)
        exit()
except (ValueError, TypeError):
    print('Preencha tudo de forma correcta!')
conexão = sqlite3.connect('pw.db')
cursor = conexão.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print('~'*45)
    print('Escolha uma das opções: '.center(45))
    print('''           1 - Inserir nova senha
           2 - Listas senhas salvas
           3 - Recuperar senha
           4 - Sair'''.center(45))
    print('~'*45)

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print('Serviço não cadastrado, use 1 para novos serviços!')
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}')''')
    conexão.commit()

def show_service():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    try:
        menu()
        opc = int(input('Escolha uma das opções acima: '))
        if opc not in [1, 2, 3, 4]:
            print('Opção inválida!')
            continue
        if opc == 4:
            break
        if opc == 1:
            service = str(input('Serviço: '))
            user = str(input('Username: '))
            senha = str(input('Senha: '))
            insert_password(service, user, senha)
        if opc == 2:
            show_service()
        if opc == 3:
            service = str(input('Qual serviço para qual quer senha: '))
            get_password(service)
    except (ValueError, TypeError):
        print('Preencha tudo correctamente, não deixe nada vazio, nem com opções inexistentes na lista')
conexão.close()
