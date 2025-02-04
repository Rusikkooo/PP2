# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
# Напишите функцию, которая принимает строку от пользователя, верните предложение со словами, которые были обращены вспять. Мы готовы -> готовы мы
import string 
def reversed_of_words(users_input):
    
    x = users_input.split()
    x.reverse()
    return " ".join(x)
   
            
    # return users_input
users_input  = input("Please enter :")
result = reversed_of_words(users_input)
print(result)