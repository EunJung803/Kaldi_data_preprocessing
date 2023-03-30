import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = 'C:\\Users\\jeong\\Desktop\\사진\\pictures'
file_names = os.listdir(file_path)
file_names
# >>> ['photo-1577055209976-ddae617a8023.jpg', 'photo-1577255714682-69db9b067fda.jpg', ..., 'photo-1579122549707-440e9edc4a6d.jpg']

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = '1000' + str(i) + '_' + '001' + '000' + str(i) + ''
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

############

# 01001_500_0001
# 스피커ID_폴더번호_순서

# 스피커ID = 10001 부터 시작 / 001 = 폴더번호 / 순서 = 0001 부터 시작
# 10001_001_0001

import os
import glob

def rename_flac(path, files):
    for i, f in enumerate(files):
        ftitle, fext = os.path.splitext(f)  # ftitle = 원래 파일 이름 , fext = 파일 확장자 (.flac, .txt) 으로 split해서 들어감
        if(fext == '.flac') :   # 음성 파일이면
            # 파일명 재구성 -> 스피커ID_폴더번호_순서 + 파일 확장자
            os.rename(f, '1000{}'.format(i+1) + '_' + '001' + '_' +'{0:04d}'.format(i+1) + fext)
    
def rename_txt(path, files):
    for j, f in enumerate(files):
        ftitle, fext = os.path.splitext(f)
        if(fext == '.txt') :   # txt 파일이면
            # 파일명 재구성 -> 스피커ID_폴더번호_순서 + 파일 확장자
            os.rename(f, '1000{}'.format(j+1) + '_' + '001' + '_' +'{0:04d}'.format(j+1) + fext)


if __name__ == '__main__':
    path = "./testdir"
    files = glob.glob(path + '/*')
    rename_flac(path, files)
    rename_txt(path, files)