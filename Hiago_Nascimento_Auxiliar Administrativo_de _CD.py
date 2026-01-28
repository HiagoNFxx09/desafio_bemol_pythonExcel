import pandas as pd

df =pd.read_excel(r"dados\base_dados_basico.xlsx")

#1.	Qual é a soma do valor total de vendas (em R$) agrupada por unidade, desconsiderando registros inválidos?
registros_validos = df[(df['Valor Total']>0) &
                        (df['Qtd']>0)]

vendas_unidade = (registros_validos.groupby('Unidade')['Valor Total'].sum())
print('A soma total de vendas é R$ {}'.format(vendas_unidade))

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

unidade_mais_vendas = registros_validos['Unidade'].value_counts().idxmax()

categoria_mais_vendido = (registros_validos[registros_validos['Unidade'] == unidade_mais_vendas].groupby('Categoria')['Qtd'].sum().idxmax())

produto_mais_vendido = (registros_validos[(registros_validos ['Unidade'] == unidade_mais_vendas) & 
                                          (registros_validos['Categoria'] == categoria_mais_vendido)].groupby('Produto')['Qtd'].sum().idxmax())

quantidade_produto = (registros_validos [(registros_validos['Unidade']== unidade_mais_vendas) & 
                                         registros_validos ['Produto'] == produto_mais_vendido]['Qtd'].sum())
print('=-' *30)
print(unidade_mais_vendas, categoria_mais_vendido, produto_mais_vendido, quantidade_produto)

#7.	Se considerarmos o produto com o maior valor total de vendas em cada centro,
# qual deles, entre esses vencedores locais,possui a maior diferença percentual em
# relação ao segundo colocado no seu respectivo centro?
def diferenca_percentual(grupo):
    valores = grupo.sort_values(ascending=False)
    if len(valores) < 2:
        return 0
    return ((valores.iloc[0] - valores.iloc[1]) / valores.iloc[1])*100

dif_percentual = ( registros_validos.groupby(['Centro', 'Produto']) ['Valor Total'].sum().groupby('Centro').apply(diferenca_percentual))
print('=-' *30)
print(dif_percentual)


#8.	Determine o percentual de vendas de cada categoria em relação ao total de vendas.
total_vendas = registros_validos['Valor Total'].sum()
percentual_categoria = (registros_validos.groupby('Categoria')['Valor Total'].sum() / total_vendas)*100
print('=-' *30)
print('O percentual de vendas de cada categoria em relação ao total de vendas é: {}'.format(percentual_categoria))

#9.	Liste os 5 vendedores com menor desempenho (em valor total de vendas).
vendedores_Menor_desempenho = ( registros_validos.groupby('Cod_vendedor')['Valor Total'].sum().sort_values().head(5))
print('=-' *30)
print('Os 5 vendedores com menor desempenho é : {}'.format(vendedores_Menor_desempenho))

#10. Qual a média de produtos vendidos por venda (Qtd) em cada unidade?
media_produtos = registros_validos.groupby('Unidade')['Qtd'].mean()
print('=-' *30)
print('A média de produtos vendidos por Quantidade em cada unidade é: {}'.format(media_produtos))


'''
GABARITO

Q1: Soma do valor total de vendas por unidade conforme saída do código.

Q2:
Unidade com maior faturamento: {unidade_maior_em_vendas}
Produto mais vendido: {produto_mais_vendido}
Valor total: R$ {unidade_maior_valor_total}

Q3:
Vendedor com maior faturamento: {vendedor_maior_em_vendas}
Valor vendido: R$ {vendedor_maior_total_venda}

Q4:
Faturamento por categoria e centro conforme tabela gerada.

Q5:
Centro com maior ticket médio: {centro_maior_vendas}
Ticket médio: R$ {valor_ticket_vendas}

Q6:
Unidade: {unidade_mais_vendas}
Categoria: {categoria_mais_vendido}
Produto: {produto_mais_vendido}
Quantidade: {quantidade_produto}

Q7:
Diferença percentual entre campeão e segundo colocado por centro conforme cálculo.

Q8:
Percentual de vendas por categoria conforme cálculo.

Q9:
Cinco vendedores com menor desempenho listados acima.

Q10:
Média de produtos vendidos por venda em cada unidade conforme cálculo.
'''






