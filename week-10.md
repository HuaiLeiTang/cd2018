# 第十週心得報告

## 40523145

利用pyslvs設計出兩個六連桿所結合的機構，以及它提球的軌跡須符合本身機構預先之設計，將設計好的pyslvs傳入2D的solvespace這時候就可以從solvespace看到提球機構線段的尺寸，當已知道尺寸時就可以在solvespace或onshape建立零件，我們是用onshape建立零件並且組立起來，當組立好的圖檔轉成.stl傳入v-rep進行模擬。

### [six links ball lifting mechanism 3.0.stl](https://github.com/s40523145/cd2018/blob/gh-pages/w10/six links 3.0.stl)

### [six links ball lifting mechanism 3.0.pyslvs](https://github.com/s40523145/cd2018/blob/gh-pages/w10/six links 3.0pyslvs.pyslvs)

### [six links ball lifting mechanism 3.0.slvs](https://github.com/s40523145/cd2018/blob/gh-pages/w10/six links 3.slvs)

### [six links ball lifting mechanism 3.0.ttt](https://github.com/s40523145/cd2018/blob/gh-pages/w10/six links ball lifting mechanism 3.0.ttt)

### [six links ball lifting mechanism 3.0 video](https://www.youtube.com/watch?v=M7oOTyCCsDs)

### [six links ball lifting mechanism 3.0 教學製作過程](https://www.youtube.com/watch?v=MBgTHzn_weU&t=5s) video

### [onshape](https://cad.onshape.com/documents/3b9e805055ae75fdbb2cb324/w/35725227a089223f72737219/e/8d20ebc1878667fdc8b3830e)

---

### 心得:

40523145

從上學期得到的經驗，在一開始設計時盡量不要過度的精細化零件，而是要從簡目的是要達到本身所想要的運動軌跡或是其它其它需求，減少運算的複雜，當達到理想的運動時就可以循序漸進的增加其它功能，否則只會增加設計成本的負擔，慢慢的在加入提球勺子和軌道。

---

## 40523146

這次用pyslvs中的六連桿範例做出可以模擬出循環至少兩次的鋼球運動系統，pyslvs可以一邊更改尺寸一邊做模擬，知道架構後我們輸出成2Dslvs，開solvespace知道各個連桿實際尺寸之後，再用OnShape繪製零件並組合，最後再用V-rep模擬，那這次比較困難的部分是V-rep的零件的樹狀組裝和Dummy的使用。

### [40523146.pyslvs](https://github.com/s40523145/cd2018/blob/gh-pages/40523146 W10/40523146.pyslvs)

### [40523146.slvs](https://github.com/s40523145/cd2018/blob/gh-pages/40523146 W10/40523146.slvs)

### [Assembly .stl](https://github.com/s40523145/cd2018/blob/gh-pages/40523146 W10/Assembly .stl)

### [SIX BAR FINAL.ttt](https://github.com/s40523145/cd2018/blob/gh-pages/40523146 W10/SIX BAR FINAL.ttt)

### [模擬影片\(1\)](https://www.youtube.com/watch?v=dj40uLCovRA)

### [模擬影片\(2\)](https://www.youtube.com/watch?v=P-3Feg7BkUA&feature=youtu.be)

---

### 心得:

這個兩段式提球機構和之前相比，省掉了很多想機構的時間，但是卻迎來了更多問題，零件變多了組裝變困難，需要考慮會不會撞到，雖然這些東西都克服了，還有球的軌道要設計，其中需要思考的是進軌道和出軌道的狀況，如果沒有一個檔球機構，很難確實撈到球，這部分是個人覺得比較困難的部分，所以只能靠概念去想像，實際要做出來就需要更多知識了。

