from os import path
import prepare as prep
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import json

if __name__ == "__main__":
    # フォントを全て読み込み
    fonts = set([f.name for f in fm.fontManager.ttflist])
    
    # 描画領域のサイズ調整
    plt.figure(figsize=(100,len(fonts)/4))
    
    # フォントの表示
    for i, font in enumerate(fonts):
        plt.text(0, i, f"日本語：{font}", fontname=font)
        
    # 見やすいように軸を消す
    plt.ylim(0, len(fonts))
    plt.axis("off")
        
    plt.show()