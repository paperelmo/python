# python crawl a web xml file and extract its attributes
# YouTube timetext
# using requests, ElementTree
# encoding: utf-8
# python 3.6
import requests
import xml.etree.ElementTree as ET

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

def lang_list(yid):
    res=requests.get("https://video.google.com/timedtext?type=list&v="+yid, headers=header)  # using requests to get the content
    tree=ET.fromstring(res.text.encode('utf-8'))    #formatting
    docid=tree.attrib['docid']  #the most outside tag's attrib
    for sth_attrs in tree.iter(tag = 'track'):  #loop all same name of tag e.g.'track'
        track_id=sth_attrs.attrib['id'] #get the item of the attrib in the tag e.g.'id'
        lang_translated=sth_attrs.attrib['lang_translated']
        lang_code=sth_attrs.attrib['lang_code']
        # print (track_id, lang_translated, lang_code)
        if (lang_translated=='English'):
            return docid, track_id, lang_translated, lang_code
        elif (lang_translated=='English (United Kingdom)'):
            return docid, track_id, lang_translated, lang_code

def timetext(lang_code, yid):
    res=requests.get("https://video.google.com/timedtext?lang="+lang_code+"&v="+yid, headers=header)  # using requests to get the content
    tree=ET.fromstring(res.text.encode('utf-8'))    #formatting
    for fact in tree.iter(tag = 'text'):    #loop all same name of tag e.g.'text'
        start=fact.attrib['start']  #get the item of the attrib in the tag e.g.'start'
        dur=fact.attrib['dur']
        subtitle=fact.text  #get the item of the tag
        print (start, dur, subtitle)

def main():
    yid='XJGiS83eQLk'
    # yid='WOxr2dmLHLo'    
    # lang_list('tCXGJQYZ9JA')  # Taylor Swift - Delicate
    # lang_list('K3IhW8uPH0U')    # How to Download Subtitles/CC from YouTube
    # lang_list('WOxr2dmLHLo')    # How to add subtitles to a YouTube video
    # lang_list('XJGiS83eQLk')    # Creating Subtitles and Closed Captions on Your Youtube Videos
    docid, subtitle_id, lang_translated, lang_code=lang_list(yid)
    print (subtitle_id, lang_translated, lang_code)
    timetext(lang_code, yid)
    
    

if __name__=="__main__":
        main()
