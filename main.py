from Download import NetWork, ExtractData
import FileIO
import Trains
from time import sleep


netWork = NetWork()
extractData = ExtractData()

Album_Count, Album_List = FileIO.Read('Album.xml')

for i in range(0, Album_Count):

    print(Album_List[i][0])

    IndexAndID = netWork.getIndexAndID(Album_List[i][1], 1, 1)

    TrackId = extractData.extracTrackID(IndexAndID)

    Program_Name = extractData.extracProgramName(IndexAndID)

    new_track_ids = FileIO.Check_New(TrackId, int(Album_List[i][2]))

    if len(new_track_ids) == 0:
        print("No new program")
        continue
    else:
        FileIO.Updata_New(TrackId, 'Album.xml', i)
        print('Find new program.')

    Download_URL = extractData.extracDownloadUrl(new_track_ids)

    if len(new_track_ids) == len(Download_URL):
        Program_count = len(Download_URL)

    for i in range(0, len(Download_URL)):
        filepath = netWork.getMediaFile(Download_URL[i], "C:\\Users\\gavin\\Documents\\Coding\\test", Program_Name[i])
        Trains.trains_to_any(filepath, 'mp3')
        sleep(1)
