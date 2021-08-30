from Download import NetWork, ExtractData
import Trains
import random
from time import sleep

netWork = NetWork()
extractData = ExtractData()

album = int(input('album ID:'))
pages = int(input('pages:'))
totel = int(input('totel:'))

Ran_TrackID = []

for count in range(0, totel):
    page = random.randint(1, pages)

    IndexAndID = netWork.getIndexAndID(album, page, 1)

    TrackId = extractData.extracTrackID(IndexAndID)
    Ran_TrackID.append(random.choice(TrackId))

Download_URL = extractData.extracDownloadUrl(Ran_TrackID)
print(Ran_TrackID)

for i in range(0, len(Download_URL)):
    if Download_URL[i] == 0:
        continue
    filepath = netWork.getMediaFile(Download_URL[i], "C:\\Users\\gavin\\Documents\\Coding\\file", Ran_TrackID[i])
    Trains.trains_to_any(filepath, 'mp3')
    # print(Ran_TrackID)

