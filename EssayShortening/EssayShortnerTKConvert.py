
import pandas
import tkinter
from tkinter.filedialog import askopenfilename
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def browse():
    global infile    
    infile=askopenfilename()


def shortIt(outfile="C:/Users/CodersMine/Desktop/NewEssay.txt"):
    global infile
    if infile is None:
        infile=browse()
    file=open(infile,'r')
    lines=file.read()
    #print(lines)
    lines=lines.replace('.','\n')
    #print(lines)
    file.close()
    file=open("C:/Users/CodersMine/Desktop/Modified.txt",'w')
    file.write(lines)
    file.close()
    file=open("C:/Users/CodersMine/Desktop/Modified.txt",'r')
    #print(file.read())
    lines=file.readlines()
    #print(lines)
    corpus=[]
    for i in range(len(lines)):
        short=re.sub('[^a-zA-Z]',' ',lines[i])
        short=short.lower()
        short=short.split()
        ps = PorterStemmer()
        short=[ps.stem(word) for word in short if not word in set(stopwords.words('english'))]
        short=' '.join(short)
        corpus.append(short)
    
    corpus=' '.join(corpus)
    file=open(outfile,'w')
    print("File Written Successfully")
    file.write(corpus)
    file.close()

root=tkinter.Tk()
root.title("Essay Shortner")
label=tkinter.Label(root,text="This Program Finds the gist of the TEXT file given to it")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="Write To file ",command=shortIt)
kmlButton.pack()
root.mainloop()