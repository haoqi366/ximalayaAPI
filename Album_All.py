from Download import NetWork, ExtractData
import Trains
from time import sleep

netWork = NetWork()
extractData = ExtractData()

album = int(input('album ID'))
pages = int(input('pages'))


for page in range(0, pages):
    IndexAndID = netWork.getIndexAndID(album, page, 0)

    TrackId = extractData.extracTrackID(IndexAndID)
    Program_Name = extractData.extracProgramName(IndexAndID)

    # URLS = extractData.extracDownloadUrl(TrackId)

    for i in range(0, len(Program_Name)):
        filepath = netWork.getMediaFile(URLS[i], "C:\\Users\\gavin\\Documents\\Coding\\file", Program_Name[i])
        # Trains.trains_to_any(filepath, 'mp3')
        sleep(1)
        print(Program_Name[i])



