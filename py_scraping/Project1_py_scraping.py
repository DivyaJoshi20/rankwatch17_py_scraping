import urllib
import re

def crawl_names_save_csv():
    """
    This function crawls data from site and puts them in csv
    """

    country = ["indian", "american", "french", "german", "australian", "arabic", "christian", "english", "iranian", "irish"]
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z"]
    i = 0
    k = 0
    names_map = {}

    while i < len(country):
        while k < len(alpha):
            gi_url = 'https://www.babynamesdirect.com/baby-names/' + country[i] + '/' + 'girl' + '/' + alpha[k] + '/';
            b_url = 'https://www.babynamesdirect.com/baby-names/' + country[i] + '/' + 'boy' + '/' + alpha[k] + '/';
            g_req = urllib.urlopen(gi_url)
            b_req = urllib.urlopen(b_url)
            g_res = g_req.read()
            b_res = b_req.read()

            links = re.findall('"((http|ftp)s?://.*?)"', g_res)
            blinks = re.findall('"((http|ftp)s?://.*?)"', b_res)

            for link in links:
                if "babynamesdirect.com/girl/" in link[0]:
                    names_map[str(link[0].split("/")[-1])] = "girl"

            for link in blinks:
                if "babynamesdirect.com/boy/" in link[0]:
                    names_map[str(link[0].split("/")[-1])] = "boy"
            k = k + 1
        i = i + 1

    f = open("Baby_names.csv", 'w');
    for key in names_map:
        f.write(key + "," + names_map[key])
        f.write("\n");
    print ("CSV Updated..")
    f.close()

if __name__ == "__main__":
    crawl_names_save_csv()