import os
import glob
import shutil

# 파일 명 변환 함수
def rename_file(speakers_each, speakerID, scriptID):
    os.chdir(speakers_each)     # speakerID 속으로 이동
    current_path = os.getcwd()  # 해당 경로 저장
    files = sorted(glob.glob(current_path + '/*'))  # speakerID 내부에 있는 모든 음성파일 및 텍스트파일 리스트로 정렬해서 저장

    for f in files:
        ftitle, fext = os.path.splitext(f)        # ftitle = 원래 파일 이름 , fext = 파일 확장자 (.flac, .txt) 으로 split해서 들어감
        speak_seq_long = ftitle.split('_')[-1]    # ftitle에서 '_'으로 분리한 것 중 마지막 부분 = 발화순번 000001 부터
        # print(speak_seq_long)
        speak_seq = '0' + speak_seq_long[3:]      # 000001 -> 0001로 저장
        # print(speak_seq)

        if(fext == '.flac'):    # flac 파일명 변환
            new_name = scriptID[-1] + speakerID + '_' + scriptID + '_' + speak_seq + fext
            os.rename(f, os.path.join(current_path, new_name))

        if(fext == '.txt'):     # txt 파일명 변환
            new_name = scriptID[-1] + speakerID + '_' + scriptID + '_' + speak_seq + fext
            os.rename(f, os.path.join(current_path, new_name))


# 새로운 폴더 생성 후 해당 폴더로 파일을 옮겨주는 함수
def grouping(new_group):
    file_source = os.getcwd()
    os.makedirs(new_group, exist_ok=True)

    for root, subdirs, files in os.walk(file_source):
        for f in files:
            file_to_move = os.path.join(root, f)
            file_to_new = os.path.join('./'+new_group, f)
            shutil.move(file_to_move, file_to_new)


# grouping 함수 작동 후 원래 있어야 하는 경로로 이동시켜주기
def move_files(move_file, move_dir):
    file_source = os.getcwd()
    source_path = os.path.join(file_source, move_file)
    dest_path = os.path.join(move_dir, move_file)
    shutil.move(source_path, dest_path)


# speakers, speakerID, scriptID 추출 함수
def get_ID():
    current_files = os.listdir()  # 현재 디렉토리 내 존재하는 파일들

    for i in current_files:   # 현재 존재하는 파일들 중
        if 'KsponSpeech' in i:    # KsponSpeech 파일을 찾으면
            os.chdir('./KsponSpeech_01')       # KsponSpeech 폴더 안으로 이동
            path = os.getcwd()                 # 이동 후의 경로 저장

            scriptID = '0' + path.split('_')[-1]    # 경로에서 '_'로 분리 후 뒷번호만 가져와서 앞에 0을 붙여 저장 (scriptID)

            speakers = sorted(glob.glob(path + '/*'))  # 이동 후의 경로 내부 모든 파일 경로 가져와서 리스트로 저장

            speakerID = [0 for i in range(len(speakers))]   # speakerID 배열 초기화
            for n, i in enumerate(speakers):     # 모든 파일들 중
                speakerID[n] = i.split('_')[-1]     # '_'로 분리 후 뒷번호만 가져와서 speakerID 배열에 저장 (speakerID)

    return speakers, speakerID, scriptID


# 실행
if __name__ == '__main__':
    speakers, speakerID, scriptID = get_ID()
    # 각 변수에 담긴 값 예시
    # speakers = ['/Users/eunjung/Documents/ai_speaker/KsponSpeech_01/hi_0001', '/Users/eunjung/Documents/ai_speaker/KsponSpeech_01/hi_0002', '/Users/eunjung/Documents/ai_speaker/KsponSpeech_01/hi_0003'] 
    # speakerID = ['0001', '0002', '0003'] 
    # scriptID = 001
    
    cur_dir = os.getcwd()   # 현재 디렉토리 경로 cur_dir에 저장
    # print(cur_dir)

    for i in range(len(speakerID)):     # 파일 순차대로 파일명 변환
        rename_file(speakers[i], speakerID[i], scriptID)
        grouping(speakerID[i])
        move_files(speakerID[i], cur_dir)

    current_files = os.listdir()    # 현재 존재하는 파일들 리스트로 current_files에 저장
    # print(current_files)

    # grouping -> move_files 후 남은 예전 이름을 가진 비어있는 폴더들 제거 (current_files에서 찾아서)
    for i in current_files:     
        if(i[0] == 'K'):
            os.rmdir(i)
    
    os.chdir('../') # 상위 디렉터리로 경로 이동 후
    os.mkdir(scriptID)  # scriptID를 가진 폴더 생성

    file_oldname = os.path.join(cur_dir)    # 이전 파일명의 경로 (/Users/eunjung/Documents/ai_speaker/KsponSpeech_01)
    file_newname_newfile = os.path.join("/Users/eunjung/Documents/ai_speaker/001")  #새로운 경로 지정
    os.rename(file_oldname, file_newname_newfile)   # scriptID 이름인 폴더로 옮기기
    
    