import os 
def unzipCodeFolder():
    os.system(f"unzip -q -P {os.environ.get('zippsw')} /opt/app-root/src/codes.zip -d /opt/app-root/src/codes")
if __name__ == "__main__":
    os.system("git pull")
    unzipCodeFolder()
    from codes.main import cron
    while True :
        cron()
        print(">>>>>> cron done.")
        time.sleep(40)
