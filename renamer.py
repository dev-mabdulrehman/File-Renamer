import os,time

def getFileCreatedDate(filename,path=None):
    if path is None:
        path = os.getcwd()
    SRC = path + "\\" + filename
    return str(time.ctime(os.path.getmtime(SRC)))
def dateTimeToFileName(dateTime):
    dateTime = dateTime.split(" ")
    dateTime[0],dateTime[2],dateTime[-1],dateTime[-2] = dateTime[2],dateTime[-1],dateTime[-2],dateTime[0]
    dateTime[0] = dateTime[0] + dateTime[1] + dateTime[2]
    del dateTime[1],dateTime[1]
    dateTime[-1] = dateTime[-1].replace(":","-")
    filename = "_".join(dateTime)
    return filename
def listFiles(path):
    fileNames = sorted(os.listdir(path))
    return fileNames
def renameFiles(fileNames,path):
    IsRenamed = []
    FileNames = []
    for fileName in fileNames:
        EXT = fileName.split(".")[-1]
        SRC = path + "\\" + fileName
        DST = path + "\\" + dateTimeToFileName(getFileCreatedDate(fileName,FOLDER_PATH))
        TEMP_DST = DST
        try:
            FileNames.append(DST)
            DST = addFileExtension(DST,EXT)
            os.rename(SRC,DST)
            IsRenamed.append(True)
        except FileExistsError:
            index = FileNames.count(TEMP_DST)
            TEMP_DST = TEMP_DST + "_" + str(index)
            TEMP_DST = addFileExtension(TEMP_DST,EXT)
            os.rename(SRC,TEMP_DST)
            IsRenamed.append(True)
    return IsRenamed
def getFilesDetail(renameDetail):
    if all(renameDetail):
        print("All files Renamed Successfully.")
    elif sum(renameDetail):
        numOfFilesRenamed = sum(renameDetail)
        filesNotRenamed = len(renameDetail) - numOfFilesRenamed
        print(f"{numOfFilesRenamed} files has been Renamed Successfully.")
        print(f"{filesNotRenamed} files Renaming Failed.")
def addFileExtension(filename,fileExtension):
    return filename + "." + fileExtension

if __name__ == "__main__":
    FOLDER_PATH = input("Enter Folder Path : ")
    fileNames = listFiles(FOLDER_PATH)
    renameDetail = renameFiles(fileNames,FOLDER_PATH)
    getFilesDetail(renameDetail)
