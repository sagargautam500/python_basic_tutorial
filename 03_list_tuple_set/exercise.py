# Let‘s Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# movie1=input("enter first movie ")
# movie2=input("enter second movie ")
# movie3=input("enter third movie ")

# movies=[movie1,movie2,movie3]
# print(movies)
# print(type(movies))

movies = []

for i in range(3):
    movie = input("Enter your favorite movie: ")
    movies.append(movie)

print("Your favorite movies are:", movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1][1, “abc”, “abc”, 1]
lst = [1, 2, 3, 2, 1]
# lst = [1, "abc", "abc", 1]

copy_lst = lst.copy()
copy_lst.reverse()

if lst == copy_lst:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
