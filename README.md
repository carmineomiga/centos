# CentOS

CentOS7.x 설치 이후 필요한 스크립트를 작성하는 리포지터리 입니다.

- scripts : bash script가 모여있는 경로입니다.
- pytyon 

## CentOS Bash 설정
~/.bashrc 파일 내부에 아래코드가 작성되어 있어야 합니다.
```bash
source /home/$USER/centos/env/init.env
source /home/$USER/cenots/env/help.env
```

install.sh 를 실행하면 자동으로 추가됩니다.
