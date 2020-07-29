def end_other(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    if len(word1)>=len(word2):
        if word1[-len(word2):] == word2:
            return True
        else:
            return False
    else:
        if word2[-len(word1):]==word1:
            return True
        else:
            return False
print(end_other('AbC','abXabc'))