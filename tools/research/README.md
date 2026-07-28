# 公开资料采样工具

这些工具只用于把公开测试视频转为可追溯的研究证据，不属于游戏自动化实现。

## Bilibili 临时采样

```powershell
powershell -File tools/research/fetch_bilibili_sample.ps1 -Bvid BV1YqTK6oEkk
```

视频和音频默认写入系统临时目录，不提交仓库。

公开检索：

```powershell
powershell -File tools/research/search_bilibili.ps1 -Query "RO3 挂机" -Pages 3
```

## YouTube 长直播元数据

常规下载器遇到访客验证时，只读取无需登录的公开 watch 页面，不读取浏览器
Cookie。播放器响应和 storyboard 规格仅存入系统临时目录：

```powershell
powershell -File tools/research/fetch_youtube_watch.ps1 `
  -VideoId ac4CcVmAI70 `
  -SavePlayerResponse `
  -FetchPublicCaptions
```

该工具只建立候选时间轴。缩略图、字幕或播放器元数据都不能替代目标片段的
人工画面复核，也不能直接成为 Manifest 中的流程证据。

`-FetchPublicCaptions` 使用 MacParakeet 页面公开说明的无账号字幕接口，仅在
原视频本身已有字幕轨时有效；返回为空时，不应推断视频没有相关内容。

## 按时间点抽帧

```powershell
uv run --python 3.12 --with av --with pillow python tools/research/extract_frames.py `
  --input "$env:TEMP/maaRO3-research/BV1YqTK6oEkk/video.m4s" `
  --output "research/work/BV1YqTK6oEkk" `
  --times 333 388 448 456 466
```

抽帧后人工检查，只有确实支持设计事实的最少帧才可复制到 `research/evidence/`，并补写 manifest。

## Twitch 公开 VOD 目标区间

仅对明确给出的时间段下载公开 HLS 分片，不下载整场 VOD，也不使用账号、Cookie
或验证码绕过：

```powershell
uv run --python 3.12 --with av --with yt-dlp python `
  tools/research/extract_twitch_hls_ranges.py `
  --url "https://www.twitch.tv/videos/2804737558" `
  --format 720p60 `
  --output "$env:TEMP/maaRO3-research/TW-2804737558/review" `
  --ranges 03:31:30-03:32:00 06:20:00-06:21:00 `
  --interval 0.5
```

生成的 `review.json` 保存 VOD 元数据、格式、分片范围及每张帧的原始时间点。
临时故事板和目标区间只能用于人工排查；未命中目标事实时不得复制进正式证据库。
故事板的 slide／tile 文件名只表示候选窗口起点，不是目标事件的精确时间戳；必须扫描完整窗口，再以 HLS 帧的真实 VOD 时间回抽高清。`2540550896` 的连接弹窗就是从约 756 秒故事板候选块校正到约 817 秒高清事件。

公开聊天只能用作短事件时间定位，同样不能代替画面：

```powershell
uv run --python 3.12 python tools/research/search_twitch_chat.py `
  --vod 2804807809 2804892798 `
  --terms 背包 滿包 疲勞 復活 斷線 重連 `
  --output "$env:TEMP/maaRO3-research/twitch-chat-gap-search.json"
```

工具只读取无需账号、Cookie 或 OAuth 的公开视频聊天，并记录命中词与录像秒数；
所有命中仍须回抽连续画面，聊天者的说法不能直接进入图标证据库。

## 图标与 UI 状态裁图

裁图定义位于 `research/evidence/icons/catalog.json`。生成器会先核对父帧哈希，
按声明坐标裁切，并机械更新尺寸和裁图 SHA-256：

```powershell
py -3 tools/research/crop_icon_evidence.py --update-derived
py -3 tools/validate_research.py
```

总校验器会从父帧逐像素重建每张裁图。不得用生成图、其他 RO 产品或同一张状态
图替代缺少的普通／选中／锁定／可领／已领变体。

## Bilibili 站内候选检索

```powershell
powershell -File tools/research/search_bilibili.ps1 `
  -Query "RO3 仙境传说3 启燃测试" `
  -Pages 2
```

检索结果默认只是 `queued` 候选。标题、播放量和搜索摘要不能代替完整观看。

## 联络表

对临时抽取的一组 PNG 生成方便人工筛选的联络表：

```powershell
uv run --python 3.12 --with pillow python tools/research/make_contact_sheet.py `
  --input research/work/BV1YqTK6oEkk `
  --output research/work/BV1YqTK6oEkk/contact-sheet.jpg
```

联络表只用于快速定位，不能代替查看原帧。

## 本地语音转写

`transcribe_audio.py` 只使用已下载到本机的 faster-whisper 模型，不自动联网取模型：

```powershell
uv run --python 3.12 --with faster-whisper python tools/research/transcribe_audio.py `
  --input "$env:TEMP/maaRO3-research/BV1oKNi6kEzy/audio.m4s" `
  --output "research/work/BV1oKNi6kEzy/transcript.json" `
  --model "D:/models/faster-whisper-small"
```

转写只用于建立时间轴，错字和解说观点必须回到视频画面或第二来源复核。

## 制作接触表

```powershell
uv run --python 3.12 --with pillow python tools/research/make_contact_sheet.py `
  --input "research/work/BV1YqTK6oEkk" `
  --output "research/work/BV1YqTK6oEkk-contact.jpg"
```
