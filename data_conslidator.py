import perligo_scraper
import youtubeapi
import google_scholar_scraper
import datacleaner

class data_conslidator():
    
    def __init__(self, isbn_number: int):
        """
        Consolidates the data across the main three areas which are perligo book table contant
        youtube video searches based on topic and finally the academic papers assocatied with topics
        """
        scarpethis = perligo_scraper.scrapebook(isbn_number)
        scarpethis.loadwebpage()
        table_of_content = scarpethis.soupingthecontent()
        data = datacleaner.strip_other_books(table_of_content)
        data = datacleaner.remove_appendix_from_list(data)
        data = datacleaner.remove_chapter_section_from_str(data)
        data = datacleaner.strip_preface_introduction(data) # the book table content

        #using book table chapters to find youtube videos related
        search = youtubeapi.youtube_videos.youtube_search_book_content(data)

        scholar_data = {}
        
        for topic in data:
           key_word_search = google_scholar_scraper.ScholarScraper(topic)
           key_word_search.open_webpage()
           key_word_search.get_pdf_files()

           #the academic papers used for topics
           scholar_data[f'{topic}'] = key_word_search.get_pdf_files()
        
        #consolidate form of data which the api can return
        self.data = {'book_isbn_number': isbn_number ,
                     'Chapter titles': data, 
                     'youtube_videos': search , 
                     'academic_papers': scholar_data }
        
    def get_data(self):
        """
        Method to return all the consolidated data
        """    
    
        return self.data

    
