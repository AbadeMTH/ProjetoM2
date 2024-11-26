import re

def inputConsistente(dado, tipoDado):
    #Sequência de condições para cada tipo de input
    if tipoDado == 'str' and re.match(r'^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ]+( [A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ]+)*$', dado) and len(dado) <= 50: #Regex aceita apenas letras com ou sem acentos ou cedilhas sem espaços no início e finall
        return dado
    elif tipoDado == 'sexo' and dado.lower() in ['m', 'f', 'feminino', 'masculino']:
        return 'Masculino' if dado.lower() == 'm' else 'Feminino'
    elif tipoDado == 'int' and dado.isdigit():
        return int(dado)
    elif tipoDado == 'cpf' and dado.isdigit() and len(dado) == 11:
        return dado
    elif tipoDado == 'idade' and dado.isdigit() and 0 < int(dado) < 120:
        return int(dado)
    elif tipoDado == 'sintomas' and re.match(r'^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ.,;:\- ]+( [A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ.,;:\- ]+)*$', dado) and len(dado) <= 180:
        return dado
    else:
        return 'None'