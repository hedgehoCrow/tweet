# coding: UTF-8

def get(id):
    if id==200 or id==201 or id==202 or id==210 or id==211 or id==212 or id==221 or id==230 or id==231 or id==232:
        return "雷雨"
    elif id==300 or id==301 or id==302 or id==310 or id==311 or id==312 or id==313 or id==314 or id==321:
        return "霧雨"
    elif 500:
        return "小雨"
    elif 501:
        return "雨"
    elif 502:
        return "強い雨"
    elif 503:
        return "豪雨"
    elif 504:
        return "極端に強い雨"
    elif id==511 or id==520 or id==521 or id==522 or id==531:
        return "シャワーのような雨"
    elif 600:
        return "小雪"
    elif 601:
        return "雪"
    elif 602:
        return "大雪"
    elif id==611 or id==612:
        return "みぞれ"
    elif id==615 or id==616:
        return "雨と雪が降る"
    elif id==620 or id==621 or id==622:
        return "シャワーのような雪"
    elif id==701 or id==721 or id==741:
        return "霧"
    elif id== 731 or id==751:
        return "砂塵が舞う"
    elif id== 761 or id==711:
        return "ほこりっぽい"
    elif 762:
        return "火山灰"
    elif 771:
        return "スコール"
    elif id==781 or id==900 or id==902:
        return "竜巻"
    elif 800:
        return "晴れ"
    elif id==801 or id==802 or id==803 or id==804:
        return "曇り"
    elif 901:
        return "熱帯暴雨"
    elif 903:
        return "かなり冷え込む"
    elif 904:
        return "かなり暑い"
    elif 905:
        return "強風"
    elif 906:
        return "ひょうが降る"
    elif 951:
        return "比較的に大気の状態が穏やか"
    elif id==952 or id==953:
        return "風が吹き荒れる"
    elif id==954 or id==955 or id==956 or id==957 or id==958 or id==959:
        return "暴風"
    elif id==960 or id==961:
        return "嵐"
    elif 962:
        return "ハリケーン"
    else:
        return "現在の天気情報を取得できません"

