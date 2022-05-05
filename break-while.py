my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for food in my_list:
    if food == "hot dog":
        print('hello')
        break
    print('hi')
    print(food, end= " ")

num = 1
new_num = 0
while num < 7:
    for i in range(3):
        new_num += 1
    num += 3
print(new_num)