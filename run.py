from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://www.meetup.com/pt-BR/Grupy-SP/events/260344985/attendees/')
elementos = driver.find_elements_by_class_name('text--ellipsisOneLine')
contador = 0
for elemento in elementos:
    print(elemento.text)
    contador += 1

print(f'O evento tem um total de {contador} inscritos!')
driver.close()
