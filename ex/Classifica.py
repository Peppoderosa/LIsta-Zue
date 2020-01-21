name = input('Name? ')
grade = float(input('Grade? '))

print('Name: {}, Grade: {}'.format(name,grade))
if grade >= 6:
    print('Concept: D')
    print('Aproved')
elif grade >= 7:
    print('Concept: C')
    print('Aproved')
elif grade >= 8:
    print('Concept: B')
    print('Aproved')
elif grade >= 9:
    print('Concept: A')
    print('Aproved')
else:
    print('Concept: E')
    print('Disappoved')