import re

def strip_other_books(data):
   
    counter = 0 
    other_book_position = None
    for x in data:
        
        if(x == 'Other Books You May Enjoy'):
            other_book_position = counter
            
        counter = counter + 1 
    if(other_book_position is not None):
        data_without_other_book = data[:other_book_position-1]
    else:
        data_without_other_book = data 

    return data_without_other_book

def strip_preface_introduction(data):
   
    counter = 0
    for x in data:
        counter = counter + 1
        if(x == 'Preface'):
            position_in_list = counter
        elif(x == 'Introduction'):
            position_in_list = counter

    
    data_without_preface = data[position_in_list+1::]
   
    return data_without_preface

def remove_appendix_from_list(data):
   
    counter = 0
    for x in data:
        if(re.match("Appendix", x)):
            data_without_appendix = data[:counter]
   
            return data_without_appendix
   
        counter += 1
   
    return data

def remove_chapter_section_from_str(data):
    
    without_chapter_secton = []

    for x in data:
        if(re.match("Chapter", x)):
            x_without_2 = re.sub("Chapter\s\d.\s", '', x)
           
            without_chapter_secton.append(x_without_2.strip())
        elif(re.match('Section',x)):
            pass
        else:
            without_chapter_secton.append(x)
    return without_chapter_secton
    