import urllib.request
import re
for i in range(0,100,1):
  search_keyword="airplane+sound"
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  print("https://www.youtube.com/watch?v=" + video_ids[i])
  with open("links.txt", "a") as f:
    f.write("https://www.youtube.com/watch?v=" + video_ids[i]+"\n")
