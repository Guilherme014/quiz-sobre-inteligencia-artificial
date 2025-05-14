import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.acertos = 0
        self.topo = 200
        self.esquerda = 200
        self.largura = 500
        self.altura = 600
        self.labelTituloImagem = QLabel(self)
        self.ImagemTitulo = QPixmap(resource_path('Titulo.png'))
        self.setWindowIcon(QIcon("robo.ico"))

        
       
        
        self.titulo = "Quiz de inteligência artificial"

        self.perguntas = [
    {"pergunta": "O que é inteligência artificial?", "opções": ["Um robô de brinquedo", "Tecnologia que aprende e pensa como gente", "Controle remoto moderno", "Um jogo de computador"], "resposta certa": "Tecnologia que aprende e pensa como gente"},
    {"pergunta": "Qual desses usa inteligência artificial?", "opções": ["Ventilador", "Bicicleta", "Celular com assistente de voz", "Televisão sem internet"], "resposta certa": "Celular com assistente de voz"},
    {"pergunta": "O que a inteligência artificial precisa para funcionar bem?", "opções": ["Água e comida", "Vento e sol", "Informações e exemplos para aprender", "Parafusos e rodas"], "resposta certa": "Informações e exemplos para aprender"},
    {"pergunta": "Onde a IA ajuda muito?", "opções": ["Pintar paredes", "Ajudar médicos com exames", "Cortar cabelo", "Jogar futebol"], "resposta certa": "Ajudar médicos com exames"},
    {"pergunta": "Qual é um problema da inteligência artificial?", "opções": ["Ela canta errado", "Pessoas podem perder o emprego", "Ela come muito", "Faz barulho demais"], "resposta certa": "Pessoas podem perder o emprego"},
    {"pergunta": "Como a IA ajuda o meio ambiente?", "opções": ["Mostra onde estão queimadas e desmatamentos", "Aumenta a poluição", "Quebra árvores", "Usa muita água"], "resposta certa": "Mostra onde estão queimadas e desmatamentos"},
    {"pergunta": "Como usar inteligência artificial com responsabilidade?", "opções": ["Mandar ela fazer tudo por você", "Usar com cuidado e proteger seus dados", "Compartilhar tudo com estranhos", "Mentir para a IA aprender mais"], "resposta certa": "Usar com cuidado e proteger seus dados"}
]
        random.shuffle(self.perguntas)
        self.indice_pergunta = 0
        
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        

        self.layout = QVBoxLayout()
        self.layoutBotoes = QGridLayout()
        self.labelTituloImagem.setPixmap(self.ImagemTitulo)
        
    
       

       
        self.labelTituloImagem.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.labelTituloImagem)


        self.label_acertos = QLabel(self)
        self.label_acertos.move(150, 150)
        self.label_acertos.resize(150, 150)
        self.label_acertos.setStyleSheet("font-size: 40px; font-weight: bold; margin-top: 20px;")
        self.label_acertos.setTextFormat(Qt.RichText)
        self.label_acertos.setText('Acertos: <span style="color: black;">0</span>')
        
        self.label_pergunta = QLabel(self)
        self.label_pergunta.setAlignment(Qt.AlignCenter)
        
        
        self.layout.addWidget(self.label_pergunta)
        self.layout.addWidget(self.label_acertos)




        self.botoes = []
        quantidade_opcoes = len(self.perguntas[self.indice_pergunta] ["opções"])
        for i in range(quantidade_opcoes):
            botao = QPushButton(self)
            botao.clicked.connect(self.verificar_resposta)
            self.botoes.append(botao)
            botao.setFixedSize(750, 95)
            
            linha = i // 2
            coluna = i % 2
            self.layoutBotoes.addWidget(botao, linha, coluna)

            botao.setStyleSheet("""
           QPushButton {
            background-color: #ffffff;
            font-size: 30px;
            border: 2px solid #000000;
            border-radius: 15px;
            padding: 10px ;
        }
        QPushButton:hover {
            background-color: #d6d4e0;
        }
    """)
        self.layout.addLayout(self.layoutBotoes)

        self.botao_reiniciar = QPushButton("Reiniciar quiz!")
        self.botao_reiniciar.hide()
        ##self.botao_reiniciar.move(215, 350)
        ##self.botao_reiniciar.resize(100, 100)
        self.botao_reiniciar.clicked.connect(self.reiniciarQuiz)
        self.botao_reiniciar.setStyleSheet("""
                   QPushButton {
                    background-color: #ffffff;
                    border: 2px solid #8c8a97;
                    border-radius: 10px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #7c8894; 
                }
            """)
        self.Label_recopensa = QLabel(self) 
        self.Label_recopensa.setText(f"voce acertou {self.acertos} de {len(self.perguntas)} perguntas! ")
        self.Label_recopensa.setStyleSheet("font-size: 15px; font-weight: bold; margin-top: 15px;")
        self.Label_recopensa.hide()
        self.layout.addWidget(self.Label_recopensa)
        self.Label_Pirulito = QLabel(self)
        self.Label_Pirulito.setStyleSheet("font-size: 40px; font-weight: bold; margin-top: 20px;")
        self.Label_Pirulito.hide()
        self.layout.addWidget(self.Label_Pirulito, alignment=Qt.AlignCenter)

        self.layout.addWidget(self.botao_reiniciar, alignment=Qt.AlignCenter)
        
        
        
        self.widget.setLayout(self.layout)
       
        
       


        self.carregar_pergunta()
        self.carregar_janela()

    def carregar_pergunta(self):
        if self.indice_pergunta < len(self.perguntas):
            pergunta_atual = self.perguntas[self.indice_pergunta]
            self.label_pergunta.setText(pergunta_atual["pergunta"])
            self.label_pergunta.setStyleSheet("font-size: 50px; font-weight: bold; ")
            

            
            self.opcoes_atuais = list(pergunta_atual["opções"])
            random.shuffle(self.opcoes_atuais)

            for i, botao in enumerate(self.botoes):
                botao.setText(self.opcoes_atuais[i])
                botao.show()
        else:
            self.label_pergunta.setText("Fim do quiz!")
            self.botao_reiniciar.show()
            self.Label_recopensa.setText(f"Você acertou {self.acertos} de {len(self.perguntas)}")
            self.Label_recopensa.setStyleSheet("font-size: 30px; font-weight: bold;")
            self.Label_recopensa.show()
            self.label_acertos.hide()
            random.shuffle(self.perguntas)
            if self.acertos >= len(self.perguntas) / 2:
                self.Label_Pirulito.setText("Parabens! você ganhou um pirulito!")
                self.Label_Pirulito.show()
            else:
                self.Label_Pirulito.setText("Que pena... Você não ganhou um pirulito")
                self.Label_Pirulito.show()



            for botao in self.botoes:
                botao.hide()

    def reiniciarQuiz(self):
        self.botao_reiniciar.hide()
        self.Label_recopensa.hide()
        self.indice_pergunta = 0
        self.acertos = 0
        self.label_acertos.setText(f'Acertos: <span style="color: black;">{self.acertos}</span>')

        self.Label_Pirulito.hide()
        self.label_acertos.show()
        self.label_acertos.setStyleSheet('font-size: 40px; font-weight: bold; margin-top: 20px;')
        self.carregar_pergunta()
    

    def verificar_resposta(self):
        botao_clicado = self.sender()
        resposta_usuario = botao_clicado.text()
        resposta_certa = self.perguntas[self.indice_pergunta]["resposta certa"]
        
        
        
        if resposta_usuario == resposta_certa:
            self.acertos += 1
            self.label_acertos.setText(f'Acertos: <span style="color: green;">{self.acertos}</span>')
            
            
        else:
            self.label_acertos.setText(f'Acertos: <span style="color: red;">{self.acertos}</span>')

           


                     
        if self.acertos < 0:
            self.acertos = 0
            
        self.indice_pergunta += 1
        self.carregar_pergunta()
    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()





aplicacao = QApplication(sys.argv)
j = Janela()
j.setStyleSheet("background-color: #0e69c4;") ###9ea7c0; azul claro meio cinza / #a3a1b0; um cinza meio escuro suave / #d1d0db; branco meio escuro, minimalista
sys.exit(aplicacao.exec())

