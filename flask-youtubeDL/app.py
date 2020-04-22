from appVar import *
from flask import Flask, request, render_template, flash, redirect, url_for
import os
import sys

app = Flask(__name__)

def mkScratchFolder(dir):
    scratchDir = dlDir+dir
    try:
      os.mkdir(scratchDir)
    except OSError:
      print ("Failed to create Scratch Dir: {}".format(scratchDir))
    else:
      print("Successfully created: {}".format(scratchDir))
    return scratchDir

def dlPlaylist(url,dir):
  scratchDir = mkScratchFolder(dir)
  ytdl_cmd = "youtube-dl {} -o '{}/{}' {}".format(ytdl_flags, scratchDir, fileFormat, url)
  #print(ytdl_cmd)
  os.system(ytdl_cmd)



@app.route('/')
def main():
  return render_template('dl.html')

@app.route('/process',methods=['POST'])
def process():
  _dirName = request.form.get('dirName')
  _playlistURL = request.form.get('playlistURL')
  if _playlistURL:
    dlPlaylist(_playlistURL, _dirName)
    return render_template('dlresponse.html', playlistURL=_playlistURL, dirName=_dirName)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')


### Pending Items
# do check on url before running
# check to make sure there is not a youtube-dl python module
# work on DockerFile
