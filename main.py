__author__ = '1'

import os

TRACK_SUBTITLES_EN_ID = "18"
TRACK_SUBTITLES_RU_ID = "17"
PATH_FILE_MKV = "D:\downloads\\1.mkv"
PATH_FILE_SUBTITLES_EN = "Subtitles_en.srt"
PATH_FILE_SUBTITLES_RU = "Subtitles_ru.srt"
PATH_FILE_SUBTITLES_EN_RU = "Subtitles_en_ru.srt"
MKVEXTRACT = "D:\distr\mkvtoolnix\mkvextract.exe"

ID = "id"
CONTENT= "content"
TIME = "time"
END = "end"

def extractSubtitle(trackID, fileSubtitle):
    os.system(
        MKVEXTRACT +
        " tracks " +
        PATH_FILE_MKV +
        " " + trackID +
        ":" + fileSubtitle)

def getListLinesFromFile(file):
    with open(file) as f:
        lines = f.readlines()
        f.close()
    return lines


def writeLineWithKey(dict, line):
    key = CONTENT
    if not dict.has_key(ID):
        key = ID
    elif not dict.has_key(TIME):
        key = TIME

    if dict.has_key(CONTENT):
        dict[key] += (line)
    else:
        dict[key] = line

def getSubtitles(file):
    lines = getListLinesFromFile(file)
    temp = {}
    result = []
    for i in xrange(len(lines)):
        line = lines[i]
        if line == "\n":
            temp[END] = line
            result.append(temp)
            temp = {}
        else:
            writeLineWithKey(temp, line)
    return result

def writeLine(out, lineEN, lineRU):
    out.write(lineEN.get(ID))
    out.write(lineEN.get(TIME))
    out.write(
        lineEN.get(CONTENT) +
        lineRU.get(CONTENT)
    )
    out.write(lineEN.get(END))
    out.flush()

#extractSubtitle(trackSubtitlesEN, fileSubtitlesEN)
#extractSubtitle(trackSubtitlesRU, fileSubtitlesRU)

linesEN = getSubtitles(PATH_FILE_SUBTITLES_EN)
linesRU = getSubtitles(PATH_FILE_SUBTITLES_RU)

with open(PATH_FILE_SUBTITLES_EN_RU, "w") as out:
    for i in xrange(len(linesEN)):
        writeLine(out, linesEN[i], linesRU[i])
    out.close()