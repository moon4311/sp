import os
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if len(full_filename)>255:
                return

            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]  # 파일과 확장자 분리 중 확장자
                if ext == '.py':  # full_filename.endswith(".py")
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")