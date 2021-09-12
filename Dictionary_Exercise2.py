code = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'2', 'c':'1', 'D':'4', 'd':'3', \
'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':',', \
'J':'.', 'j':'>', 'K':'<', 'k':'$', 'L':'0', 'l':'\-', 'M':'\"', 'm':':', 'N':';', \
'n':'+', 'O':'$', 'o':'-', 'Q':'/', 'q':'%', 'R':'^', 'r':'&', 'S':'=', \
's':'(','T':')', 't':'~', 'U':'`', 'u':'5', 'V':'\\', 'v':'+', 'W':'*', 'w':'7', \
'X':'~', 'x':')', 'Y':'2', 'y':'*', 'Z':']', 'z':'8'}

infile = open('info_security.txt','r')
read_infile = infile.read()



infile.close()



encrypted_text = open('encrypted_file.txt','w')

for letter in read_infile:
    if letter in code:
        encrypted_text.write(code[letter])
encrypted_text.close()