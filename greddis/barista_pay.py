NUM_EMPLOYEES = 6 # кол-во работничков

def main():
    hours = [0] * NUM_EMPLOYEES

    for index in range(NUM_EMPLOYEES):
        print("Введите кол-во часов отработанных сотрудником ",
              index + 1, ": ", sep='', end='')
        hours[index] = float(input())

        #почасовая

        pay_rate  = float(input('Введите почасовую ставку '))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('ЗП сотрудника ', index + 1, ':$', format(gross_pay, '.2f'), sep='')

main()