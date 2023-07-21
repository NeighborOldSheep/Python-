import urllib.request 

#下载网页
""" url_page = 'http://www.baidu.com' """

# url代表下载的路径   filename代表的是文件的名字
# 在python中 可以写变量的名字  也可以直接写值
""" urllib.request.urlretrieve(url_page,'baidu.html') """

#下载图片
""" 
url_img = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.i-scmp.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F1200x800%2Fpublic%2Fd8%2Fimages%2Fmethode%2F2020%2F06%2F10%2F8e352e96-a96e-11ea-bf1b-7541df8028ff_image_hires_114359.jpg%3Fitok%3DX0DUcXW-%26v%3D1591760644&imgrefurl=https%3A%2F%2Fwww.scmp.com%2Fmagazines%2Fstyle%2Fcelebrity%2Farticle%2F3088361%2Fend-blackpink-we-know-it-rose-lisa-and-jisoo-all-reveal&tbnid=FfO0nKaEqWCviM&vet=12ahUKEwiusefq-cf9AhU0NUQIHS-3D14QMygOegUIARDSAQ..i&docid=L92S78NtRio5dM&w=1200&h=800&q=blackpink&ved=2ahUKEwiusefq-cf9AhU0NUQIHS-3D14QMygOegUIARDSAQ'
urllib.request.urlretrieve(url=url_img,filename='blackpink.jpg') 
"""

#下载视频
url_video = 'https://v3-dy-o.zjcdn.com/23e14d47fe622a2dfa8d3f06677750e9/6406422b/video/tos/cn/tos-cn-ve-15c001-alinc2/okQH0hVerA0Fd7X2AQ4G3AaP22Vhf3AHBBCfuo/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=792&bt=792&cs=2&ds=3&ft=pP-tGY28Qjju9wfMtR-9Q6C~Yw98ImApx3bi7S6BJE&mime_type=video_mp4&qs=15&rc=ZTxpNztmaDg7ZTdnNTY2M0Bpamp4MzM6ZmgzaTMzNGkzM0BfYy1iMzRjX18xLTA1YTUtYSNlc2lpcjRvMmtgLS1kLWFzcw%3D%3D&l=20230307024225E622E93465E1672E420F&btag=8000&cc=1f'

urllib.request.urlretrieve(url_video,'guishidong.mp4')