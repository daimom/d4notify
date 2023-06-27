
# D4Notify

截取暗黑編年史的世界王通知時間，透過Line Notify發送到Line上面。

## 注意

 需將d4spider.py 的 第 36行， 將token 更改為自己的token


## Usage

此乃python 的scrapy架構。
執行方式可用command或是其他scrapy的排程軟體。

```bash
scrapy crawl d4spider 
```

在d4spider.py上，增加呼叫倒數計時器的api方法，
將名稱與boos出現時間傳到[D4Countdowntimer](https://github.com/daimom/d4countdowntimer)裏面，
即將開始前30分，會開始發通知。