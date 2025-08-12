'''
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
for x in create_cubes(10):
    print(x)
'''

def create_cubes(n):

    for x in range(n):
        yield x**3 #makes it memory efficient as the result is returned post each iteration and not bulked out

for x in create_cubes(10):
    print(x)