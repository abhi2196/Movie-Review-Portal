import pprint
import urllib.request, json


def upcoming():
    fd = open("data3.txt",'w')
    fd.truncate()
    for i in range(1,10):
        
        url = "http://api.themoviedb.org/3/movie/upcoming?api_key=85985390077f25b10937d6d06a3213be&page="+str(i)
        response = urllib.request.urlopen(url)
        l = response.read()
        s = l.decode('utf-8')
        data = json.loads(s)
        for item in data['results']:
            if item["overview"] is None:
                item["overview"] = "No Information Available"
            info =  {
                  "title": item["original_title"],
                  "overview": item["overview"],
                  "Release_date":item["release_date"],
                  "genre":item["genre_ids"],
                   "Rating": item["vote_average"]
                  }
            fd.write(info["title"]+"\t"+info["overview"]+"\t"+info["Release_date"]+"\t"+str(info["Rating"])+"\n")
        
def now_playing():
    fd=open("data4.txt",'w')
    fd.truncate()
    for i in range(1,43):        
        url = "http://api.themoviedb.org/3/movie/now_playing?api_key=85985390077f25b10937d6d06a3213be&page="+str(i)
        response = urllib.request.urlopen(url)
        l = response.read()
        s = l.decode('utf-8')
        data = json.loads(s)
        for item in data['results']:
            if item["overview"] is None:
                item["overview"] = "No Information Available"
            info =  {
                    "title": item["original_title"],
                    "overview": item["overview"],
                    "Release_date":item["release_date"],
                    "genre":item["genre_ids"],
                    "Rating": item["vote_average"]
                  }
            fd.write(info["title"]+"\t"+info["overview"]+"\t"+info["Release_date"]+"\t"+str(info["Rating"])+"\n")

upcoming()
now_playing()
print ("Data Extracted Successfully!!")
