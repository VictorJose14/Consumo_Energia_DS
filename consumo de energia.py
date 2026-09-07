# Calculadora de Consumo Elétrico Inteligente

print("=" * 40)
print(" CALCULADORA DE CONSUMO ELÉTRICO ")
print("=" * 40)

# Entrada de dados
aparelho = input("Nome do aparelho (ex: Geladeira): ").strip()
potencia = float(input("Potência do aparelho em Watts (W): "))
horas_dia = float(input("Tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
# Fórmula: (potência * horas_dia * 30) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo opcional de custo estimado (tarifa média de R$ 0,75/kWh)
tarifa_kwh = 0.75
custo_estimado = consumo_mensal * tarifa_kwh

# Exibição dos resultados
print("\n" + "-" * 40)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês (tarifa: R$ {tarifa_kwh:.2f}/kWh)")
print("-" * 40)