import os
import glob
import shutil

# os.chdir('/Users/eunjung/Documents/ai_speaker')

current_direct = os.listdir()  #현재 디렉토리

for i in current_direct:   #현재 디렉토리 내부에서 
    if 'KsponSpeech' in i:    #KsponSpeech 파일을 찾으면
        os.chdir('./KsponSpeech_01')       #KsponSpeech 폴더 안으로 이동
        path = os.getcwd()          #이동 후의 경로 저장

        scriptID = '0' + path.split('_')[-1]    #경로에서 '_'로 분리 후 뒷번호만 가져와서 앞에 0을 붙여 저장 (scriptID)
        print(scriptID)

        speakers = sorted(glob.glob(path + '/*'))  #이동 후의 경로 내부 모든 파일 경로 가져와서 리스트로 저장
        # print(speakers)

        for i in speakers:     #모든 파일들 중
            speakerID = i.split('_')[-1]     # '_'로 분리 후 뒷번호만 가져와서 저장 (speakerID)
            print(speakerID)


# file_source = os.listdir()
# print(file_source)

def grouping():
    file_source = os.getcwd()
    
    group_num = './001'
    os.makedirs(group_num, exist_ok=True)
    # get_files = os.listdir(file_source)

    for root, subdirs, files in os.walk(file_source):
        for f in files:
            if 'flac' or 'txt' in f:
                file_to_move = os.path.join(root, f)
                shutil.move(file_to_move, group_num)
