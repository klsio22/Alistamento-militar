from datetime import date

cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\33[35m',
    'verdeAgua': '\033[36m',
    'cinza': '\033[37m',
    'Mageta': '\033[35m',

    'fundo preto ': '\033[40m',
    'fundo vermelho ': '\033[41m',
    'fundo verde ': '\033[42m',
    'fundo amarelo ': '\033[43m',
    'fundo azul': '\033[44m',
    'fundo magenta ': '\033[45m',
    'fundo ciano ': '\033[46m',
    'fundo branco': '\033[47m',

}

print('\n' + '-=-' * 10 + ' Alistamento Militar ' + '-=-' * 10 + '\n')

genero = str(input('{}Digite o sexo "m" para masculino ou "f" para feminino : {}'
                   .format(cores['verdeAgua'], cores['limpa']))).strip().lower()

if genero == str('m'):
    print('\n' + '-=-' * 20)
    print('{}AVISO : A data de Nascimento deve ser valida .{}'.format(cores['vermelho'], cores['limpa']))
    print('-=-' * 20)
    dataNascimento = int(input('\n{}Ano de nascimento do Candidato: {}'.format(cores['amarelo'], cores['limpa'])))

    anoAtual = date.today().year
    idadeAlistamento = 18
    idadeAtual = anoAtual - dataNascimento

    if 0 < idadeAtual < 18:

        print('Quem nasceu em {} tem {} anos em {}.'.format(dataNascimento, idadeAtual, anoAtual))
        print('falta {} anos/ano para o seu alistamento'.format(idadeAlistamento - idadeAtual))
        print('Seu alistamento será em {}.'.format(anoAtual+(idadeAlistamento - idadeAtual)))


    elif idadeAtual == 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(dataNascimento, idadeAtual, anoAtual))
        print('Você tem que se alistar IMEDIATAMENTE!')

    elif 18 < idadeAtual < 70:
        print('Quem nasceu em {} tem {} anos em {}.'.format(dataNascimento, idadeAtual, anoAtual))
        print('Você já deveria ter se alistado há {} ano/anos'.format(idadeAtual - idadeAlistamento))
        print('Seu alistamento foi em {}.'.format(anoAtual-(idadeAtual-idadeAlistamento)))

    else:
        print('\nAno inválido')
elif genero == str('f'):
    print('{}Mulher não é obrigatoria ao alistamento{}'.format(cores['roxo'], cores['limpa']))
else:
    print('{}{}Dígito/Digitos inválido{}'.format(cores['branco'], cores['fundo vermelho '], cores['limpa']))
