# BookContentToYoutubeVideo

An educational tool alongside your academics studies, by the use of ISBN number of an educatinal book, we can search keyword terms provided by their chapter titles on both google scholar and youtube. 

# The aim

The idea behind this project and motivation is everything is easier when its streamlined, through the use of the chapter titles mentioned previously, we search the youtube api for 5 videos including their title, description and the url link. Further on google scholar we use those search terms and again return as many pdfs their are on the first page

# The architecture

# Perligo Scraper

This class is used to scrape through the perligo website, it initially starts off with a constructor that takes in that ISBN in the form of a string, through the constructor we also create selenium webdriver

The following method is the most important ones: 

* Loadwebpage: This method loads the website, is responsible for waiting till the objects are visible and then clicking on cookie acceptance and the table of contents

* soupingthecontent: Whereas once we're on the table contents this method is responsible for looking in the children of this PageElement and find all PageElements that match the given criteria. Then once this is done it extracts the text from each given PageElement and returns everything

# Data Cleaner

Alongside perligo scraper there is a datacleaner.py which is responsible for cleaning the table of contents for anything we do not desire, Currently i've come across 4 undesirable content that I wouldn't want in

1. Looking at the table of content of a particular book what we don't want is anything after the other books you may enjoy section so it removes that from the contents Hence inspired strip_other_books method
2. Strip preface and introduction from table of content, which is the strip_preface_introduction method
3. Remove anything after and including the appendix from the table of content, which is remove_appendix_from_list
4.  Remove chapter and section from title chapters in table of content for example 'chapter 9. memory managment' would be outputted as 'memory managment' remove_chapter_section_from_str method 


