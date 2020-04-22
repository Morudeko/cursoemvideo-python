# Forma simples
# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

# Formatado
# Apresentação
print("Para calcular a quantidade de tinta necessária, digite as medidas abaixo.")

# Variáveis
plat = float(input("Largura: "))
palt = float(input("Altura: "))

# Cálculos
area = (palt * plat)
tint = (area / 2)

# Resultado
print("A parede de {la:.1f}m x {al:.1f}m tem uma área de {ar:.2f}m² e necessita de {li:.2f}L de tinta".format(li=tint, ar=area, al=palt, la=plat))
