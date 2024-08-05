commanders = {(4, "Barzak"), (2, "Donesia"), (5, "Zeroza"), (1, "Yggacia"), (3, "Larzon")}

def sort_by_rank(commanders):
    commanders_list = list(commanders)
    commanders_list.sort(key=lambda x: x[0], reverse=True)
    return commanders_list

def sort_by_name(commanders):
    commanders_list = list(commanders)
    commanders_list.sort(key=lambda x: x[1])
    return commanders_list

print('Sorted by Rank:',sort_by_rank(commanders))
print('Sorted by Name:',sort_by_name(commanders))

'''
key is an optional parameter for the sort() method that specifies a function to be called on each list element prior to making comparisons for sorting.
lambda x: x[0] defines an anonymous function (lambda function) that takes a single argument x (each tuple in this case) and returns the value of the first element (x[0]) of the tuple.
For example, if the tuple is (4, "Barzak"), the lambda function will return 4.
This means that the sort() method will use the first element of each tuple as the key for sorting.
'''