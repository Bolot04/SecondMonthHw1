"""Импорт и настройка:"""
# from faker import Faker

"""Указываем локлизацию"""
# fake = Faker("ru_RU")


"""Генерация нескольких записей"""
# for _ in range(5):
#     print({
#         "name": fake.name(),
#         "email":fake.email(),
#         "address":fake.address().replace("\n",","),
#         "lat": float(fake.latitude()),
#         "lon": float(fake.longitude()),
#         "website": fake.url()
#     })

"""Улучшенный вывод ткрминала"""
# for _ in range(5):
#     person = ({
#         "name": fake.name(),
#         "email":fake.email(),
#         "address":fake.address().replace("\n",","),
#         "lat": float(fake.latitude()),
#         "lon": float(fake.longitude()),
#         "website": fake.url()
#     })
#
#     print("────────────────────────────────────────")
#     print(f"Имя:     {person['name']}")
#     print(f"Email:   {person['email']}")
#     print(f"Адрес:   {person['address']}")
#     print(f"Широта:  {person['lat']}")
#     print(f"Долгота: {person['lon']}")
#     print(f"Сайт:    {person['website']}")
#     print("────────────────────────────────────────\n")




"""Генерация базовых данных"""
# print(fake.name())
# print(fake.address().replace("\n", ","))
# print(fake.text(max_nb_chars=200))
# print(fake.email())
# print(fake.country())



"""Доп задание"""
#brute force
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 9, 15, 22, 66]

target = 17

result = two_sum(nums, target)
print(result)

