
sentence=input('please enter a sentence:')
x=set(sentence)
output=dict()
for i in x :
    output.update({i:sentence.count(i)})
print(output)