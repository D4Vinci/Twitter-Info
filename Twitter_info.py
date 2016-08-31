#Author:D4Vinci
from bs4 import BeautifulSoup as So
import urllib ,sys

def get(twitter):
    try:
        u = urllib.urlopen(twitter)
        data = u.read()
        s = So(data, 'html.parser')
        details = s.find_all("span" ,{"data-is-compact":"false"})
        following = details[1].text.encode("utf-8")
        name = s.find("a" ,{"href":"/"+twitter.split("/")[-1]}).text.encode("utf-8").replace("  ","").replace("\n","")
        followers = details[2].text.encode("utf-8")
        likes = details[3].text.encode("utf-8")
        pic = s.find("a" ,{"class":"ProfileAvatar-container u-block js-tooltip profile-picture"})["href"].encode("utf-8")
        date = s.find("span" ,{"class":"ProfileHeaderCard-joinDateText js-tooltip u-dir"})["title"].encode("utf-8")
        print " Name : " + name
        print " Following : " + following
        print " Followers : " + followers
        print " Likes : " + likes
        print " This Account made in : " + date
        print " Full Profile Picture : " + pic
    except:
        print "Error <Twitter_Profile_link>/<username> is not correct"
        sys.exit(0)


try:
    u = sys.argv[1]

except:
    print "\n [*] Error :"
    print " [*] Usage : "+sys.argv[0].split("\\")[-1] +" <Twitter_Profile_link>/<username>"
    sys.exit(0)


if "twitter.com" not in u:
    get("https://twitter.com/" + u)
else:
    get(u)
