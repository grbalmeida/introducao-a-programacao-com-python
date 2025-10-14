# Exercício 3.13: Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é: F = (9 X C) / 5 + 32

graus_celsius = float(input("Digite a temperatura em graus celsius: "))
graus_fahrenheit = (9 * graus_celsius) / 5 + 32

print(f"{graus_celsius}ºC é igual a {graus_fahrenheit}ºF")