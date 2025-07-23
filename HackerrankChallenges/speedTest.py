import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
print("Download speed: {0}\nUpload speed: {1}".format(download, upload))
