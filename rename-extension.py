# Programador - Eduardo Caetano

# GUI PYTHON PARA RENOMEAR E TROCAR AS EXTENÇÃO DE ARQUIVOS USANDO O MÓDULO shutil
#
# O módulo shutil oferece várias operações de alto nível em arquivos e coleções de arquivos.
# Em particular, são fornecidas funções que suportam a cópia e remoção de arquivos.
#
# shutil.copy (src, dst, *, follow_symlinks = True) - copia o arquivo src no arquivo ou diretório dst.
# src e dst devem ser strings. Se dst especificar um diretório, o arquivo será copiado no dst usando
# o nome do arquivo base de src. Retorna o caminho para o arquivo recém-criado.
#
# shutil.move (src, dst, copy_function = copy2) - Move recursivamente um arquivo ou diretório (src) para outro
# location (dst) e retorne o destino.
# Importando pacotes necessários

import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Definindo a função CreateWidgets () para criar os widgets tkinter necessários
def CreateWidgets():
    # texto (label)
    linkLabel = Label(root, text="SELECIONE O ARQUIVO PARA RENOMEAR", bg="deepskyblue4" ,fg="white")
    linkLabel.grid(row=1, column=0, pady=5, padx=10)

    # campo onde vai o diretorio do arquivo que vai ser copiado
    root.sourceText = Entry(root, width=50, textvariable=sourceLocation ,justify="center")
    root.sourceText.grid(row=2, column=0, padx=5)

    # botao procurar arquivo
    source_browseButton = Button(root, text="BROWSE", command=SourceBrowse, width=15, bg="gray",fg="white")
    source_browseButton.grid(row=3, column=0, pady=5, padx=5)

    # -------------------------------------------------------------------------------------------------------------------------------------
    
    # texto (label)
    destinationLabel = Label(root, text="SELECIONE A PASTA PARA RENOMEAR TODOS", bg="deepskyblue4",fg="white")
    destinationLabel.grid(row=4, column=0, pady=(15,0), padx=5)

    # campo onde vai o diretorio onde o arquivo vai ser movido ou copiado
    root.destinationText = Entry(root, width=50, textvariable=destinationLocation , justify="center")
    root.destinationText.grid(row=5, column=0, padx=5)

    # botao procurar arquivo
    dest_browseButton = Button(root, text="BROWSE", command=DestinationBrowse, width=15, bg="gray",fg="white")
    dest_browseButton.grid(row=6, column=0, pady=5, padx=5)

    # -------------------------------------------------------------------------------------------------------------------------------------

    # texto (label)
    destinationLabel = Label(root, text="Extenção", bg="deepskyblue4",fg="white" ,justify="center")
    destinationLabel.grid(row=7, column=0, pady=(15,0), padx=5)

    # campo onde vai o diretorio onde o arquivo vai ser movido ou copiado
    root.extensaoText = Entry(root, width=50, justify="center")
    root.extensaoText.insert(0, ".png")
    root.extensaoText.grid(row=8, column=0, padx=5)

    # -------------------------------------------------------------------------------------------------------------------------------------

    # botao renomear ARQUIVO
    copyButton = Button(root, text="RENOMEAR UM ARQUIVO", command=renameFile, width=45)
    copyButton.grid(row=14, column=0, pady=(15,15), padx=15)

    copyButton = Button(root, text="RENOMEAR TODOS ARQUIVOS", command=rename_All_File, width=45)
    copyButton.grid(row=15, column=0, pady=(0,15), padx=15)

    copyButton = Button(root, text="LIMPAR CAMPOS", command=clear_text, width=45)
    copyButton.grid(row=16, column=0, pady=(0,15), padx=15)
    
    # -------------------------------------------------------------------------------------------------------------------------------------
# funçao para pegar o arquivo para renomear
def SourceBrowse():
    try:
        root.files_list = list(filedialog.askopenfilenames(initialdir="C:/Users"))

        root.diretorio_antigo = root.files_list[0]
        root.sourceText.insert('1', root.files_list)
        root.lst1 = root.files_list.pop()
        
        lst2 = root.lst1.split("/")
        del lst2[-1]    
        root.diretorio_arquivo = (lst2[0]+'/'+lst2[1]+'/'+lst2[2]+'/'+lst2[3]+'/'+lst2[4]+'/')
    except:
        pass

# funçao para pegar o diretorio para renomear todos
def DestinationBrowse():
    try:
        destinationdirectory = filedialog.askdirectory(initialdir="C:/Users")
        root.destinationText.insert('1', destinationdirectory)
    except:
        pass

def clear_text():
    root.extensaoText.delete(0, 'end')
    root.sourceText.delete(0, 'end')
    root.destinationText.delete(0, 'end')
    
# -------------------------------------------------------------------------------------------------------------------------------------

def renameFile():
    #files_list = root.files_list
    destination_location = (destinationLocation.get()+'/')
    x = 1
    arquivos = os.listdir(destination_location)

    try:
            os.rename(root.diretorio_antigo, root.diretorio_arquivo+('imagem-99'+str(x)+root.extensaoText.get()))
            x+=1
            messagebox.showinfo("SUCCESSO", "ARQUIVO RENOMEADO COM SUCCESSO")
    except:
            os.rename(root.diretorio_antigo, root.diretorio_arquivo+('foto-98'+str(x)+root.extensaoText.get()))
            x+=1
            messagebox.showinfo("SUCCESS", "FILES COPIED SUCCESSFULLY")

# -------------------------------------------------------------------------------------------------------------------------------------

def rename_All_File():
    #files_list = root.files_list
    destination_location = (destinationLocation.get()+'/')
    
    arquivos = os.listdir(destination_location)    
    
    for x in range(len(arquivos)):
        try:
                os.rename(destination_location+arquivos[x], destination_location+('imagem-'+str(x)+root.extensaoText.get()))
        except:
                
                os.rename(destination_location+arquivos[x], destination_location+('foto-'+str(x)+root.extensaoText.get()))

    messagebox.showinfo("SUCCESS", "FILES COPIED SUCCESSFULLY")

# -------------------------------------------------------------------------------------------------------------------------------------


root = tk.Tk()

# Definindo a cor do título e do plano de fundo desativando a propriedade de redimensionamento
root.geometry("350x370")
root.resizable(False, False)
root.title("Mudar a Extenção")
root.config(background = "deepskyblue4")

# Criando a variável tkinter
sourceLocation = StringVar()
destinationLocation = StringVar()
extensaoText = StringVar()

# Chamando a função CreateWidgets()
CreateWidgets()

# Definindo loop infinito para executar o aplicativo
root.mainloop()
