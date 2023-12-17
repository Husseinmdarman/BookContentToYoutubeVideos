import re

def strip_other_books(data):
    """
    Looking at the table of content of a particular book what we don't want is 
    anything after the other books you may enjoy section
    so it removes that from the contents

    for example, it may go like this
    chapter 12. Memory management
    other books you may like
    index

    so ideally the out result would be chapter 12. Memory management
    """
    counter = 0 #counter to indicate where in the list other books may be located
    other_book_position = None #index currently set to none
    for x in data:
        
        if(x == 'Other Books You May Enjoy'):
            other_book_position = counter
            
        counter = counter + 1 

    if(other_book_position is not None):
        data_without_other_book = data[:other_book_position-1]  #once found it will strip the table of contents list from the index position it found
    else:
        data_without_other_book = data #else it does nothing and returns the data

    return data_without_other_book

def strip_preface_introduction(data):
    """
    Strip preface and introduction from table of content
    """

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
    """
    Remove anything after and including the appendix from the table of content
    """
    counter = 0
    for x in data:
        if(re.match("Appendix", x)):
            data_without_appendix = data[:counter]
   
            return data_without_appendix
   
        counter += 1
   
    return data

def remove_chapter_section_from_str(data):
    """
    Remove chapter and section from title chapters in table of content

    for example chapter 9. memory managment

    would be outputted as memory managment 
    """
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
    