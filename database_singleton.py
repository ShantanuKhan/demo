class database:
    
    __instance = None

    @staticmethod
    def getInstance():
        if database.__instance == None:
            database()
        return database.__instance
    
    def __init__(self):
        if database.__instance != None:
            raise Exception("Singleton Database Class")
        else:
            database.__instance = self

s = database()
print(s)

s = database.getInstance()
print(s)

s = database.getInstance()
print(s)

# s = database() //invalid object creation
# print(s)

print("Singleton class example master update")