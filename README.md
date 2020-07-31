# SendEmailByPython

### pyinstaller를 통한 python exe 실행파일 빌드
[pyinstaller를 이용한 Python exe 실행 파일 만들기](https://hongku.tistory.com/338)
```bash
$ pip install pyinstaller

$ pyinstaller -F --icon=youngbee.ico main.py

# -w 옵션 넣으면, cmd 창이 뜨지않고 백그라운드로 실행
$ pyinstaller -w -F main.py 
```
