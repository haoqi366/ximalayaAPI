import requests
from time import time
from json import loads


class NetWork:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Host': 'www.ximalaya.com',
        'If-None-Match': 'W/"2cc08-HvI5ufGZ9TNYyyZOgJLO8mPSV64"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.87 Safari/537.36'}

    def __init__(self):

        pass

    def getIndexAndID(self, albumID, page, sort, headers=headers):

        pageurl = 'http://www.ximalaya.com/revision/album/getTracksList?albumId={}&pageNum={}&sort={}'.format(albumID, page, sort)
        s = requests.session()
        ret = s.get(url=pageurl, headers=headers).content.decode('utf-8')
        j = loads(ret)
        return j

    def getDownloadUrl(self, trackId, headers=headers):

        s = requests.session()
        ret = s.get(url='http://www.ximalaya.com/revision/play/tracks?trackIds={}'.format(trackId),
                    headers=headers).content
        j = loads(ret)
        src = j['data']['tracksForAudioPlay'][0]['src']
        if src and src != "" and 'm4a' in src:
            return src
        else:
            print("Error:Wrong Src!,TrackID:", trackId)
            print('Src:', src)
            # exit()

    def getMediaFile(self, Download_URL, File_Path, File_Name, headers=headers):

        File_Name = str(File_Name) + '.' + Download_URL.split('.')[-1]
        start = time()
        MediaFile = requests.get(url=Download_URL, headers=headers)
        if MediaFile.status_code != requests.codes.ok:
            print("Error:Download wrong! Src:", Download_URL)
            exit()
        MediaFile_Path = File_Path + '\\' + File_Name
        Write_File = open(MediaFile_Path, "wb")
        Write_File.write(MediaFile.content)
        Write_File.close()
        end = time()
        print("File {} Download Success. Use {} seconds.".format(File_Name, end - start))

        return MediaFile_Path


class ExtractData:
    def __init__(self):

        pass

    def extracTrackID(self, Data):

        tracks = Data['data']['tracks']

        TrackID = []

        for track in tracks:
            TrackID.append(track['trackId'])

        return TrackID

    def extracProgramName(self, Data):

        tracks = Data['data']['tracks']

        ProgramName = []

        for track in tracks:
            ProgramName.append(track['title'])

        return ProgramName

    def extracDownloadUrl(self, TrackID):

        Download_URL = []

        for Track in TrackID:
            Download_URL.append(NetWork.getDownloadUrl("Test", Track))
            # time.sleep(1)

        return Download_URL
