import xml.etree.ElementTree as ET


def Read(File):
    tree = ET.parse(File)
    root = tree.getroot()
    Album_Count = Count_Album('Album.xml')
    Album_List = [[0 for i in range(3)] for j in range(Album_Count)]

    for i in range(0, Album_Count):
        Album = root[0][i]
        Album_List[i][0] = Album.attrib['Name']
        Album_List[i][1] = Album[0].text
        Album_List[i][2] = Album[1].text
        # print(Album_ID, Album_Name, Newest_TraickID)

    return Album_Count, Album_List


def Check_New(TrackID, History_ID):
    i = 0
    is_new = True
    new_id = []
    while is_new and i < 30:
        if TrackID[i] > History_ID:
            new_id.append(TrackID[i])
            i = i + 1
        else:
            is_new = False

    return new_id


def Updata_New(New_ID, File, count):
    tree = ET.parse(File)
    root = tree.getroot()

    ID = root[0][count + 0][1]
    # print(ID.text)
    ID.text = str(New_ID[0])
    # print(ID.text)

    tree.write("Album.xml", encoding="utf-8", xml_declaration=True)


def Count_Album(File):
    tree = ET.parse(File)
    root = tree.getroot()

    count = 0
    for i in root.iter('Album'):
        count = count + 1
    return count
