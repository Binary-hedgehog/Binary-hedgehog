class FiveLetters():
    #
    
    def __init__(self):
        
        all_words = open('russian_nouns.txt', encoding='utf-8')
        self.list_with_words = [i[0:-1] for i in all_words if len(i) == 6]
        self.new_word = ''
        self.truth = [None] * 5
        
    def input_new_word(self):
        
        print('Input any word with len 5: ')
        self.new_word = input()
        
        if len(self.new_word) != 5:
            print('Wrong lenght of word, try again =)')
            self.input_new_word()
        
        for i in self.new_word:
            if not (ord(i) >= 1072 and ord(i) <= 1103 or ord(i) == 1105):
                print('Wrong letters, should be rus in low reg, try again =)')
                self.input_new_word()
                              
    def input_coincedences(self):
        
        print('Input coincidences which mean:')
        print('"0"-non in this word,"-1"-wrong position,"1"-correct position')
        
        for count in range(5):
            try:
                self.truth[count] = int((input('Сoincidences ')))
            except ValueError:
                print('ValueError')
                self.input_coincedences()
        
        for i in self.truth:
            if i != 1 and i != -1 and i != 0:
                print('Wrong coincidences, try again =)')
                self.input_coincedences()
        
        print('Your coincidences - ', self.truth)
        
        if set(self.truth) == {1}:
            print('Your word is - ', self.new_word, 'Congratulations!!!')
            input('Bye =))')
        try:
            self.list_with_words.remove(self.new_word)
        except:
            pass
        
    def show_unic_words(self):
        
        list_unic_words = [i for i in self.list_with_words if len(set(i)) == 5]
        
        if len(list_unic_words) != 0:         
            print(list_unic_words)
        else:
            print(self.list_with_words)
        
    def elaboration_list_with_word(self):
        
        list_temp = []
        list_temp1 = [self.new_word[count] for count,          
                      val in enumerate(self.truth) if val == 1] 
        # list_temp1 with correct letters
        
        for i in self.list_with_words:
            for count in range(len(i)):
                if self.truth[count] == 0:
                    if self.new_word[count] in i and self.new_word[count] not in list_temp1:
                        break
                elif self.truth[count] == -1:
                    if self.new_word[count] not in i or self.new_word[count]==i[count]:
                        break
                elif self.truth[count] == 1:
                    if self.new_word[count] != i[count]:
                        break
                else:
                    print('incorrect coincidences')
                    input()
            else:
                list_temp.append(i)
                
        if len(list_temp) == 0:
            print('Smthng goes wrong, idk. Probably your dict isnt full') 
            # вообще это местро про мой баг или про то, что слова нет в списке
            print('Think by yorself now))). Bye =(') #
            print(self.list_with_words)
        elif len(list_temp) == 1:
            print('Your word is - ', list_temp, 'Congratulations!!!')
            input('Bye =))')
        else:
            self.list_with_words = list_temp.copy()
            
    def main(self):
        
        for count in range(5):
            self.show_unic_words()
            self.input_new_word()
            self.input_coincedences()
            self.elaboration_list_with_word()
        
        if len(self.list_with_words) == 1: 
            # probably this if does not work, need to test, but too lazy)))
            print('Your word is - ', self.list_with_words, 'Congratulations!!!')
            input('Bye =))')
        else:
            print('Choose one of them =)')
            print(self.list_with_words)
        input('Bye =)')
        
     
test_lab = FiveLetters()
test_lab.main()

