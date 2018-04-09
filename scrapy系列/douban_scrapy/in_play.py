import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

def get_soup(url):
    urllib3.disable_warnings()  ###忽略警告
    re = requests.get(url, verify=False)
    set_num = 0
    ### 请求错误时重新请求5次，超过exit
    if re.status_code != 200 and re.status_code >= 400 and re.status_code < 500:
        exit("请求被禁止！错误码：" + re.status_code)
    while re.status_code != 200 and re.status_code >= 500:
        set_num = set_num + 1
        print("请求失败，正在重新请求，重新请求次数：" + set_num)
        re = requests.get(url, verify=False)
        if re.status_code == 200:
            break
        if set_num > 5:
            exit("重新请求超过5次，程序终止")
    soup = BeautifulSoup(re.text, 'lxml')
    return soup

class in_play():

    def __init__(self):
        self.url = "https://movie.douban.com/cinema/nowplaying/beijing/"

    def download_url(self):
        soup = get_soup(self.url)
        moive_list = soup.select('div[id=nowplaying] > div > ul > li > ul > li[class=poster] > a')
        moive_url = []
        for i in moive_list:
            moive_url.append(i.get("href"))
        #print(moive_url)
        return moive_url

    def get_desc(self,moive_url):
        try:
            soup = get_soup(moive_url)
            moive_name = soup.find('span',{'property':'v:itemreviewed'}).get_text()   #电影名
            #print(moive_name)
            moive_star = soup.find('strong',{'class':'ll','class':'rating_num'}).get_text()   #星级
            #print(moive_star)
            moive_img = soup.find('img',{'rel':'v:image'}).get('src')   #图片
            moive_director = soup.find('span',{'class':'attrs'}).get_text()   #导演
            moive_actor_list = []   #演员
            moive_actor = soup.select('span[class=actor] > span > a')
            for i in moive_actor:
                moive_actor_list.append(i.get_text())
            moive_type_list = []    #类型
            moive_type = soup.find_all('span',{'property':'v:genre'})
            for i in moive_type:
                moive_type_list.append(i.get_text())
            moive_runtime = soup.find('span',{'property':'v:runtime'}).get_text()   #时长
            moive_video = soup.find('a',{'class':'related-pic-video'}).get('href')  #预告影片
            moive_comments_list = []    #影评
            moive_comments = soup.select('div[id=hot-comments] > div > div > p')
            for i in moive_comments:
                moive_comments_list.append(i.get_text())
        except AttributeError as e:
            print('error!{}'.format(e))
            moive_star = '未获取到评分'
        moive_info = dict(name=moive_name, star=moive_star, img=moive_img, director=moive_director,
                          actor=moive_actor_list,mtype=moive_type_list,mtime=moive_runtime,video=moive_video,comments=moive_comments_list)
        return moive_info






# if __name__ == '__main__':
#     a = in_play()
#     moive_url = a.download_url()
#     print(a.get_desc(moive_url[0]))
