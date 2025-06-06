print("python 6th homework")


# 1: დაწერეთ პროგრამა, რომელიც შექმნის დიქტს, რომელშიც key-ები იქნება 1-დან 10-ის ჩათვლით რიცხვები,
# ხოლო value-ები key-ს შესაბამისი კვადრატები, ანუ {1: 1, 2: 4, 3: 9...}, არ დაწეროთ ხელით,
# გამოიყენეთ ციკლი(ბონუსი: გამოიყენეთ dictionary comprehension )
emptyDict = {}
for i in range(1, 11):
    emptyDict[i] = i ** 2

print(emptyDict)



# მოცემულია პროდუქტების ლისტი:
products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]
totalPrice = 0
#a. დაბეჭდეთ ყველა პროდუქტის დასახელება
for i in products:
    for j in i:
        print(f"prodycts names are: {j}")

# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)
        name = i[j]

#
        price = name["price"]
        quantity = name["quantity"]
        totalPrice = totalPrice + price * quantity
print(f"total price of all items are {totalPrice}")


# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:
fruits = {}
fruit_name = input("Enter your fruit name: ")

while True:
    if fruit_name == "stop":
        break
    elif fruit_name in fruits:
        fruits[fruit_name] += 1
    else:
        fruits[fruit_name] = 1
print(fruits)

