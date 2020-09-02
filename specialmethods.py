class book():
    def __init__(self,name,author,totalpages,kind):
        self.name=name
        self.author=author
        self.totalpages=totalpages
        self.book_kind=kind
    def __str__(self):
        return "name:{} \nauthor:{} \ntotal_pages:{} \nkind:{}".format(self.name,self.author,self.totalpages,self.book_kind)
    def __len__(self):
        return self.totalpages
    def __del__(self):
        return

book1=book("honey","jeny",210,"action")
print(book1)
print(len(book1))
del book1
