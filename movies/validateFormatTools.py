class VFMovieTool( object ):

    def formatPersonName(self,name):
        temp = name.split()
        for i in range(len(temp)):
            temp[i] = temp[i].capitalize()
        name = " ".join(temp)
        return name
