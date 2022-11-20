# BookContentToYoutubeVideos
scrape the table of content from a book and search using youtube using the chapter titles

So this is currently not going to be the best readme since i still have to finish this with a front facing application

Although the idea of this project, is given and educational books isbn number, it will scrape perlego for the books table of content then using that table of content
it will data cleaning it, into actual terms you can search on youtube

to example the secondary takes the isbn of the books and returns the table of contents and cleans the html from it
the data cleaner cleans the titles and book content parts that we don't need and don't  desire
the youtubeapi then takes the scraped book content and searches each term on youtube and then creates a dictionary of search term, [video id, title, description]

What i have left to build is the front end that brings this all together

