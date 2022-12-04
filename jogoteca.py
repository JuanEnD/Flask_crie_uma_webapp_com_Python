from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Hollow Knight', 'Indie', 'PC/Consoles')
    jogo3 = Jogo('Valorant', 'FPS', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


# app.run()

app.run(host='0.0.0.0', port=8080)

'''
Observação: não utilizar estas definições para produção, 
estas opções foram preparadas para ajudar no ambiente de desenvolvimento.

app.run(host='0.0.0.0', port=8080)
'''