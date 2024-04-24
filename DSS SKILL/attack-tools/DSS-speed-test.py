import speedtest

print("_"*80)

print("."*80)
print("please wait...")
print("."*80)

speed = speedtest.Speedtest()
DownloadSpeed = speed.download()
UploadSpeed = speed.upload()

print("-"*80)
print('downlad speed: {DownloadSpeed}')
print('upload speed: {UploadSpeed}')
print("-"*80)
