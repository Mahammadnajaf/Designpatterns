#SRP SOC

class Journal:
    def __init__(self):
        self.entries=[]
        self.count=0

    def add_entry(self,text):
        self.count+=1
        self.entries.append(f"{self.count}: {text}")
    def remove_entry(self,pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class Persistance_Manager:
    @staticmethod
    def save_to_file(journal,filename):
        file=open(filename,'w')
        file.write(str(journal))
        file.close()


j=Journal()
j.add_entry("necesen ayqam")
j.add_entry("uww qaqamdie")
print(f'Jounral entry: \n{j}')

p=Persistance_Manager
file=r'/home/najaf/journal.txt'
p.save_to_file(j,file)

#verify
with open(file) as fh:
    print(fh.read())
