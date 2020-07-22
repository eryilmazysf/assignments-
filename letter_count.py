sentence=input('please enter a sentence:')
y=list()
output=dict()
for i in sentence:
    y.append(i)
z=set(y)
for x in z:
    output.update({x:y.count(x)})
print(output)