#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,Италия
#РейнаТур – Англия,Япония,Канада,ЮАР. Определить:
#1. какие туры из Вояж, отсутствуют в РейнаТур.
#2. какие товары из РейнаТур, отсутствуют в Вояж
#3. перечень одинаковых туров.
#4. равны ли перечни туров

voyage_tours = {'Мексика', 'Канада', 'Израиль', 'Италия'}
reina_tours = {'Англия', 'Япония', 'Канада', 'ЮАР'}

absent_in_reina = voyage_tours - reina_tours

absent_in_voyage = reina_tours - voyage_tours

identical_tours = voyage_tours & reina_tours

are_equal = voyage_tours == reina_tours

print("Туры из Вояж, отсутствующие в РейнаТур:", absent_in_reina)
print("Туры из РейнаТур, отсутствующие в Вояж:", absent_in_voyage)
print("Одинаковые туры:", identical_tours)
print("Перечни туров равны:", are_equal)