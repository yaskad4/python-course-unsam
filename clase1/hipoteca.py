# Ejercicio 1.11
# hipoteca.py
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.
# ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

total_money = 500000.0
rate = 0.05
total_paid = 0.0
total_months = 0

while total_money > 0:
    total_months += 1
    if total_months >= 61 and total_months <= 108:
        monthly_paid = 3684.11
    else:
        monthly_paid = 2684.11
    total_money = total_money * (1 + rate / 12) - monthly_paid

    if total_money < 0:
        monthly_paid = monthly_paid + total_money # ojo es + porque ya saldo es negativo, y si pongo - en vez de restarlo se sumaria
        total_money = 0

    total_paid = total_paid + monthly_paid
    print(f'{total_months} - {total_paid:0.2f} - {total_money:0.2f}')

print('Total pagado: ', round(total_paid, 2))
print('Meses totales: ',total_months)