
# Ask user for birth year
birth_year = int(input("Digite o ano de nascimento: "))

# Calculate the remainder of birth year divided by 12
remainder = birth_year % 12

# Determine the zodiac sign based on the remainder
if remainder == 0:
    sign = "Macaco"
elif remainder == 1:
    sign = "Galo"
elif remainder == 2:
    sign = "Cão"
elif remainder == 3:
    sign = "Porco"
elif remainder == 4:
    sign = "Rato"
elif remainder == 5:
    sign = "Boi"
elif remainder == 6:
    sign = "Tigre"
elif remainder == 7:
    sign = "Coelho"
elif remainder == 8:
    sign = "Dragão"
elif remainder == 9:
    sign = "Cobra"
elif remainder == 10:
    sign = "Cavalo"
else:
    sign = "Carneiro"

# Print the zodiac sign
print("Seu signo é:", sign)
