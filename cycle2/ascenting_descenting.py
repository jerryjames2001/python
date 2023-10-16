list1 = {'Tom': 31, 'Jerrin': 10, 'Shijo': 26, 'Jeril': 8, 'Merin': 16, 'Ashy': 1}
l=list(list1.items())
l.sort()
print("In ascending order:",l)
l.sort(reverse=True)
print("Descenting order:",l)