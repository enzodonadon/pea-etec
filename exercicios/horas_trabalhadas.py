"""
⦁	Obtenha o valor para a variável HT (horas trabalhadas no mês);
⦁	Obtenha o valor para a variável VH (valor hora trabalhada):
⦁	Obtenha o valor para a variável PD (percentual de desconto);
⦁	Calcule o salário bruto => SB = HT * VH;
⦁	Calcule o total de desconto => TD = (PD/100) *SB;
⦁	Calcule o salário líquido => SL = SB - TD;
⦁	Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário Líquido.
"""

ht = float(input("Horas trabalhadas no mês: "))
vh = float(input("Valor por hora trabalhada: "))
pd = float(input("Percentual de desconto: "))

sb = ht * vh
td = (pd/100) * sb
sl = sb - td

print()
print(
    f"Horas trabalhadas: {ht}\n"
    f"Salário bruto: {sb}\n"
    f"Desconto: {pd}\n"
    f"Salário Líquido: {sl}"
)