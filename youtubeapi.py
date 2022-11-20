#%%
import googleapiclient.discovery
import googleapiclient.errors
import constants


api_service_name = "youtube"
api_version = "v3"
max_results = 5


def youtube_search_book_content(YoutubeSearchTerms: list):

    """
    Takes in the scraped book content after going through the data cleaner,
    searches for 5 particular youtube videos that comes up for that key term,
    then returns 5 videos for every associated search term

    PARAM: 
      YoutubeSearchTerms = List

    Output:
        Book content with associated videos 
        
    
    """
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey= constants.API_KEY)  
    search_Results = {}
    video_data = []
    
    #Using the book scraped search terms it will look for x max results of videos 
    for x in YoutubeSearchTerms:
        request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults= max_results,
        q=f"{x}"
    )
        response = request.execute()
        
        #once the response is excuted we will look through each response and take thhe video ID, TITLE AND DESCRIPTION
        for i in range(0,max_results):
            print(i)
            video_id = response['items'][i]['id']['videoId']
            print(video_id)
            video_title = response['items'][i]['snippet']['title']
            print(video_title)
            video_description = response['items'][i]['snippet']['description']
            print(video_description)
            video_data.append([video_title, video_description, video_id])
        
        #Now the new video data must be associated with the key term 
        search_Results[f'{x}'] = video_data
        video_data = []

    return search_Results      

if __name__ == "__main__":
   search = youtube_search_book_content(['genetic algorithms']) 
   print(search)

# %%
