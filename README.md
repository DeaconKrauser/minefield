# Minesweeper em Python
<p>Este é um jogo de campo minado em Python utilizando a biblioteca PyQt5 para interface gráfica.</p>

## 💻 Instalação
<p>Instale o Python em sua máquina se ainda não tiver instalado (pode ser encontrado em <a href=“http://exemplo.com/“>https://www.python.org/downloads/</a>).</p>
<p>Instale a biblioteca PyQt5 através do seguinte comando no terminal/cmd:</p>

    pip install PyQt5
    
<p>Baixe o arquivo com o código-fonte do jogo.</p>

___
## 📥 Baixando o código
Clique no botão <b>"Clone or download"</b> e depois em <b>"Download ZIP"</b>. Descompacte o arquivo baixado e abra o arquivo <b>"minefield.py"</b> no seu editor de código preferido.

___
## 🚀 Executando o jogo
Execute o arquivo <b>"minefield.py"</b> com o Python. O jogo irá abrir na tela.
___
## 🎮 Como jogar
O objetivo do jogo é descobrir todos os quadrados que não possuem minas. Clique em um quadrado para revelar o que há nele. Se o quadrado revelado tiver uma mina, o jogo acaba. Se não, um número será exibido indicando quantas minas há nos quadrados adjacentes.

___
## 💥 Alerta
Caso você clique em um quadrado com uma mina, o jogo acaba e todas as minas são reveladas.

___
## 🔁 Reiniciar
Para reiniciar o jogo, feche a janela e execute o arquivo "minefield.py" novamente.

___
## 💡 Como o código funciona
O código utiliza a biblioteca PyQt5 para criar a interface gráfica do jogo. Ele cria uma matriz de botões, cada um representando um quadrado no campo minado. Quando um botão é clicado, a função "reveal" é chamada, que verifica se a posição clicada contém uma mina ou não. Caso haja uma mina, a função "end_game" é chamada e todas as minas são reveladas. Se não houver uma mina, a função "count_mines" é chamada para contar quantas minas há nos quadrados adjacentes, e o número é exibido no botão clicado.