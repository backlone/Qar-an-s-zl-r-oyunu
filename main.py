import random

# Kelime listi tuple içindedir.
word_list = ("alma", "armud", "çiyələk", "banan", "qarpız", "portağal", "mandarin", "yemiş")

# Range ile random bir kəlimə uzunlugu seçirik
word_length = random.choice(range(4, 9))

# Tuple içindəki kəlimələr arasından seçilen uzunluqda bir kəlimə seçilir ve herfler qarışdırılır.
word = random.choice([w for w in word_list if len(w) == word_length])
shuffled_word = ''.join(random.sample(word, len(word)))

print("Kəlimə qarışdırıldı:", shuffled_word)

# Oyunçudan texmin istenir ve dogru olub olmadığı yoxlanir.
guess = input("Kəliməni təxmin et: ")
if guess.lower() == word:
    print("Təbriklər, doğru təxmin etdin!")
else:
    print("Təəssüflər olsun, yanlış təxmin etdin. Doğru kəlimə:", word)

# Complex istifadə edərək 2 rəqəm toplanır.
num1 = complex(2, 3)
num2 = complex(4, 2)
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")