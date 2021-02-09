a="habahabahabahaba"
print(a.count("a")) # подсчет количества символов "a"    Работает и с LIST
print(a.count("ha"))


z=["a",4,"four","4",7,"neutron","proton","neutron"]
print(z.count("4"))   # 1 так как указали "4" STR
print(z.count("e"))   # 0 так как мы ищем цельный элемент(так как работаем в List, а не в str)

