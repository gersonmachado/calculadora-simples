from tkinter import *

root = Tk()
root.title('Calculadora Simples') #Título
root.geometry('410x350') #Tamanho padrão de abertura
root.minsize(410, 350) #Tamanho mínimo
root.maxsize(410, 350) #Tamanho máximo

num1 = ''
divide = False
mult = False
soma = False
sub = False



root.configure(background='#292929') #Plano de fundo/ Cor em hex

#Parte de entrada de dados com Entry - Visor da calculadora
entrada = Entry(root, width=15, borderwidth=4, relief=FLAT,
                fg='#FFFFFF', bg='#CCCCCC', font=('futura', 25, 'bold'), justify=CENTER)

#funções
def botao_click(num):
    entrada.insert(END, num) #Inserir no final, número

def botao_divide():
    global num1
    global divide
    divide = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_soma():
    global num1
    global soma
    soma = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_menos():
    global num1
    global sub
    sub = True
    num1 = entrada.get()
    entrada.delete(0, END)


def botao_mult():
    global num1
    global mult
    mult = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_limpa():
    entrada.delete(0, END)

def botao_igual():
    global sub
    global mult
    global soma
    global divide
    num2 = entrada.get()
    entrada.delete(0, END)
    if soma == True:
        entrada.insert(0, float(num1) + float(num2))
        soma = False

    if sub == True:
        entrada.insert(0, float(num1) - float(num2))
        sub = False

    if mult == True:
        entrada.insert(0, float(num1) * float(num2))
        mult = False

    if divide == True:
        entrada.insert(0, float(num1) / float(num2))
        divide = False

#grid() adiciona o objeto criado no root/tela
entrada.grid(
    row=0, #Linha zero
    column=0, #Coluna zero
    columnspan=4,  #Ocupar 4 colunas
    pady= 2 #Distância entre o botão e o númer3
)



#botao dividir
divide = Button(root,
                text= '÷', #texto do botão
                padx=42, #largura
                pady=20, #altura
                command=botao_divide, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))

divide.grid(row=0,
            column=4)

#botao multiplicar
multiplica = Button(root,
                text= 'x', #texto do botão
                padx=42, #largura
                pady=20, #altura
                command= botao_mult, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))

multiplica.grid(row=1,
            column=4)

#botao somar
somar = Button(root,
                text= '+', #texto do botão
                padx=42, #largura
                pady=20, #altura
                command=botao_soma, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))

somar.grid(row=2,
            column=4)

#botao subtrair
subtrair = Button(root,
                text= '-', #texto do botão
                padx=44, #largura
                pady=20, #altura
                command=botao_menos, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))

subtrair.grid(row=3,
            column=4)

limpar = Button(root,
                text='C', #texto do botão
                padx=38, #largura
                pady=20, #altura
                command=botao_limpa, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
#adicionando a tecla na janela
limpar.grid(row=4,
          column=3)


igual = Button(root,
                text='=', #texto do botão
                padx=43, #largura
                pady=20, #altura
                command=botao_igual, #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 11, 'bold'))
#adicionando a tecla na janela
igual.grid(row=4,
          column=4)


#primeira fileira

um = Button(root,
                text= '1', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(1), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
um.grid(row=1,
            column=1)

dois = Button(root,
                text= '2', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(2), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
dois.grid(row=1,
            column=2)


tres = Button(root,
                text= '3', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(3), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
tres.grid(row=1,
            column=3)

quatro = Button(root,
                text= '4', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(4), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
quatro.grid(row=2,
            column=1)

cinco = Button(root,
                text= '5', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(5), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
cinco.grid(row=2,
            column=2)

seis = Button(root,
                text= '6', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(6), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
seis.grid(row=2,
            column=3)

sete = Button(root,
                text= '7', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(7), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
sete.grid(row=3,
            column=1)


oito = Button(root,
                text= '8', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(8), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
oito.grid(row=3,
            column=2)

nove = Button(root,
                text= '9', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(9), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
nove.grid(row=3,
            column=3)

zero = Button(root,
                text= '0', #texto do botão
                padx=91, #largura
                pady=20, #altura
                command=lambda: botao_click(0), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#f1f1f1', #seria o HOVER do button
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 13, 'bold'))
#adicionando a tecla na janela
zero.grid(row=4,
          column=1,
          columnspan=2)





#Para a janela pernamecer aberta aguardando ação
root.mainloop()

