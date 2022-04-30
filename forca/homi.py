''' 8 linhas
   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / \
  |
 _|__
 '''

def forca(erros: int):

    if erros == 0:
        print('   _______\n  |/      |\n  |      \n  |      \n  |       \n  |      \n  |\n _|__')
    elif erros == 1:
        print('   _______\n  |/      |\n  |      (_)\n  |      \n  |       \n  |      \n  |\n _|__')
    elif erros == 2:
        print('   _______\n  |/      |\n  |      (_)\n  |      \|\n  |       \n  |      \n  |\n _|__')
    elif erros == 3:
        print('   _______\n  |/      |\n  |      (_)\n  |      \|/\n  |       \n  |      \n  |\n _|__')
    elif erros == 4:
        print('   _______\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |      \n  |\n _|__')
    elif erros == 5:
        print('   _______\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |      / \n  |\n _|__')
    else:
        print('   _______\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |      / \\\n  |\n _|__')

'''
  __ 
 / _|
| |_ 
|  _|
| |  
|_|  
'''

def morte():
    print('  __ \n / _|\n| |_\n|  _|\n| |  \n|_| ')


respostas = {
    'quartzo' : 'pedra',
    'hera' : 'plantas',
    'psique' : 'mente',
    'xilofone' : 'instrumento musical',
    'catarro' : 'fluído corporal'
}