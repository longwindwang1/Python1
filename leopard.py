"""
Please write your name
@author:Changfeng Wang

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        filepath =  input("Print file name:") # Prompt the user for a file name
        self.filepath = filepath
        try:
            f =open(filepath) #Open the file
            f.close()       
        except FileNotFoundError:
            print ("File is not found.")
        with open(filepath) as f:
            if len(open(filepath).readline()) == 0: # Determining if a file is empty
                print("File is empty")
            else:
                reader = csv.reader(f)
                header = next(reader)
                self.header = header
                # First row

                for Remainingdata in reader:
                    self.Remainngdata = Remainingdata
                    # The data part

    def get_header(self) -> list:  
        if len(self.header) == 0:
            return None
        else:
            return self.header
    def get_data(self) -> list: 
        if len(self.Remainngdata) == 0:
            return None
        else:
            return self.Remainngdata
    def stats(self) -> dict:
        list1 = []
        with open(self.filepath, 'r') as f:
            reader = csv.DictReader(f)
            column = [row['label'] for row in reader]
        list1 = column
        for i in self.Remainngdata:
            try:
                float(i)
                return True
            except:
                return False


    def html_stats(self, stats: dict, filepath: str) -> None:
        # delete pass and this comment to write your code
        pass

    def count_instances(self, criteria) -> int:
        """
        Write your docstring to explain how to use this method.
        You are to decide what data type format is criteria or how many
        arguments to this method.
        Delete above and this comment to write your docstring.
        """
        # delete pass and this comment to write your code
        pass


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()
'''
    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
'''