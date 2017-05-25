class VFBookTool (object ):
    
    def validateISBN(self,isbn):
        temp = isbn.split()
        temp2 = "".join(temp)
        temp = isbn.split('-')
        temp2 = "".join(temp)
        try:
            int(temp2)
            return True
        except ValueError:
            return False
        
    def formatISBN(self,isbn):
        temp = isbn.split()
        temp2 = "".join(temp)
        temp = isbn.split('-')
        temp2 = "".join(temp)
        return temp2
        
    def formatAuthorName(self,name):
        temp = name.split()
        for i in range(len(temp)):
            temp[i] = temp[i].capitalize()
        name = " ".join(temp)
        return name
