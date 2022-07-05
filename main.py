
# LER EXPLICACAO DO PROGRAMA NA README.md #

from tkinter import Image
from pyfiglet import figlet_format, fonts
import os
import onetimepad
from dotenv import load_dotenv
from tqdm import tqdm
import time
from getpass import getuser
from pathlib import Path
from PIL import Image, ImageDraw
from gtts import gTTS
from fpdf import FPDF
import random
import pathlib
import shutil

# Carrega a .env que contem todas as chaves, e a informacao da primeira vez que roda
load_dotenv('env\\.env')

# Atribui firstTime ao FIRST_TIME da .env, sendo ele TRUE
firstTime = bool(os.getenv('FIRST_TIME'))

# Se for a primeira vez abrindo o programa, esconde as chaves
if firstTime == True:
    os.system('cls')

    # Pega o PATH atual
    path = pathlib.Path().resolve()
    path = path.joinpath('env')

    # PRIMEIRA CHAVE
    try:
        with tqdm(total=100, desc='Escondendo chave 1...') as pbar:

            # Cria um arquivo chamado cypher.txt e escreve a primeira chave nele
            with open('cypher.txt', 'w+') as one:
                one.write(os.getenv('KEY1'))
                pbar.update(20)

            pbar.update(20)

            # Torna o arquivo Hidden
            os.system('attrib +h cypher.txt')

            pbar.update(40)
            time.sleep(1)
            pbar.update(20)
        pbar.close()
        print('Chave 1 escondida!')
        print('\n')

    # Se nao conseguir esconder a chave, é porque ela ja está la
    except:
        PermissionError
        print('Chave já escondida!')

    # SEGUNDA CHAVE

    def sec():
        with tqdm(total=100, desc='Escondendo chave 2...') as pbar:

            # todo esse loop tenta achar steam.exe nos arquivos
            # um programa que eu sei que todos meus amigos tinham
            # e esconde um txt na mesma pasta do exe

            for r, d, f in os.walk("C:\\"):
                for files in f:
                    if files == "steam.exe":
                        pbar.update(40)
                        steamFolder = (os.path.join(r, files)
                                       ).replace('steam.exe', '')
                        pbar.update(30)
                        with open(steamFolder + '#C1PH3R.txt', 'w+') as two:
                            two.write(os.getenv('KEY2'))
                        pbar.update(30)
                        print('Chave 2 escondida!')
                        print('\n')
                        return
    try:
        sec()
    except:
        PermissionError
        print('Chave já escondida!')

    # TERCEIRA CHAVE
    def terc():

        # a terceira chave é escondida assim:
        # cria um arquivo txt
        # coloca a chave dentro dele
        # transforma em .rar pra disfarçar

        user = getuser()
        with tqdm(total=100, desc='Escondendo chave 3...') as pbar:
            if os.path.exists('C:\\Users\\'+user+'\\Downloads\\sifer.rar'):
                pbar.update(100)
                pbar.close()
                return
            else:
                with open('C:\\Users\\'+user+'\\Downloads\\sifer.txt', 'w+') as sifer:
                    pbar.update(30)
                    sifer.write(os.getenv('KEY3'))
                    pbar.update(20)
                p = Path('C:\\Users\\'+user+'\\Downloads\\sifer.txt')
                pbar.update(30)
                p.rename(p.with_suffix('.rar'))
                pbar.update(20)
                os.unlink('C:/Users/'+user+'/Downloads/sifer.txt')
        pbar.close()

    print('Chave 3 escondida!')
    print('\n')

    try:
        terc()
    except:
        PermissionError
        print('Chave já escondida!')

    # CHAVE QUATRO E CINCO
    def quarCinc():

        # A chave 4 é escrita em uma imagem usando o PIL
        # A chave 5 é escrita na imagem quando abre em .txt
        # salva na pasta Imagens

        user = getuser()
        with tqdm(total=100, desc='Escondendo chave 4...') as pbar:
            img = Image.new('RGB', (200, 200), color='black')
            pbar.update(30)
            d = ImageDraw.Draw(img)
            pbar.update(20)
            d.text((75, 90), os.getenv('KEY4'),
                   fill='white')
            d.text((5, 180), 'there is more than meets the eye',
                   fill='white')
            pbar.update(30)

            # salva a imagem com a quarta chave
            img.save('C:\\Users\\'+user+'\\Pictures\\S41F3R.jpg', quality=100)

            # cria um arquivo temporario com a chave
            with open('C:\\Users\\'+user+'\\Pictures\\temp.txt', '+w') as temp:
                temp.write('\n\n------------\n')
                temp.write(os.getenv('KEY5'))
            pbar.update(10)
            os.chdir('C:\\Users\\'+user+'\\Pictures')

            # coloca a chave no final do codigo do jpg
            # da pra achar ela abrindo o jpg como txt

            os.system('copy /b S41F3R.jpg + temp.txt S41F3R.jpg')
            os.remove('temp.txt')
            pbar.update(10)

            print('Chave 4 escondida!')
            print('\n')
            print('Chave 5 escondida!')
            print('\n')
    try:
        quarCinc()
    except:
        PermissionError
        print('Chave já escondida!')

    # SEXTA CHAVE

    def seis():

        # A sexta chave é um arquivo de audio, com uma voz robotizada que fala
        # umas letras aleatorias e o codigo no meio
        # e salva na pasta Music

        user = getuser()
        with tqdm(total=100, desc='Escondendo chave 6...') as pbar:
            keylist = []
            pbar.update(30)
            keylist[:0] = os.getenv('KEY6')
            commaKeyList = ",".join(keylist)
            pbar.update(30)
            text = 'K, J, A, R, B,' + commaKeyList + ', G, J, W, S, S, S'
            tts = gTTS(text, lang='pt-br')
            pbar.update(30)
            try:
                tts.save('C:\\Users\\'+user+'\\Music\\cfer.mp3')
            except FileNotFoundError:
                tts.save('C:\\Users\\'+user+'\\cfer.mp3')
            pbar.update(10)
            print('Chave 6 escondida!')
            print('\n')
            return

    # SÉTIMA CHAVE

    def sete():

        # a sétima chave é escondida em um pdf de ~5000 letras
        # ela está no meio
        # é escondida na pasta documentos

        user = getuser()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=15)
        alphabet = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

        pdfText = ''
        for i in range(2500):
            pdfText = pdfText + random.choice(alphabet)
        pdfText = pdfText + os.getenv('KEY7')
        for i in range(2000):
            pdfText = pdfText + random.choice(alphabet)
        pdf.multi_cell(0, 10, pdfText)
        pdf.output('C:\\Users\\'+user+'\\Documents\\simfer.pdf')

    sete()
