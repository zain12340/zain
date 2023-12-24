car=c

print(car)
print(car["year"])
print(car["color"][1])

car["year"]=2023
print(car["year"])

car["color"][1]='red'
print(car)

car["size"]='large'
print(car)

car.pop("year")
print(car)



