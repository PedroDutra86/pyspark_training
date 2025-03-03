a = 'A'
b = 'B'
c = 1.1
format_type = 'a={}, b={}, c={:.2f}'.format(a, b, c,)
format_type_by_index = 'a={0}, b={1}, c={2:.2f} d={2} e={1}'.format(a, b, c,)
format_type_by_index_named = 'a={first_name}, b={second_name}, c={third_name:.4f}'.format(first_name=a,second_name=b,third_name=c,)

print(format_type)
print(format_type_by_index)
print(format_type_by_index_named)