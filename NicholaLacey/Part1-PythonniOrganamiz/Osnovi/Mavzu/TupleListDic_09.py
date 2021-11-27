""" Кортежи, списки и словари """

"""
Объяснение
Пока что мы использовали переменные, в которых могло храниться только одно зна-
чение. Выполняя строку random.choice(["red", "blue", "green"]), вы выбираете 
один случайный элемент из списка возможных вариантов. Однако этот пример пока-
зывает, что одно значение может содержать несколько элементов данных (в данном 
случае это набор цветов).
Есть несколько вариантов сохранения наборов данных в одном значении. Три про-
стейших варианта:
   кортежи;
   списки;
   словари.
Кортежи
После того как кортеж будет определен, вы уже не сможете изменить 
его содержимое. Это означает, что при написании программы необ-
ходимо указать, какие данные хранятся в кортеже, и они останутся 
неизменными во время выполнения программы. Кортежи обычно ис-
пользуются для команд меню, которые не будут изменяться во время 
выполнения.
Списки
Содержимое списка может изменяться во время выполнения программы, поэтому 
списки стали одним из самых распространенных способов хранения наборов данных 
под одним именем переменной в Python. Данные в списке не обязаны относиться 
к одному типу. Например, в одном списке могут храниться как строки, так и целые 
числа; однако позднее это может создать путаницу при обработке списка, поэтому 
поступать так не рекомендуется

"""

n = int(input().strip())
if n % 2 == 0:
    print("Weird")
if 2 <= n <= 5:
    print("Not Weird")
if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
if n > 20:
    print("Not Weird")