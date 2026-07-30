

"""set is an unordered data structure"""

set_comp = {
    x**2 for x in range(10)
}



"""Ex 1 : find the squres of the all the even numbers under 100"""

even_number_sq = {x**2 for x in range(100) if x%2 == 0}

# print(even_number_sq)

"""Ex  2 : find the length of words, the lenght would be unique """

words = ["apple", "banana", "kiwi", "pear", "apple", "fig"]

word_length = {len(word) for word in words}
# print(word_length)



