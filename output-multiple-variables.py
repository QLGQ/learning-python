a='dead'        #Define three attributes
b='parrot'      #Exported to other files
c='sketch'
print(a, b, c)  #Also used in this file(in 2.X: print a,b,c)

#output
qiang@qiang:/tmp$ python threenames.py
('dead', 'parrot', 'sketch')
qiang@qiang:/tmp$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import threenames
('dead', 'parrot', 'sketch')
>>> threenames.b, threenames.c
('parrot', 'sketch')

