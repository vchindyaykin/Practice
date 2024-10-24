def sperma():
  user_input = int(input("Введите свой возраст для продолжения работы на сайте: "))
  if user_input >= 18:
    print("Доступ к сайту разрешен!")
  else:
    print("Доступ заблокирован, не дорос ещё!")
sperma()
