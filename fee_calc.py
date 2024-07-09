# Тарифы
electricity_tax = 5.82
cold_water_tax = 30.20
hot_water_tax = 257.74
canalization_tax = 39.17


# Счётчики
print("Показания счётчика электроэнергии в прошлом месяце: ")
electricity_before = float(input())
print("Показания счётчика электроэнергии сейчас: ")
electricity_now = float(input())

print("Показания счётчика холодной воды в прошлом месяце: ")
cold_water_before = float(input())
print("Показания счётчика холодной воды сейчас: ")
cold_water_now = float(input())

print("Показания счётчика горячей воды в прошлом месяце: ")
hot_water_before = float(input())
print("Показания счётчика горячей воды сейчас: ")
hot_water_now = float(input())


# Вывод
print("\n")
for_electricity = electricity_tax * (electricity_now - electricity_before)
print("За электроэнергию: %.2f" % for_electricity)

for_cold_water = cold_water_tax * (cold_water_now - cold_water_before)
print("За холодную воду: %.2f" % for_cold_water)

for_hot_water = hot_water_tax * (hot_water_now - hot_water_before)
print("За горячую воду: '%.2f" % for_hot_water)

for_canalization = canalization_tax * ((hot_water_now - hot_water_before) + (cold_water_now - cold_water_before))
print("За водоотведение: %.2f" % for_canalization)

total = for_electricity + for_cold_water + for_hot_water + for_canalization
print("Всего: %.2f" % total)
input()