class jester:
    def laugh(self):
        return "laugh () calles"
    
    def __str__(self):
        return "A more helpful description"

obj = jester()
print(obj)