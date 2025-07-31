set guess 0
set key 12
while !(guess = key)
    get guess ADIVINHA --> 
    if guess > key
        show Menor...
    elif guess < key
        show Maior...
show acertou!