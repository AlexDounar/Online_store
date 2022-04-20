rome_number = input('Enter the Rome number: ')
list_of_rome_numbers = []
list_to_count = []
for number in rome_number:
    if number == "I" or "V" or 'X' or 'C' or 'M' or 'L':
        list_of_rome_numbers.append(number)

    else:
        raise Exception('UnacceptableNumber')
sum = 0
print(list_of_rome_numbers)
list_to_count = list_of_rome_numbers.reverse()
print(list_of_rome_numbers)
for el in list_of_rome_numbers:

    if el == 'I':
        sum += 1
        print(sum)


    elif el == 'V':

        if el in range(list_of_rome_numbers[+1:]) != 'I':
            sum += 5
            print(sum)

        else:
            sum += 4
            print(sum)


    elif el == 'X':

        if el in range(list_of_rome_numbers[+1:]) != 'I':
            sum += 10
            print(sum)

        else:
            sum += 9
            print(sum)



    else:
        raise ValueError
print(sum)

for i in range(len(list_of_rome_numbers)):
    print(list_of_rome_numbers[i +1:])



{% for part in parts %}
            <div class="alert alert-warning mt-2">
                <h3>{{ part.name_of_part}}</h3>
                <p>{{ part.description }}</p>
            </div>
        {% endfor %}