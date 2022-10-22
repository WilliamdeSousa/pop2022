leds_n = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5,
          '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
num_casos = int(input())
for caso in range(num_casos):
    num = str(input())
    num_leds = 0
    for digito in num:
        num_leds += leds_n[digito]
    print(f'{num_leds} leds')