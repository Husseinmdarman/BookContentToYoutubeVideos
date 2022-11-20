#%%
import googleapiclient.discovery
import googleapiclient.errors
import constants


api_service_name = "youtube"
api_version = "v3"
max_results = 5


def youtube_search_book_content(YoutubeSearchTerms: list):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey= constants.API_KEY)  
    search_Results = {}
    video_data = []

    for x in YoutubeSearchTerms:
        request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults= max_results,
        q=f"{x}"
    )
        response = request.execute()
        
        for i in range(0,max_results):
            print(i)
            video_id = response['items'][i]['id']['videoId']
            print(video_id)
            video_title = response['items'][i]['snippet']['title']
            print(video_title)
            video_description = response['items'][i]['snippet']['description']
            print(video_description)
            video_data.append([video_title, video_description, video_id])
        search_Results[f'{x}'] = video_data
        video_data = []

    return search_Results      

if __name__ == "__main__":
   search = youtube_search_book_content(['genetic algorithms']) 
   print(search)
  # print(search['genetic algorithms']['items'][0]['id']['videoId'])
   #print(search['genetic algorithms']['items'][0]['snippet']['title'])
  # print(search['genetic algorithms']['items'][0]['snippet']['description'])     
   

# %%
