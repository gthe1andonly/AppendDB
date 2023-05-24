import csv
    
class StorageEngine:

    def __init__(self) -> None:
        self.path = "./"

    #  Take in headers as a list
    def create_db(self, db_name, headers):
        filename = self.path + db_name
        with open(filename, 'w',newline = '') as csvfile:
            writer = csv.DictWriter(csvfile , fieldnames=headers)
            writer.writeheader()
        
    def db_get(self, db_name, item_key):
        filename = self.path + db_name
        pass

    def db_set(self, db_name, item):
        filename = self.path + db_name
        headers = list(item.keys())
        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writerow(item)
        print(item, " has been added to db")
            

    def db_remove(self, db_name, item_key):
        pass
    
    
if __name__ == "__main__":
    storageEngine = StorageEngine()
    storageEngine.create_db("testdb.csv", ["col1", "col2"])
    storageEngine.db_set("testdb.csv", {"col1": "furstrow", "col2": "secondrow"})
    storageEngine.db_set("testdb.csv", {"col1": "2row", "col2": "3drow"})