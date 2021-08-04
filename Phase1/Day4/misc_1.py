class JustCount:
    __secretcount = 0
    
    
    def count(self):
        self.__secretcount += 1
        print (self.__secretcount)
        
Counter = JustCount()
Counter.count()
Counter.count()

print ("Type: ", type(Counter._JustCount__secretcount))