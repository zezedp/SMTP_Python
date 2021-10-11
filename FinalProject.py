import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def destinatario():
    """
    Essa função retorna o e-mail do destinatário ou os e-mails listados;
        -> list
    """
    contador = 1
    email_temp = []
    usar_arquivo = input('1: Para digitar manualmente o e-mail destinatário \n2: para digitar o caminho do arquivo de texto .txt com os e-mails (um e-mail por linha):\n')
    if usar_arquivo == '1':
        n_destinatarios = input('Digite o número de pessoas para quem você quer enviar o e-mail: ')
        while contador <= int(n_destinatarios):
            email_input = input('Digite o e-mail do destinatário: ')
            email_temp.append(email_input)
            contador += 1
        email = ','.join(email_temp)
    elif usar_arquivo == '2':
        caminho = input('Digite o caminho do arquivo: ')
        arquivo_com_emails = open(caminho, encoding='utf8')
        conteudo = arquivo_com_emails.read()
        email_list = conteudo.split('\n')
        arquivo_com_emails.close()
        email = ','.join(email_list)
    return email


def host_port():
    """
    Essa função retorna o server,  a partir do domínio escolhido pelo usuário, ou se ocorrou um erro no host e/ou port;
    """
    dominio = input('Qual o seu dominio?\n Digite 1: Gmail\n Digite 2: Outlook, Hotmail ou Microsoft365\n Digite 3: Yahoo\n Digite 4: MSN\n Digite 0: Não encotrei meu domínio\n')
    if dominio == '1':
        host = 'smtp.gmail.com'
        port = '587'
    elif dominio == '2':
        host = 'smtp.office365.com'
        port = '587'
    elif dominio == '3':
        host = 'smtp.mail.yahoo.com'
        port = '465'
    elif dominio == '4':
        host = 'smtp-mail.outlook.com'
        port = '587'
    elif dominio == '0':
        host = input('Insira o servidor SMTP do seu domínio. Essa informação é encontrada facilmente no Google.')
        port = input('Agora, insira a porta de saída do servidor SMTP do seu domínio.')
    try:
        server = smtplib.SMTP(host, port)
    except Exception as e:
        err = 'O servidor não foi encontrado. Algo está errado com host ou porta, verifique se foram digitados novamente.\nErro: {}'.format(str(e))
        return err
    return server


def main():
    """
    Essa função retorna o erro ou se o e-mail foi enviado com sucesso;
        -> str
    """
    login = input(str('Insira o seu e-mail: '))
    senha = input(str('Agora digite sua senha: '))
    assunto = input(str('Digite o assunto do e-mail: '))
    corpo = input(str('Digite o corpo do e-mail: '))
    server = host_port()
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = destinatario()
    email_msg['Subject'] = assunto
    try:
        server.ehlo()
        server.starttls()
    except Exception as e:
        err = 'Algo inesperado aconteceu.\nErro: {}'.format(str(e))
        return err
    try:
        server.login(login, senha)
    except Exception as e:
        err = 'Os dados inseridos estão incorretos. Verifique se o login e senha foram digitados corretamente.\nErro: {}'.format(str(e))
        return err
    email_msg.attach(MIMEText(corpo, 'plain'))
    try:
        server.sendmail(email_msg['From'], email_msg['To'].split(','), email_msg.as_string())
    except Exception as e:
        err = 'Não foi possível enviar o e-mail.\nErro: {}'.format(str(e))
        return err
    finally:
        server.quit()
        return 'As mensagens foram enviadas com sucesso.'

print(main())