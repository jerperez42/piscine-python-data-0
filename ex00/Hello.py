ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
ft_list[1] = 'World!'

tmp_list = list(ft_tuple)
tmp_list[1] = 'France!'
ft_tuple = tuple(tmp_list)

ft_set.remove("tutu!")
ft_set.add('Paris!')

ft_dict["Hello"] = '42Paris!'
#

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
