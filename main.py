import re

texto = """
Bom dia,

Seguem os orçamentos solicitados:


Cerveja importada (330 ml) - R$12,30598615178 - bebida
Cerveja nacional (0,5 litros) - R$6,10 - bebida
Garrafa de vinho (750ml) - R$39,90 - bebida
Água (garrafa de 1,5 litros) - R$3,30 - bebida
Alface (1 unidade) - R$3,50 - comida
Cebolas (1kg) - R$5,10 - comida
Batatas (1 kg) - R$5,20 - comida
Tomates (1 kg) - R$7,90 - comida
Laranjas (1 kg) - R$4,70 - comida
Bananas (1kg) - R$5,50 - comida
Maçãs (1 kg) - R$8,30 - comida
Queijo fresco (1 kg) - R$42,90 - comida
Uma dúzia de ovos(12) - R$9,80 - comida
Arroz (1 kg) - R$5,70 - comida
Um quilo de pão (1 kg) - R$7,20 - comida
Leite (1 litro) - R$5,20 - bebida
Azeite (1 unidade) - R$20 - tempero
Pimenta Reino (20g) - R$5 - tempero


Favor informar as quantidades desejadas 
para emissão da Nota Fiscal.

Att.,"""


# quantas comidas
padrao = re.compile("comida")
resultado = re.finditer(padrao, texto)
print(resultado)
for item in resultado:
    print(item)

# quantas bebidas
padrao = re.compile("bebida")
resultado = re.findall(padrao, texto)
print(len(resultado))


# quantos itens
padrao = re.compile("\$")
resultado = re.findall(padrao, texto)
print(len(resultado))


novo_texto = "Nome: Lira Idade: 29 Salario: 1500"
padrao = re.compile(r"[a-zA-Z:]+")
resultado = re.findall(padrao, novo_texto)
print(resultado)

padrao = re.compile(r"R\$(\d+,?\d{0,2})")

resultado = re.findall(padrao, texto)
resultado2 = re.search(padrao, texto)
resultado3 = re.finditer(padrao, texto)

print(resultado)
print(resultado2)
for item in resultado3:
    print(item)

texto2 = """
Olá

Segue o relatório de SEO para os seguintes sites:
https://portalhashtag.com
http://hashtagtreinamentos.com
https://www.wikipedia.org/
www.bcb.gov.br/

Qualquer dúvida estamos à disposição"""

padrao = re.compile(r"(https?://)?(www\.)?\w+\.(com\.br|com|org|gov\.br)")
resultado1 = re.findall(padrao, texto2)
resultado2 = re.finditer(padrao, texto2)
print(resultado1)
for item in resultado2:
    print(item.group(0))