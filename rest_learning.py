# https://docs.python-requests.org/en/latest/user/quickstart/
# python -m pip install requests
import requests
r = requests.get('https://api.github.com/events')


r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
r.text
r.encoding
r.content
r.encoding = 'ISO-8859-1'
r.text
r.json()
r.status_code
r.headers['Server']
r.headers['Content-Type']
r.cookies
r.history

# Timeouts
# You can tell Requests to stop waiting for a response after a given number of seconds with the timeout parameter.
# Nearly all production code should use this parameter in nearly all requests. Failure to do so can cause your program
# to hang indefinitely...

requests.get('https://github.com/', timeout=0.1)

import requests
# import bs4 #beautiful soup 4; pip install beautifulsoup 
# from bs4 import BeautifulSoup
import json

#https://www.neighborhoodscout.com/tx/austin/real-estate
neighborhood_google_urls = [
   "https://www.google.com/maps/place/Austin,+TX+78735/@30.2693295,-97.9444617,12z/data=!3m1!4b1!4m6!3m5!1s0x865b4a223455c13b:0xcd751fbcf0fb3c0a!8m2!3d30.2573497!4d-97.8612767!16s%2Fm%2F020ym0l?entry=ttu",
   "https://www.google.com/maps/place/South+Lamar,+Austin,+TX+78704/@30.2266895,-97.8509394,12.83z/data=!4m6!3m5!1s0x8644b4cdb7c2ac45:0x737138a1f89c150f!8m2!3d30.2372278!4d-97.7837533!16s%2Fm%2F0hgqszd?entry=ttu",
   "https://www.google.com/maps/place/Crestview,+Austin,+TX/@30.3465099,-97.7458137,14z/data=!3m1!4b1!4m6!3m5!1s0x8644cbb3586bc2a3:0xc8cf1eed0e664a44!8m2!3d30.348322!4d-97.727536!16s%2Fm%2F0hgmqty?entry=ttu",
   "https://www.google.com/maps/place/Central+East+Austin,+Austin,+TX/@30.2705551,-97.7651495,13z/data=!3m1!4b1!4m6!3m5!1s0x8644b5b96a8cf2af:0x759c9742828553e9!8m2!3d30.2716235!4d-97.7248647!16s%2Fm%2F0y7t5my?entry=ttu",
   "https://www.google.com/maps/place/Chestnut,+Austin,+TX/@30.2783286,-97.710809,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b5ea0671591d:0xe6300a756e554fe!8m2!3d30.2790657!4d-97.7131577!16s%2Fg%2F1tfhgt6y?entry=ttu",
   "https://www.google.com/maps/place/Zilker,+Austin,+TX/@30.2559887,-97.7796689,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b5213187c143:0x58356ef955bfbf77!8m2!3d30.2542688!4d-97.7669536!16zL20vMDZ2a2du?entry=ttu",
   "https://www.google.com/maps/place/Govalle,+Austin,+TX+78702/@30.2595231,-97.7446073,13z/data=!3m1!4b1!4m6!3m5!1s0x8644b5d14c083de1:0xa5efef5bcf1adb9a!8m2!3d30.2560413!4d-97.7016981!16s%2Fg%2F1tmxw_0f?entry=ttu",
   "https://www.google.com/maps/place/East+Oak+Hill,+Austin,+TX/@30.2468605,-97.8792218,13z/data=!3m1!4b1!4m6!3m5!1s0x865b4bad311aa5f3:0xc3f2725545b55e12!8m2!3d30.240054!4d-97.8303149!16s%2Fg%2F1vy7g_bv?entry=ttu",
   "https://www.google.com/maps/place/Rosewood,+Austin,+TX+78702/@30.2701575,-97.7192773,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b5c4ce8889b7:0x3d6a6574f0f86d10!8m2!3d30.2706266!4d-97.7104428!16s%2Fg%2F1tm0c5xs?entry=ttu",
   "https://www.google.com/maps/place/Pecan+Springs+Springdale,+Austin,+TX+78723/@30.2978059,-97.695482,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b6219200c94f:0x6f12ffd65e157e78!8m2!3d30.3000111!4d-97.6738023!16s%2Fg%2F1tcw3_x6?entry=ttu",
   "https://www.google.com/maps/place/Johnston+Terrace,+Austin,+TX/@30.2568776,-97.6939877,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b662f6246a85:0xabe68c8365abdaf1!8m2!3d30.2558365!4d-97.6849958!16s%2Fg%2F1tgns182?entry=ttu",
   "https://www.google.com/maps/place/Pleasant+Valley,+Austin,+TX+78741/@30.2325865,-97.7881622,13z/data=!3m1!4b1!4m6!3m5!1s0x8644b43da62a85f1:0x9b514f8c351693af!8m2!3d30.2347108!4d-97.7118003!16s%2Fg%2F1tq8jyt7?entry=ttu",
   "https://www.google.com/maps/place/Travis+Heights,+Austin,+TX/@30.2477129,-97.7650247,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b4fc2f422a37:0x2994f0398d3d2843!8m2!3d30.2442551!4d-97.7443863!16zL20vMDdqY202?entry=ttu",
   "https://www.google.com/maps/place/Barton+Hills,+Austin,+TX/@30.253185,-97.8635492,13z/data=!3m1!4b1!4m6!3m5!1s0x865b4ad4c8f3c345:0xcc1e2029a7db9ba8!8m2!3d30.2533686!4d-97.7835429!16s%2Fm%2F04cy8hf?entry=ttu",
   "https://www.google.com/maps/place/St.+Edward's+University/@30.23218,-97.7609103,17z/data=!3m1!4b1!4m6!3m5!1s0x8644b492ae61201b:0x1142c282cbe51336!8m2!3d30.23218!4d-97.75833!16zL20vMDF4MGpw?entry=ttu",
   "https://www.google.com/maps/place/Dawson,+Austin,+TX+78704/@30.23256,-97.7719038,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b4ea439ecbc1:0xec8417cc6bd78095!8m2!3d30.2329651!4d-97.7613825!16s%2Fm%2F0c3v_qw?entry=ttu",
   "https://www.google.com/maps/place/Valley+View+Rd,+Austin,+TX+78704/@30.2329389,-97.7863895,17z/data=!3m1!4b1!4m6!3m5!1s0x8644b4cb5f207c31:0x9767229499ed64bb!8m2!3d30.2329389!4d-97.7838092!16s%2Fg%2F1thz215r?entry=ttu",
   "https://www.google.com/maps/place/Mueller,+Austin,+TX/@30.2984516,-97.7396903,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b5fe5b3bfc47:0x78dc0a5de60a06d6!8m2!3d30.2986834!4d-97.700371!16s%2Fm%2F04jbkcv?entry=ttu",
   "https://www.google.com/maps/place/Westgate,+Austin,+TX/@30.2249033,-97.8367592,14z/data=!3m1!4b1!4m6!3m5!1s0x865b4b38df9123df:0x8e567d6a20e5cb5a!8m2!3d30.2230485!4d-97.7986926!16s%2Fm%2F0hhsvlp?entry=ttu",
   "https://www.google.com/maps/place/South+Manchaca,+Austin,+TX/@30.2194201,-97.8040954,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b4b318091d79:0xfb7efe4f2c879e06!8m2!3d30.2195294!4d-97.7839041!16s%2Fg%2F1tfrxwlv?entry=ttu",
   "https://www.google.com/maps/place/Ridgewood+Village,+Austin,+TX+78746/@30.2807228,-97.7957986,16z/data=!3m1!4b1!4m6!3m5!1s0x865b4ab16263fb4d:0xc7e647fda42f4f22!8m2!3d30.2824798!4d-97.7885374!16s%2Fg%2F1tsyq610?entry=ttu",
   "https://www.google.com/maps/place/Brentwood,+Austin,+TX/@30.3296166,-97.7717985,13z/data=!3m1!4b1!4m6!3m5!1s0x8644ca5b1eb3641f:0x652f75e8e6226623!8m2!3d30.330898!4d-97.7316065!16zL20vMGRfMWo4?entry=ttu",
   "https://www.google.com/maps/place/Wooten,+Austin,+TX/@30.3603659,-97.7423834,14z/data=!3m1!4b1!4m6!3m5!1s0x8644cbb8ff66163d:0x9cd49b74a813d492!8m2!3d30.3610582!4d-97.7232992!16s%2Fm%2F0g9_h7_?entry=ttu",
   "https://www.google.com/maps/place/N+Loop+Blvd,+Austin,+TX/@30.3223651,-97.7346477,17z/data=!3m1!4b1!4m6!3m5!1s0x8644ca6b7ba2bbd3:0xf262a74a34fc721a!8m2!3d30.3223605!4d-97.7320728!16s%2Fg%2F11bz_05w3f?entry=ttu",
   "https://www.google.com/maps/place/Hyde+Park,+Austin,+TX/@30.3073541,-97.7475774,14z/data=!3m1!4b1!4m6!3m5!1s0x8644ca710dd9e5b5:0x526d78512aa5b73c!8m2!3d30.3081697!4d-97.7274412!16zL20vMDdxMTdk?entry=ttu",
   "https://www.google.com/maps/place/Austin,+TX+78752/@30.2684235,-97.804423,12z/data=!3m1!4b1!4m6!3m5!1s0x8644b5b735cb7297:0xb589f9f8819370dd!8m2!3d30.3317278!4d-97.705158!16s%2Fm%2F020ymrm?entry=ttu",
   "https://www.google.com/maps/place/Austin,+TX+78723/@30.3042959,-97.7072675,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b5ce8e1d01b1:0xdf7283ae206ae376!8m2!3d30.3081307!4d-97.681943!16s%2Fm%2F020ym1f?entry=ttu",
   "https://www.google.com/maps/place/Austin,+TX+78759/@30.3990075,-97.7997674,13z/data=!3m1!4b1!4m6!3m5!1s0x8644cc84fa84ad09:0x5cbfa0aea73effe3!8m2!3d30.401356!4d-97.7525352!16s%2Fm%2F020ylz6?entry=ttu",
   "https://www.google.com/maps/place/Austin,+TX+78757/@30.3546734,-97.7547279,14z/data=!3m1!4b1!4m6!3m5!1s0x8644cbae658a6df1:0xcc784a8fcbc3294f!8m2!3d30.3568213!4d-97.730807!16s%2Fm%2F020ylq7?entry=ttu",
   "https://www.google.com/maps/place/East+Congress,+Austin,+TX/@30.2106708,-97.7737912,15z/data=!3m1!4b1!4m6!3m5!1s0x8644b4a1e268f32b:0x5fb98c8eaa4fe63b!8m2!3d30.2085609!4d-97.7661188!16s%2Fg%2F1tdbftly?entry=ttu"

   # best family neighborhoods, according to https://austinrelocationguide.com/top-family-friendly-neighborhoods-in-austin/
   # https://www.google.com/maps/place/Rollingwood,+TX+78746/@30.2707354,-97.8049782,13.92z/data=!4m6!3m5!1s0x865b4ab50ca9efb1:0x867547599c1726c7!8m2!3d30.2768742!4d-97.7911175!16zL20vMDEwOV8x?entry=ttu
   # https://www.google.com/maps/place/Old+West+Austin,+Austin,+TX/@30.2943615,-97.7535293,14z/data=!3m1!4b1!4m6!3m5!1s0x8644b562de0d4557:0x220d4c3e5079884!8m2!3d30.2954625!4d-97.7551352!16zL20vMGY3c3Mz?entry=ttu
   # https://www.google.com/maps/place/East+Oak+Hill,+Austin,+TX/@30.2469347,-97.8791365,13z/data=!3m1!4b1!4m6!3m5!1s0x865b4bad311aa5f3:0xc3f2725545b55e12!8m2!3d30.240054!4d-97.8303149!16s%2Fg%2F1vy7g_bv?entry=ttu
   # https://www.google.com/maps/place/Triangle+State,+Austin,+TX/@30.3019146,-97.7816207,13.1z/data=!4m6!3m5!1s0x8644ca64da7890ef:0x46be54b346d36c3e!8m2!3d30.3121843!4d-97.7352856!16s%2Fg%2F1tdd11zq?entry=ttu
   # https://www.google.com/maps/place/Barton+Hills,+Austin,+TX/@30.2532591,-97.863635,13z/data=!3m1!4b1!4m6!3m5!1s0x865b4ad4c8f3c345:0xcc1e2029a7db9ba8!8m2!3d30.2533686!4d-97.7835429!16s%2Fm%2F04cy8hf?entry=ttu

]
   
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

open_weather_map_base_url = "http://api.openweathermap.org/data/2.5/weather"
open_weather_map_api_key = "bd3987f785f348cc80b9dfb4a1fa4fa4"

for url in neighborhood_google_urls:

    lat_and_long = []
    lat_and_long += url.split('@')[1].split(',')[0:2]
        
    lat = lat_and_long[0]
    long = lat_and_long[1]
    
    parameters = {
        'lat': lat,
        'lon': long,  
        'appid': open_weather_map_api_key
    }

    # Make the API request and pass parameters as a query string
    response = requests.get(open_weather_map_base_url, params=parameters)
    response_json_as_dict = json.loads(response.text)

    #side tip: to view json in pretty print:  print(json.dumps(response_json_as_dict,indent=2))
    
    area_name_from_google_map = url.split("place/")[1].split(",")[0].replace("+"," ")
    area_name_from_weather_map = json.loads(response.text)["name"]
    area_weather = json.loads(response.text)["weather"][0]["description"]

    print("The weather in " + area_name_from_google_map + " (" + area_name_from_weather_map + ") is " + "\"" + area_weather+ "\"")


