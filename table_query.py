def check_constraints(table, constraints):
    result = 0
    
    for row in table:
        # Проверяем, удовлетворяет ли текущая строка всем ограничениям
        satisfy = True
        for constraint in constraints:
            column_name, operator, value = constraint
            column_index = table[0].index(column_name)
            column_value = row[column_index]
            
            if operator == '<' and column_value >= value:
                satisfy = False
                break
            
            if operator == '>' and column_value <= value:
                satisfy = False
                break
        
        # Если текущая строка удовлетворяет всем ограничениям, добавляем сумму ее элементов к результату
        if satisfy:
            result += sum(row)
    
    return result
