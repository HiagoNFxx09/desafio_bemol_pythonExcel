import pandas as pd

df =pd.read_excel(r"dados\base_dados_basico.xlsx")

#Questao 1.
# desconsiderando registros inválidos.

registros_validos = df[(df['Valor Total']>0) &
                        (df['Qtd']>0)]

#Qual é a soma do valor total de vendas (em R$) agrupada por unidade.
vendas_por_unidades = (registros_validos.groupby('Unidade')['Valor Total'].sum())

print(vendas_por_unidades)


#2.	Qual foi a unidade com o maior valor total de vendas, qual foi o produto mais vendido (em quantidade) 
#nessa unidade e qual foi o valor total de vendas dessa unidade?
unidade_maior_em_vendas = vendas_por_unidades.idxmax()
unidade_maior_valor_total = vendas_por_unidades.max()
dados_unidade =registros_validos[registros_validos['Unidade']== unidade_maior_em_vendas]
produto_mais_vendido = (dados_unidade.groupby('Produto')['Qtd'].sum().idxmax())

print('A unidade que mais vendeu é {}'.format(unidade_maior_em_vendas))
print('A unidade {} teve seu total de vendas de R$ {}'.format(unidade_maior_em_vendas,unidade_maior_valor_total))
print('O produto mais vendido é:  {} '.format(produto_mais_vendido))

#3.	Qual foi o vendedor com o maior total de vendas (em R$) e quanto ele vendeu?

vendas_de_cada_vendedor = (registros_validos.groupby('Cod_vendedor')['Valor Total'].sum())
vendedor_maior_total_vendas = vendas_de_cada_vendedor.idxmax()
print(vendedor_maior_total_vendas)






