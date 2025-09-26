# upgraded 폴더의 파일 구조를 실행하는 예시 파일
import os

def list_upgraded_files():
    base_path = os.path.dirname(os.path.abspath(__file__))
    upgraded_path = os.path.join(base_path)
    print('upgraded 폴더 내 파일 및 폴더 구조:')
    for root, dirs, files in os.walk(upgraded_path):
        level = root.replace(upgraded_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

if __name__ == '__main__':
    list_upgraded_files()
