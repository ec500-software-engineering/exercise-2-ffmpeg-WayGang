from pytest import approx
import main

def test_duration():

    OrigV = './1video.mov'
    Conv480 = './1video_480p.mov'
    Conv720 = './1video_720p.mov'

    ffOri = main.ffprobe(OrigV)
    ff480 = main.ffprobe(Conv480)
    ff720 = main.ffprobe(Conv720)

    info_in = float(ffOri['streams'][0]['duration'])
    info_480 = float(ff480['streams'][0]['duration'])
    info_720 = float(ff720['streams'][0]['duration'])

    assert info_in == approx(info_480)
    assert info_in == approx(info_720)

if __name__ == '__main__':
    test_duration()


