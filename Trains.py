# from pydub import AudioSegment
# from time import time
#
#
# def trains_to_any(filepath, source_audio_type, output_audio_type):
#     print("Trains start...")
#     start = time()
#     songs = AudioSegment.from_file(filepath, source_audio_type)
#     filename = filepath.split('.')[0]
#     songs.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")
#     end = time()
#     print("Train success,use", end - start, "seconds")

import re
import subprocess
from time import perf_counter


def get_seconds(time):
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:8])
    ms = int(time[9:12])
    ts = (h * 60 * 60) + (m * 60) + s + (ms / 1000)
    return ts


def trains_to_any(filepath, output_file_type):
    output_file_folder = ''
    output_file_name = ''
    for i in range(0, filepath.count('\\')):
        output_file_folder = output_file_folder + filepath.split('\\')[i] + '\\'
    temp_output_file_name = filepath.split('\\')[-1]
    for i in range(0, temp_output_file_name.count('.')):
        output_file_name = output_file_name + temp_output_file_name.split('.')[i] + '.'
    output_file = output_file_folder + output_file_name + output_file_type

    cmd = ['ffmpeg.exe', '-i', filepath, output_file]

    # print(str(cmd))
    start_time = perf_counter()

    process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8',
                               text=True)

    for line in process.stdout:
        duration_res = re.search(r'\sDuration: (?P<duration>\S+)', line)

        if duration_res is not None:
            duration = duration_res.groupdict()['duration']
            duration = re.sub(r',', '', duration)

        result = re.search(r'\stime?=(?P<time>\S+)', line)
        if result is not None:
            elapsed_time = result.groupdict()['time']
            progress = (get_seconds(elapsed_time) / get_seconds(duration)) * 100
            # print(elapsed_time)
            progress = round(progress, 2)
            print("\r", end="")
            print("转换进度:{}% , {} , 已用{}秒".format(progress, "▋" * (int(progress) // 2),
                                               round(perf_counter() - start_time, 2), end=""), end="")

    process.wait()
    print('\n')
    if process.poll() == 0:
        print("success")
    else:
        print("error:")
