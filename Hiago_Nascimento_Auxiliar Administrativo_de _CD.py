import pandas as pd

df =pd.read_excel(r"dados\base_dados_basico.xlsx")

#Questao 1.
# desconsiderando registros inválidos.

registros_validos = df[(df['Valor Total']>0) &
                        (df['Qtd']>0)]

#Qual é a soma do valor total de vendas (em R$) agrupada por unidade.
vendas_unidade = (registros_validos.groupby('Unidade')['Valor Total'].sum())

print(vendas_unidade)


#2.	Qual foi a unidade com o maior valor total de vendas, qual foi o produto mais vendido (em quantidade) 
#nessa unidade e qual foi o valor total de vendas dessa unidade?
unidade_maior_em_vendas = vendas_unidade.idxmax()
unidade_maior_valor_total = vendas_unidade.max()
dados_unidade =registros_validos[registros_validos['Unidade']== unidade_maior_em_vendas]
produto_mais_vendido = (dados_unidade.groupby('Produto')['Qtd'].sum().idxmax())
print('=-' *30)
print('A unidade que mais vendeu é {}'.format(unidade_maior_em_vendas))
print('A unidade {} teve seu total de vendas de R$ {}'.format(unidade_maior_em_vendas,unidade_maior_valor_total))
print('O produto mais vendido é:  {} '.format(produto_mais_vendido))

#3.	Qual foi o vendedor com o maior total de vendas (em R$) e quanto ele vendeu?

vendas_por_vendedor = (registros_validos.groupby('Cod_vendedor')['Valor Total'].sum())
vendedor_maior_em_vendas = vendas_por_vendedor.idxmax()
vendedor_maior_total_venda = vendas_por_vendedor.max()
print('=-' *30)
print('O vendedor que mais vendeu foi: {} com um total de R$ {} '.format(vendedor_maior_em_vendas, vendedor_maior_total_venda))

#4.	Liste o faturamento por categoria em cada centro de vendas.

faturamento_categoria_centro = (registros_validos.groupby(['Categoria', 'Centro'])['Valor Total'].sum())
print('=-' *30)
print('O faturamento por categoria em cada centro de vendas é: {}'.format(faturamento_categoria_centro))

#5.	Qual foi o centro de vendas com o maior ticket médio (valor total médio por compra)
# e qual foi o valor desse ticket médio?

ticket_medio = registros_validos.groupby('Centro')['Valor Total'].mean()

centro_maior_vendas = ticket_medio.idxmax()
valor_ticket_vendas = ticket_medio.max()

print('=-' *30)
print('O centro de vendas com o maior ticket médio é {} é o valor desse ticket médio é {}'.format(centro_maior_vendas, valor_ticket_vendas))

#6.	Qual foi a unidade com o maior número de vendas, qual a categoria mais vendida dentro dessa unidade,
# qual foi o produto mais vendido dentro dessa categoria e quantas unidades desse produto foram vendidas?

unidade_mais_vendas = registros_validos.groupby('Unidade').value_counts().idxmax()

categoria_mais_vendido = (registros_validos[registros_validos['Unidade'] == unidade_mais_vendas].groupby('Categoria')['Qtd'].sum().idxmax())

produto_mais_vendido = (registros_validos[(registros_validos ['Unidade'] == unidade_mais_vendas) & 
                                          (registros_validos['Categoria'] == categoria_mais_vendido)].groupby('Produto')['Qtd'].sum().idxmax())

quantidade_produto = (registros_validos [(registros_validos['Unidade']== unidade_mais_vendas) & 
                                         registros_validos ['Produto'] == produto_mais_vendido]['Qtd'].sum())
print('=-' *30)
print(unidade_mais_vendas, categoria_mais_vendido, produto_mais_vendido, quantidade_produto)







