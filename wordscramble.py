import random
def scramble(word) :
    sword = ""
    if len(word) > 3 :     

        if (word[-1] == ',' or word[-1] == '.' or word[-1] == '!' or word[-1] == ':' or word[-1] == '?' or word[-1] == "'" ):
          
           foo = list(word[1:-2])
           random.shuffle(foo) 
           sword = word[0] + ''.join(foo) + word[-2]+ word[-1]
           return sword.strip()
        else: 
          for i in range(1,len(word)-1) :
              if (word[i] == ',' or word[i] == '.' or word[i] == '!' or word[i] == ':' or word[i] == '?' or word[i] == "'" ):
              
                l1 = list(word[1:i])
                l2 = list(word[i+1:-1])
                l1=l1 + l2
                
                foo = l1
                random.shuffle(foo)

                foo.insert(i-1,word[i])
                sword = word[0] + ''.join(foo) + word[-1]
                return sword.strip() 
              

             
               
          foo = list(word[1:-1])
              
          random.shuffle(foo) 
               
          sword = word[0] + ''.join(foo) + word[-1]
          return sword.strip()

    else :
        return word


def process(words) :
        new = ' '.join(scramble(word) for word in words.split())
        file_name = open(new_file, 'a')
        file_name.write(new + '\n')
        file_name.close()
        return 0





file_name = input('Enter file name:')
try:
        number = 0
        count = 1
        file = open(file_name, 'r')
        new_file = 'Scrambled.txt'
        for line in file :
           words = line
           
           process(words)
        file.close()
        
except OSError as ose:
        print('Please enter file name properly')
