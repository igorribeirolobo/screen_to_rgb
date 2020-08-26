def aciona_curl(url):
    import pycurl
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.perform()
    curl.close()

ant = None
while 1 == 1:
    import pyscreenshot as pys
    from PIL import Image
    import time

    time.sleep(3)
    image = pys.grab()
    image.save('cap.png', 'png')
    img = Image.open("cap.png")
    cores = img.convert('RGB').getcolors(maxcolors=1000000)
    i = None
    qtd = 0

    for cor in cores:
        for arr in cor:
            if isinstance(arr, int):
                if qtd < arr:
                    qtd = arr
                    i = cor[1]
    if i != ant:
     ant = i
     aciona_curl("https://maker.ifttt.com/trigger/luzQuarto/with/key/i5kKJT2fgs3xw18-KmCycvsZQ7SWBrX2xpH-Hh2yyft")
