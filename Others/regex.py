import re

frase = "El mail de paula es paula@google.com, el de Guillermo por su lado es guillermo@microsoft.com y el de José, que me lo dijo ayer es jose@gmail.com"

print (frase)

expression = re.compile("[\w\.]+@[\w]+\.[\w]+")

emails = expression.findall(frase)

print(emails)