else:
    print('Nenhuma dotEnv encontrada!')


############

# GUI

os.system('cls')
cols = 90
os.system('mode con: cols=' + str(cols) + ' lines=40')

choice = ''

try:
    shutil.rmtree(path)
except NameError:
    print('Removed')


# funcao main roda toda a gui

def main():

    # o menu funciona assim:
    # voce tem dois comandos: ajuda e decodificar
    # quando vc escreve ajuda, vai para o menu de ajuda
    # quando escreve decodificar, o programa tenta decodificar suas chaves
    # as chaves devem ser inseridas da forma explicada no menu de ajuda

    def mainMenu():
        os.system('cls')
        welcome = figlet_format(
            '\n         C Y P H E R', font='alligator2')

        print(welcome)

        print('By yut videogame'.center(cols))
        print('\n')
        print('Comandos: ajuda, decodificar'.center(cols))
        print('\n')
        global choice
        choice = input(' /')
        return choice

    # menu de ajuda

    def helpMenu():
        os.system('cls')
        print('\n')
        print('Bem vindo a Cypher!'.center(cols))
        print('\n')
        print('Nesse jogo você pode ganhar R$10 na steam apenas navegando seu computador.'.center(cols))
        print('\n')
        print('Como funciona?'.center(cols))
        print('\n')
        print('Se você está lendo isto, você já está jogando!'.center(cols))
        print('Pouco antes de seu computador reiniciar, 7 chaves foram escondidas nele.'.center(cols))
        print('Elas podem estar escondidas em qualquer lugar (arquivos, pastas, documentos, ...),'.center(cols))
        print('e seguem um formato simples, exemplo: 1ABCDEFGH.'.center(cols))
        print('Todas as chaves contém um número índice seguido de 8 letras em caixa-alta.'.center(cols))
        print('O número indica a ordem que a chave deve ser colocada, exemplo: 1ABCDEFGH 2IJKLMNOP.'.center(cols))
        print('\n')
        print('Como inserir as chaves?'.center(cols))
        print('\n')
        print('Para inserir as chaves volte ao menu principal e digite: "decodificar CHAVES"'.center(cols))
        print('Ex.: decodificar 1ABCDEFGH 2IJKLMNOP'.center(cols))
        print('\n')
        print('Tire uma print de cada chave quando achar, para caso ocorra algum bug.'.center(cols))
        print('Qualquer outra dúvida, mande mensagem para o yut.'.center(cols))
        print('\n')
        print('Boa sorte!'.center(cols))
        print('Pressione enter para voltar...'.center(cols))
        input()

    # decodificar usa o onetimepad
    # o onetimepad é um tipo de codificaçao onde eu providencio o hash
    # e ele e decodificado com base nas chaves
    # a chave de decodificação são todas as 7 chaves uma do lado da outra

    def decodificar(key):
        return onetimepad.decrypt('6177767f790169696d0f157272717c1875750e7a0d7179707404780977751a7f707472640879747c03727379797a6d746e6e157c7f640a0d71746d7601746d0c77797f797a691d', key)

    mainMenu()

    # se for ajuda, roda o menu de ajuda

    if (choice.startswith('ajuda')):
        os.system('cls')
        helpMenu()
        os.system('cls')
        mainMenu()

    # se for decodificar, roda o decodificar

    elif(choice.startswith('decodificar')):
        codificado = choice[11:].strip().replace(' ', '')
        print('\n')
        print(decodificar(key=codificado).center(cols))
        print('\n')
        input('Pressione enter para inserir um novo comando.'.center(cols))


while True:
    main()
