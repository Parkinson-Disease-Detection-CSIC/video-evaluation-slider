import csv
from functools import cache

def get_url_from_id(video_id):
    return "https://drive.google.com/file/d/" + video_id + "/preview"

@cache
def get_video_urls():
    video_urls = {}
    with open('videos.csv') as videos_csv:
        csv_reader = csv.reader(videos_csv, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                subject = int(row[0])
                exercise = row[1]
                video_id = row[2]

                if subject in video_urls:
                    videos_dict = video_urls[subject]
                else:
                    videos_dict = {}
                videos_dict[exercise] = get_url_from_id(video_id)
                video_urls[subject] = videos_dict
    return video_urls
