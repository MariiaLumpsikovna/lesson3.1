calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    list_ = [len(string), string.upper(), string.lower()]
    list_ = tuple(list_)
    count_calls()
    return list_
def is_contains(string, list_to_search):
    string = str(string.upper())

    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string == list_to_search[i]:
        a = True
    else:
        a = False
    count_calls()
    return a
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

