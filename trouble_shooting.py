accident = "故障中"
#if文の繰り返しを避けるために、リスト化
steps = [
    "電源ついた？（y/n）",
    "関連部品は壊れてない？（y/n）",
    "ソフトのバージョンはあってる？（y/n）",
    "ソフトはハードと連携してる？（y/n）",
    "詳しい人に聞いた？（y/n）"
]
#while文で状態をfor文で決まった回数のループを行う
while accident == "故障中":
    for step in steps:
        ans = input(step + " : ").strip().lower()
        if ans == "y":
            print(" 治ってよかったね")
            accident = "復旧"
            break
    else:
        # forが全部終わってもbreakしなかった場合
        print(" まだ治らないね…全部試したら詳しい人に相談しよう！")
        break
