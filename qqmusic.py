#coding=utf-8

import requests
import random
import json
import time

'''
    一。音乐的歌单主要入口地址
    Referer: https://y.qq.com/portal/playlist.html
    url = https://y.qq.com/portal/playlist.html


    从分类歌单开始下载每一个歌单的内容
    在从播放器中找音乐的stream、
    
    一、音乐下载地址
    http://dl.stream.qqmusic.qq.com/
    音乐media
    http://dl.stream.qqmusic.qq.com/C400000Md1wq0vnwzE.m4a?vkey=8C4D819829AA3DAF250BE11F49FAC4B83CAC91A7A390DA8F096B13851AEE898FA12C0CD9FA7E217531D12C19F22D4DEEB139566035BB3F79&guid=2177108040&uin=0&fromtag=66
    这个需要：
    filename：.m4a
    vkey=
    
    二。但是该请求有这些参数，如何设置
    songmid:
    filename:
    
    songmid:
    strMediaMid:组成filename
    
    三，下面这个请求可以获得songmid和strMediaMid
    这个是获取整个歌单的信息
    http://...
    需要dissid
    
    四。
    获取dissid
    


startUrl = 'https://{0}{1}{2}'

rnd = random.random()
sin = 0
ein = 29
headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
headers['referer'] = 'https://y.qq.com/portal/playlist.html'


    一。请求歌单首页获取所有的歌单信息 dissid


dissList = requests.get(startUrl.format(rnd,sin,ein),headers = headers).text
dissList = json.loads(dissList.strip('getPlaylist()'))
# print(dissList)

# diss_id_list = []

for i in dissList['data']['list']:
    # diss_id_list.append(i['dissid'])
    dissName = i['dissName']
    diss_id = i['dissid']


    二。通过disstid获取songmid,strMediaMid

headers['referer'] = '{0}'.format(diss_id_list[0])

diss_url = '{0}'
song = requests.get(diss_url.format(diss_id_list[0],headers = headers))
song = json.loads(song.strip('playlistinfoCallback()'))

song_num = 1
for s in song['cdlist'][0]['songlist']:
    # 获取songmid
    songmid = s['songmid']
    # 获取歌曲名
    songName = s['songname']
    # 获取songMediaMid
    songMediaMid = s['strMediaMid']
    # 获取filename
    filename = 'C400' + str(s['strMediaMid']) + '.m4a'

    
        三。获取vkey
    
    headers['referer'] = ''

    vkey_url = '{0}{1}'
    response = requests.get(vkey_url.format(songmid,filename),headers = headers).text
    response = json.loads(response.strip('MusicCallback()'))



    # 提取vkey
    for vk in response['data']['items']:
        vkey = vk['vkey']

        filenames = vk['filename']

        
            四。通过vkey下载音乐
        
        musicUrl = '{0}{1}'
        del headers['referer']
        music = requests.get(musicUrl.format(filenames,vkey),headers = headers ,stream = True).raw.read()
        with open('music/'+ songName + '.mp3','wb') as file:
            file.write(music)

        time.sleep(1)

    print('{0}歌单的第{1}歌：{2}'.format(dissName,song_num,songName))

    song_num += 1

    if sin < dissList['data']['sum']:
        sin += 30
        ein += 30
        rnd = random.random()
    else:
        break
'''


'''
    一。音乐的歌单主要入口地址,获取所有歌单的名称
    Referer: https://y.qq.com/portal/playlist.html
    url = https://y.qq.com/portal/playlist.html
'''

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

playListUrl = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg' \
      '?picmid=1' \
      '&rnd={0}&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5' \
      '&sin={1}&ein={2}'

headers['referer'] = 'https://y.qq.com/portal/playlist.html'

'''
参数：当前的
rnd: 0.9169429200872523
sin: 0
ein: 29
下一页的
rnd: 0.9796491680794395
sin: 30
ein: 59
'''

rnd = random.random()
sin = 0
ein = 29

# 页数
page = 1
while True:
    getPlayList = requests.get(playListUrl.format(rnd,sin,ein),headers = headers).text
    getPlayList = json.loads(getPlayList.strip('getPlaylist()'))

    # 获取sum
    sum = getPlayList['data']['sum']

    print('第{0}页'.format(page))

    for i in getPlayList['data']['list']:
        print(i['dissname'])
        # 获取dissid
        dissid = i['dissid']
        # print(dissid)

        '''
            二。进入每个歌单里面,获取每个歌单里面的音乐列表
        '''
        # headers每一次都有变化
        headers['referer'] = 'https://y.qq.com/n/yqq/playsquare/{0}.html'.format(dissid)

        # referer = 'https://y.qq.com/n/yqq/playsquare/4183606856.html'
        # playlistinfoUrl每一次都有变化
        playlistinfoUrl = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0' \
                          '&disstid={0}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        # playlistinfoUrl = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=4183606856&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        #                     'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=4150064206&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        '''
        参数
        这个是没有下一页的参数的
        但是url和refer不同
        '''
        playlistinfoCallback = requests.get(playlistinfoUrl.format(dissid),headers = headers).text
        # 获取的text变换为json格式
        playlistinfoCallback = json.loads(playlistinfoCallback.strip('playlistinfoCallback()'))

        # 获取每首歌的歌名
        for j in playlistinfoCallback['cdlist'][0]['songlist']:
            # 获取专辑名字,歌曲名字，id
            albumname = j['albumname']
            songname = j['songname']
            songmid = j['songmid']

            # print(albumname,songname,songmid)

            '''
                三。将歌曲添加到播放列表中
            '''
            # songmid 有
            filename = 'C400' + songmid + '.m4a'
            # jsonpCallback这是一个回调函数，里面都是随机数，不用管的
            headers['referer'] = 'referer: https://y.qq.com/portal/player.html'
            musicJsonCallbackUrl = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback016447392343914125&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback016447392343914125&uin=0' \
                                   '&songmid={0}' \
                                   '&filename={1}&guid=2177108040'

            musicJsonCallback = requests.get(musicJsonCallbackUrl.format(songmid,filename),headers = headers).text
            musicJsonCallback = json.loads(musicJsonCallback.strip('MusicJsonCallback016447392343914125()'))
            # 获得vkey
            vkey = musicJsonCallback['data']['items'][0]['vkey']
            # print(vkey)

            '''
                四。获取音乐的下载地址,点击浏览器中的Media就行
            '''
            del headers['referer']
            musicUrl = 'http://dl.stream.qqmusic.qq.com/{0}?vkey={1}&guid=2177108040&uin=0&fromtag=66'
            music = requests.get(musicUrl.format(filename,vkey),headers = headers,stream = True).raw.read()
            with open('music/' + songname + '.mp3','wb') as file:
                file.write(music)

            print('专辑：',albumname,'中音乐：',songname,'downloaded')

            # time.sleep(5)

    if ein < sum:
        page += 1
        sin += 30
        ein += 30
        rnd = int(random.random() * 1000)
    else:
        break


