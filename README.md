# CYPHER

Cypher é um prejeto de caça ao tesouro que fiz para meus amigos concorrerem a R$10 em créditos na steam.
(Criado no dia 12/02/2022)

### Como funciona?

- O objetivo do jogo era encontrar 7 chaves escondidas em seu computador.
- Quando enviei aos meus amigos, estava contido no arquivo zip o EXE do jogo e um .env com as chaves
- Ao abrir o exe pela primeira vez, 7 chaves eram escondidas em diversos locais de seu computador, podendo estar em forma de texto, imagem, som, etc.
- No menu do exe, havia uma opção de decodificar, que quando digitada junto das 7 chaves em ordem correta, fazia com que o gift code de 10 Reais aparecesse

_O código final era:_

```
1JKBDGTTP2MOOLAHHH3GOLDMINE4JHWBMIOP5DIAMONDD6PISSBABY7KLIPKLIP
```

#

_Notas:_

- Como o arquivo .env não existe mais, as chaves não serão escondidas em seu computador, mas ainda pode-se abrir o exe e usar a função decodificar.
- As chaves seriam escondidas desta forma:
  -- A primeira chave era escondida na mesma pasta em que o exe foi executado, na forma de um arquivo oculto .txt
  -- A segunda chave era escondida na mesma pasta da steam (steam.exe), programa que sabia que todos os meus amigos tinham instilado.
  -- A terceira chave era disfarçada de um arquivo .rar na pasta downloads, se o jogador tentasse abril-lo como arquivo winrar normalmente um erro ocorreria, mas se o jogador abrisse o arquivo em um bloco de nota, a chave apareceria.
  -- A quarta chave estava escrita em uma imagem salva na pasta "Imagens".
  -- A quinta chave estava escondida dentro da imagem da chave quatro, e foi a mais difícil de ser encontrada, o jogador tinha que abrir a imagem em um bloco de nota e descer até o final do arquivo para achá-la.
  -- A sexta chave era escondida na pasta "Músicas", contendo um audio de uma voz robotizada (tts) falando algumas letras aleatórias seguidas da chave.
  -- A sétima chave era escondida no meio de um pdf de 4500 letras aleatórias, localizada na pasta "Documentos"
