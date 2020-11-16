while True :
    
    print('''Данная программа предназначена для анализа иерархий методом Т. Саати.
      \nДля выхода из программы нажмите 0 
      ''')
      
    h = input('Введите размерность матрицы попарных сравнений: ')
    #Проверка символов переменной h:
    while not str(h).isdigit():
            h = input('Введите целое число: ')
            h = h.replace(' ', '')
            for elem in h:
                if elem.isalpha():
                    break
                elif ',' in h:
                    break
                elif '.' in h:
                    break
                elif elem.isdigit():
                    continue   
                
    if  int(h) < 0:
        print('Введите число, большее 0. ')
            
    if int(h) > 0:
        print('''
        Для заполнения таблицы используйте шкалу следующего типа:
        \n1 - равная важность​
        \n3 - умеренное превосходство одного над другим​
        \n5 - существенное превосходство одного над другим​
        \n7 - значительное превосходство одного над другим​
        \n9 - очень сильное превосходство одного над другим​
        \n2, 4, 6, 8 - соответствующие промежуточные значения​
        ''')
        
        #Создание матрицы из нулей:
        M = []
        for i in range(int(h)): 
            M.append([])
            for j in range(int(h)): 
                if i == j:
                    M[i].append(1)
                else:
                    M[i].append(0)
        
        #Заполнение матрицы элемнетами:
        for i in range(int(h)): 
            for j in range(int(h)): 
                if M[j][i] != 0: #Условие, позволяющее заполнить элементы только выше главной диагонали 
                    continue
                else:    
                    a = 'a'+'['+str(i)+']'+'['+str(j)+']'
                    elem = 'error' 
                    while elem == 'error':
                        try:
                            elem = float(input('Введите элемент таблицы равный целому или дробному числу (через точку), больше 0.'+ a +' ='))
                            M[i][j] = elem 
                            M[j][i] = 1/elem
                        except ValueError: elem = 'error'
                        except ZeroDivisionError: elem = 'error'
                        if elem == 'error':
                            print('Введите целое или дробное число (через точку), большее 0. ')
                        else:
                            break
                    
        #Вывод матрицы попарного сравнения:
    print('Матрица попарного сравнения критериев: ')           
    for i in range(int(h)):
        print(M[i]) 

        #Суммирование всех элементов матрицы:
    sum_all = float() 
    for i in range(len(M)):
        for j in range(len(M[i])):
            sum_all += M[i][j]
           
        sum_line = float() 
    print('Весовые коэффициенты: ')
    for i in range(len(M)): #Перебор всех строк матрицы
        sum_line = sum(M[i]) #Суммирование элементов по строкам
        w = 'w'+ str(i) + ' = '
        wes = sum_line/sum_all #Расчет весового коэф-та
        print(w, wes) 
    if int(h) == 0 :
        break    
        
    

    
           