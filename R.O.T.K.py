import discord
import datetime
import random
import openpyxl
import urllib.request
import os

client_id = "3a0u06zc5RRN3TJYRtdS"
client_secret = "yPj7PX8Fxh"

client = discord.Client()

location = 0 
turn = 0 

game_money = 100

banlist = ["!경고"]

@client.event
async def on_ready():
    print(client.user.id)
    print("Latte Bot Start")
    game = discord.Game('!명령어목록으로 다양한 명령어를 확인하세요.')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    global w
    global location
    global turn
    global game
    global game_money
    global i
    global msg
    global voice
    global player
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("!탐사"):
        await message.channel.send("탐사는 다른 세계 즉, 웜홀을 찾아 다른 우주로 가는것입니다.\n다른 우주 공간에서 유물 사이트, 데이터 사이트, 등\n사이트들을 찾아 그 안에 있는 물품으로 돈을 벌수 있습니다.\n주의: 웜홀 안에 들어가면 CONCORD 가 있지 않습니다. 이 뜻은 즉 본인이 만약 다른 유저들에게 공격 받아도 웜홀에서는 PVP가 성립되기 때문에 콩코드가 오지 않습니다. 꼭 디스캔을 보며 탐사를 하시길 바랍니다.")
    if message.content.startswith("!채광"):
        await message.channel.send("채광은 광물을 캐서 돈을 벌수 있습니다. 커나이트, 벨드스파, 등 여러가지 광물이 있으며\n또는 오메가만 캘수있는 아이스가 있습니다. 광물을 압축 시켜서 팔수도 있으며 함선, 무기, 등에 만드는데에 사용할수 있습니다.")
    if message.content.startswith("!PVE"):
        await message.channel.send("PVE는 Player vs Environment 라는 뜻이며 즉 게임에 있는 NPC들과 싸우는 것입니다.\n이러한 컨텐츠는 랫질, 이머징, 데드, 어비셜, 미션, 등이 있습니다.")
    if message.content.startswith("!PVP"):
        await message.channel.send("PVP는 Player vs Player 라는 뜻이며, 즉 다른 플레이어와 싸우는 것입니다.\nPVP는 전략, 대비, 등 바로바로 대처할 수 있는 능력이 있어야합니다.\n주의: 하이섹에서 다른 플레이어를 공격할시에 CONCORD 가 와서 공격합니다. (1.0 ~ 0.5)")
    if message.content.startswith("!산업"):
        await message.channel.send("산업은 블루플린트와 필요한 재료를 이용해서 함선, 무기, 리그, 등을 만듭니다. ")
    if message.content.startswith("!ping"):
        await message.channel.send('현재 핑 {0} ms'.format(client.latency))
    if message.content.startswith("!문의"):
        await message.channel.send("콥 디렉터나 리크루터에게 문의해주세요. 단, 운영진이 잠수일 경우 잠시만 기다려주세요.")
    if message.content.startswith("!나때는말이야"):
        await message.channel.send("워워.. 진정하세요!")
        await message.channel.send("계속 그러시면 딱딱으로 신고합니다!! 저리가세요!!!!!!")
    if message.content.startswith("!안녕"):
        await message.channel.send("어서오세요")
    if message.content.startswith("!출처"):
        await message.channel.send("출처는 펀즈위키 입니다.\n링크는 이쪽! : https://www.funzinnu.com/EVEwiki/FrontPage")
    if message.content.startswith("!사진"):
        await message.channel.send("Avatar.png")
    if message.content.startswith("!앙타"):
        await message.channel.send("앙타? 바부바부")
        await message.channel.send("앙타 멍췅이!")

    if message.content.startswith('!번역기한영'):
        print("'!번역기' 요청을 받았다.")
        m = message.content
        encText = urllib.parse.quote(m[7:])
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id","3a0u06zc5RRN3TJYRtdS")
        request.add_header("X-Naver-Client-Secret","yPj7PX8Fxh")
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            await message.channel.send(response_body.decode('utf-8')[152:-4])

    if message.content.startswith('!번역기영한'):
        print("'!번역기' 요청을 받았다.")
        m = message.content
        encText = urllib.parse.quote(m[7:])
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id","3a0u06zc5RRN3TJYRtdS")
        request.add_header("X-Naver-Client-Secret","yPj7PX8Fxh")
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            await message.channel.send(response_body.decode('utf-8')[152:-4])

    if message.content.startswith('!주사위'): #dice game
        print("주사위 게임을 시작한다.")
        dice = random.randrange(1,6) # 주사위 눈의 수
        turn +=1
        location += dice
        msg = await message.channel.send('주사위의 눈은 {0}이므로 {0}칸 앞으로 갑니다. {1}/25, {2}턴째.'.format(dice, location, turn))
    elif location < 0:
        location == 0
    elif location == 5:
        location -= 3
        msg = await message.channel.send('이런! 리프터를 만났습니다! 뒤로 3칸 갑니다. {}/20'.format(location))
    elif location == 12:
        location -= 4
        msg = await message.channel.send('이런! 닉스를 만났습니다! 뒤로 4칸 갑니다. {}/20'.format(location))
    elif location == 16:
        location -= 3
        msg = await message.channel.send('이런! 아포칼립스를 만났습니다! 뒤로 3칸 갑니다. {}/20'.format(location))
    elif location == 7:
        location += 2
        msg = await message.channel.send('와우! CONCORD입니다! 앞으로 2칸 갑니다. {}/20'.format(location))
    elif location == 15:
        location += 2
        msg = await message.channel.send('와우! 진급입니다! 앞으로 2칸 갑니다. {}/20'.format(location))
    elif location >= 25:
        print("주사위 게임을 끝냈다.")
        location = 0
        msg = await message.channel.send('무사히 목표 지점에 도착했습니다! 주사위는 ' + str(turn) + '번 던져졌습니다.')
        turn = 0

    if message.content.startswith('!이미지'):
        print("'!이미지' 요청을 받았다.")
        m = message.content
        encText = urllib.parse.quote(m[5:])
        url = "https://openapi.naver.com/v1/search/image?query=" + encText # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id","ALyDsw1MsaGr9PIYYHBg")
        request.add_header("X-Naver-Client-Secret","e_tciG5ktz")
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            response_body.decode('utf-8').replace(' 'and':'and',', '')
            b=response_body.decode('utf-8').split('"')
            await message.channel.send(b[19])
   
    if message.content.startswith(""):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [30, 200, 300, 400, 500, 680, 890, 1029, 1265, 1598, 1972, 2085, 2439, 2598, 2892, 3192, 3201, 3923, 4012, 4293, 4683, 4872, 5016, 5287, 5467, 5698, 5982, 6098, 6293, 6432, 7922]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 2
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("레벨이 올랐습니다.\n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break

            i += 1

    if message.content.startswith("!기초스킬"):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Enginering', value='CPU Management 5단\nPower Grid Management 5단\nWeapon Upgrades 5단\nCapacitor Management 4단', inline=False)
        embed.add_field(name='Armor', value='Hull upgrades 4단\nEM Armor Compensation 5단\nExplosive Armor Compensation 5단\nThermal Armor Compensation 5단\nKinetic Armor Compensation 5단', inline=False)
        embed.add_field(name='Shields', value='Shield Management 4단\nShield Upgrades 4단\nShield Operation 4단\nTactical Shield Manipulation 4단\nEM Shield Compensation 4단\nExplosive Shield Compensation 4단\nThermal Shield Compensation 4단\nKinetic Shield Compensation 4단', inline=False)
        embed.add_field(name='Drones', value='Drones 5단\nLight Drone Operation 5단\nDrone Navigation 4단\nDrone Sharpshooting 4단\nDrone Interfacing 4단\nDrone Durabillity 4단\nDrone Avionics 4단')
        await message.channel.send(embed=embed)

    if message.content.startswith("!버전"):
        embed = discord.Embed(color=0x110000)
        embed.add_field(name='버전, 제작자', value= '현재 버전: 1.01\n제작자: Suding Ko\n본 봇의 상업적 이용은 허용하지 않습니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Pointsystem"):
        embed = discord.Embed(color=0x000000ff)
        embed.add_field(name='Point system', value= 'Dps ships = 1.0 (딜 넣는 배)\nT2 Logi = 2.0 (텍2 로지, 텍1 x)\nCommand Ships = 1.5 (버프 배)\n\n\nInterceptors = 0.5 (인터셉터)\nDictors = 0.5 (this was requested by FCs) (딕터)\nAny other Subcap = 1.0 (나머지)\n\n\nFaxes = 2.0 (캐피탈로지)\nSupercarriers = 2.0 (슈캐 - 닉스가 무난)\nTitans = 3.0 (타이탄)\n\n\nMultibox bonus = +20% points (알트)\n\n\nExample: say you are bringing 2 munins and 1 dread alt to a strat op, you total points would be 3 x 1.2 = 3.6 points for that fleet\n예 : 2 뮤닌 + 1드레드 알트로 옵을 참여하면 3캐릭 x 20% = 3.6포인트 얻습니다.', inline=False)
        await message.channel.send(embed=embed)
    

    if message.content.startswith("!이비스"):
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='Ship Name: Ibis', value='[실드 저항력] EM: 8% 열: 27% 키네틱: 45% 폭발: 54%\n[장갑 저항력] EM: 50% 열: 45%  키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='2 High / 2 Medium / 2 Low\n2 Turret / 2 Launcher / Drone 5, 5', inline=False)
        embed.add_field(name='Bonus', value='Small Hybrid Turret 옵티멀 20% 보너스\n Scourge Light Missile, Scourge Rocket 대미지 20% 보너스\n ECM 강도 30% 보너스\n 모든 실드 저항 8%', inline=False)
        embed.add_field(name='Description', value='칼다리 ibis 급 코르벳은 작지만 튼튼하여 화물을 옮기거나 소형 채광선으로 쓸 수 있을 정도로 믿음직하기 때문에 초보 함장들이 곧잘 탑승하곤 한다.\n함선명은 따오기를 의미하는 영어 단어 Ibis이며, 헐 식별코드는 I-81S다.')
        await message.channel.send(embed=embed)

    if message.content.startswith("!Ibis"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Ibis', value='[실드 저항력] EM: 8% 열: 27% 키네틱: 45% 폭발: 54%\n[장갑 저항력] EM: 50% 열: 45%  키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='2 High / 2 Medium / 2 Low\n2 Turret / 2 Launcher / Drone 5, 5', inline=False)
        embed.add_field(name='Bonus', value='Small Hybrid Turret 옵티멀 20% 보너스\n Scourge Light Missile, Scourge Rocket 대미지 20% 보너스\n ECM 강도 30% 보너스\n 모든 실드 저항 8%', inline=False)
        embed.add_field(name='Description', value='칼다리 ibis 급 코르벳은 작지만 튼튼하여 화물을 옮기거나 소형 채광선으로 쓸 수 있을 정도로 믿음직하기 때문에 초보 함장들이 곧잘 탑승하곤 한다.\n함선명은 따오기를 의미하는 영어 단어 Ibis이며, 헐 식별코드는 I-81S다.')
        await message.channel.send(embed=embed)

    if message.content.startswith("!멀린"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Merlin', value='[실드 저항력] EM: 16% 열: 33% 키네틱: 50% 폭발 58%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='3 High / 4 Medium / 3 Low\n3 Turret', inline=False)
        embed.add_field(name='Bonus', value='스몰 하이브리드 터렛 대미지 5% 보너스\n 모든 실드 저항 4% 보너스', inline=False)
        embed.add_field(name='Description', value='Merlin급은 칼다리의 전투 프리깃급들 중에서도 최강이다.\n지난 수 년간 이 함급의 역할 변화를 짚어보자면, 방어적 특성은 여전히 칼다리의 함급 치고는 유별난 수준의 강함을 그대로 가지고 있지만, 공격적 특성은 기존에는 범용성과 무난함에 초점이 맞춰져 있었다면 이제는 정밀하고 확실한 타격 전술에 초점을 맞춰 진화했다. 본 함급의 주 운용 목적이라면 역시 상대의 선체를 벌집으로 만드는 것이리라', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Merlin"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Merlin', value='[실드 저항력] EM: 16% 열: 33% 키네틱: 50% 폭발 58%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='3 High / 4 Medium / 3 Low\n3 Turret', inline=False)
        embed.add_field(name='Bonus', value='스몰 하이브리드 터렛 대미지 5% 보너스\n 모든 실드 저항 4% 보너스', inline=False)
        embed.add_field(name='Description', value='Merlin급은 칼다리의 전투 프리깃급들 중에서도 최강이다.\n지난 수 년간 이 함급의 역할 변화를 짚어보자면, 방어적 특성은 여전히 칼다리의 함급 치고는 유별난 수준의 강함을 그대로 가지고 있지만, 공격적 특성은 기존에는 범용성과 무난함에 초점이 맞춰져 있었다면 이제는 정밀하고 확실한 타격 전술에 초점을 맞춰 진화했다. 본 함급의 주 운용 목적이라면 역시 상대의 선체를 벌집으로 만드는 것이리라', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!케스트렐"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Kestrel', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발 50%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 4 Medium / 2 Low 4 Launcher', inline=False )
        embed.add_field(name='Bonus', value='로켓 대미지 5% 보너스 라이트 미사일, 로켓 비행속도 10% 보너스', inline=False)
        embed.add_field(name='Description', value='Kestrel급은 동급 함선들 중에서도 제일 정교하고 수준 높은 센서 어레이를 탑재한 미사일 운용 함급이다. 이러한 설계에도 불구하고 여지껏 칼다리 해군 말고도 다른 부유한 무역 회사들(corporations)에게 화물 수송선의 용도로도 쓰여왔다는 사실은 꽤 흥미로운 점이라고 할 수 있겠다. 이렇듯 괜찮은 타격 능력을 갖춘 함급이라는 점은 안전이 보장되지 않은 위험한 구역들에서 단독으로도 무역 작업을 수행할 수 있게끔 해 준다. 본 함급은 미사일 런처를 총 4문까지 탑재 가능하게 설계되었으며, 이로 인해 다른 포탑 형식의 무장이나 채광 광선의 탑재는 제한되었다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Kestrel"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Kestrel', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발 50%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 4 Medium / 2 Low 4 Launcher', inline=False)
        embed.add_field(name='Bonus', value='로켓 대미지 5% 보너스 라이트 미사일, 로켓 비행속도 10% 보너스', inline=False)
        embed.add_field(name='Description', value='Kestrel급은 동급 함선들 중에서도 제일 정교하고 수준 높은 센서 어레이를 탑재한 미사일 운용 함급이다. 이러한 설계에도 불구하고 여지껏 칼다리 해군 말고도 다른 부유한 무역 회사들(corporations)에게 화물 수송선의 용도로도 쓰여왔다는 사실은 꽤 흥미로운 점이라고 할 수 있겠다. 이렇듯 괜찮은 타격 능력을 갖춘 함급이라는 점은 안전이 보장되지 않은 위험한 구역들에서 단독으로도 무역 작업을 수행할 수 있게끔 해 준다. 본 함급은 미사일 런처를 총 4문까지 탑재 가능하게 설계되었으며, 이로 인해 다른 포탑 형식의 무장이나 채광 광선의 탑재는 제한되었다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!콘도르"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Condor', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 4 Medium / 2 Low 3 Launcher', inline=False)
        embed.add_field(name='Bonus', value='10% 키네틱 라이트 미사일과 로켓 피해량 증가\n80% 추진기 재밍 시스템 활성화 비용 감소', inline=False)
        embed.add_field(name='Description', value='콘도르는 뛰어난 기동력을 보유한 함선입니다. 제한된 적재 공간으로 인해 무역 및 채굴에는 적합하지 않지만, 어썰트 함선의 특성을 지니고 있으며 유격전에서 탁월한 성능을 자랑합니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Condor"):
        embed = discord.Embed(color=0x0000ff)
        embed.add_field(name='Ship Name: Condor', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 50% 열: 45% 키네틱: 25% 폭발: 10%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 4 Medium / 2 Low 3 Launcher', inline=False)
        embed.add_field(name='Bonus', value='10% 키네틱 라이트 미사일과 로켓 피해량 증가\n80% 추진기 재밍 시스템 활성화 비용 감소', inline=False)
        embed.add_field(name='Description', value='콘도르는 뛰어난 기동력을 보유한 함선입니다. 제한된 적재 공간으로 인해 무역 및 채굴에는 적합하지 않지만, 어썰트 함선의 특성을 지니고 있으며 유격전에서 탁월한 성능을 자랑합니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!임페이러"):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Ship Name: Impairor', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 54% 열: 41% 키네틱: 31% 폭발: 29%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='2 High / 2 Medium / 2 Low 2 Turret 1 Launcher / Drone 5, 5 ', inline=False)
        embed.add_field(name='Bonus', value='Small Energy Turret 캡 소모량 20% 감소\nSmall Energy Turret 대미지 10% 보너스\nWeapon Disruptor 강도 15% 보너스\n모든 아머 저항 보너스 8%', inline=False)
        embed.add_field(name='Description', value='임페이러급 코르벳은 아마르 제국에서 수십 년 간 양산해온 함선입니다. 아마르 영토에서 가장 흔하게 볼 수 있는 기종이며 무역 또는 노예 수송에 주로 사용됩니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Impairor"):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Ship Name: Impairor', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 54% 열: 41% 키네틱: 31% 폭발: 29%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='2 High / 2 Medium / 2 Low 2 Turret 1 Launcher / Drone 5, 5 ', inline=False)
        embed.add_field(name='Bonus', value='Small Energy Turret 캡 소모량 20% 감소\nSmall Energy Turret 대미지 10% 보너스\nWeapon Disruptor 강도 15% 보너스\n모든 아머 저항 보너스 8%', inline=False)
        embed.add_field(name='Description', value='임페이러급 코르벳은 아마르 제국에서 수십 년 간 양산해온 함선입니다. 아마르 영토에서 가장 흔하게 볼 수 있는 기종이며 무역 또는 노예 수송에 주로 사용됩니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!퍼니셔"):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Ship name: Punisher', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 54% 열: 43% 키네틱: 34% 폭발: 30%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 2 Medium / 5 Low 4 Turret', inline=False)
        embed.add_field(name='Bonus', value='Small Energy Turret 캡 소모량 10% 감소\n모든 아머 저항 4% 보너스')
        embed.add_field(name='Description', value='현존하는 최강의 아마르 프리깃 중 하나입니다. 대규모 군사 작전 수행 시 퍼니셔는 강력한 무장을 바탕으로 대형 함선과의 연계 전술을 펼칩니다. 적 대열을 단독으로 뚫고 지나갈 수 있을 만큼 뛰어난 화력을 보유하고 있습니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!Punisher"):
        embed = discord.Embed(color=0x000000)
        embed.add_field(name='Ship name: Punisher', value='[실드 저항력] EM: 0% 열: 20% 키네틱: 40% 폭발: 50%\n[장갑 저항력] EM: 54% 열: 43% 키네틱: 34% 폭발: 30%\n[선체 저항력] EM: 33% 열: 33% 키네틱: 33% 폭발: 33%', inline=False)
        embed.add_field(name='Module Mounting Restriction', value='4 High / 2 Medium / 5 Low 4 Turret', inline=False)
        embed.add_field(name='Bonus', value='Small Energy Turret 캡 소모량 10% 감소\n모든 아머 저항 4% 보너스')
        embed.add_field(name='Description', value='현존하는 최강의 아마르 프리깃 중 하나입니다. 대규모 군사 작전 수행 시 퍼니셔는 강력한 무장을 바탕으로 대형 함선과의 연계 전술을 펼칩니다. 적 대열을 단독으로 뚫고 지나갈 수 있을 만큼 뛰어난 화력을 보유하고 있습니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!랫 정보"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="Drone Rat", value='스트레인, 크리플러, 디비터, 시즈, 알버스 모선, 알버스 여왕, 감염된 캐리어', inline=False)
        embed.add_field(name="저항력", value='[스트레인] EM: 72% 열: 79% 키네틱: 85% 폭발: 90%\n[크리플러] EM: 30% 열: 40% 키네틱: 50% 폭발: 60%\n[디비터] EM: 30% 열: 40% 키네틱: 50% 폭발: 60%\n[시즈] EM: 30% 열: 40% 키네틱: 50% 폭발: 60%\n[스트라이크] EM: 30% 열: 40% 키네틱: 50% 폭발: 60%\n[알버스 모선] EM: 48% 열: 58% 키네틱: 68% 폭발: 78%\n[알버스 여왕] EM: 49% 열: 59% 키네틱: 69% 폭발: 79%\n[감염된 캐리어] EM: ??? 열: ??? 키네틱: ??? 폭발: ???', inline=False)
        embed.add_field(name="특이점", value='스트레인 접두사가 들어간 프리깃, 크루저 급은 매우 실드가 단단하다, 하지만 장갑이 뚫리면 바로 녹는다.\n 크리플러, 디비터, 시즈, 스트라이크, 접두사가 들어간 프리깃은 매우 몸집이 약하다. 하지만 워프 디스럽터, 웹같은 전자전을 쓴다. 그러므로 약하게 봐선 안되는 녀석들이다.\n알버스 모선, 알버스 여왕은 매우 좋은 탱과 강한 딜을 가지고 있다. 하지만 트래킹 속도가 안 좋아 길라같은 크루저가 500m/s 이상 속도를 내면 못맞춘다.\n다음으로 감염된 캐리어는 보이면 바로 도망가야 한다. 이녀석은 웹을 걸고 엄청난 공격력을 자랑한다. 길라도 3~4방 맞으면 터지니 보이면 바로 도망가야할 1순위 적이다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!명령어목록"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name='[명령어 목록]', value='명령어 목록입니다!', inline=False)
        embed.add_field(name='!탐사', value='탐사에 대한 설명을 해줍니다.', inline=False)
        embed.add_field(name='!채광', value='채광에 대한 설명을 해줍니다.', inline=False)
        embed.add_field(name='!PVE', value='PVE에 대한 설명을 해줍니다.', inline=False)
        embed.add_field(name='!PVP', value='PVP에 대한 설명을 해줍니다.', inline=False)
        embed.add_field(name='!산업', value='산업에 대한 설명을 해줍니다.', inline=False)
        embed.add_field(name='!ping', value='현재 Latte is horse 봇의 핑을 알려줍니다.', inline=False)
        embed.add_field(name='!시간', value='현재 시간을 알려줍니다.', inline=False)
        embed.add_field(name='!뭐하지', value='할 것을 정해줍니다. (random)', inline=False)
        embed.add_field(name='!펀즈위키', value='펀즈위키 사이트를 알려줍니다.', inline=False)
        embed.add_field(name='!나때는말이야', value='Latte is horse 봇이 맞장구를 해줍니다', inline=False)
        embed.add_field(name='!뭐먹지', value='Latte is horse 봇이 뭐해먹을지 정해줍니다', inline=False)
        embed.add_field(name='!정보', value='자신의 디스코드 정보를 표시해줍니다.', inline=False)
        embed.add_field(name='!출처', value='함선 사진 출처는 펀즈위키 입니다.', inline=False)
        embed.add_field(name='!(함선이름)', value='함선이름에 원하시는 함선을 적으시면 능력치, 등을 알려드립니다.', inline=False)
        embed.add_field(name='!랫 정보', value='랫 정보를 표시합니다.', inline=False)
        embed.add_field(name='/사진', value='[(영어로)함선이름].png 예: /사진 Avatar.png', inline=False)
        embed.add_field(name='!Pointsystem', value='Horde Pointsystem에 대한 설명입니다.', inline=False)
        embed.add_field(name='!군스', value='군스의 대한 ~~입니다. ㅎ', inline=False)
        embed.add_field(name='!남의쟁기 잡는법', value='봇이 남의 쟁기 잡는법을 알려줍니다.', inline=False)
        embed.add_field(name='!버전', value='현재 버전과, 제작자를 표기합니다.', inline=False)
        embed.add_field(name='!사진', value='이 명령어는 현재 볼수있는 사진을 표기합니다.', inline=False)
        embed.add_field(name='!기초스킬', value='초반에 찍어야되는 스킬을 표로 보여줍니다.', inline=False)
        embed.add_field(name='!주사위', value='턴제형 주사위 게임을 시작합니다.', inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("!뭐하지"):
        game = "이머징 어비셜 데드_스페이스 탐사 산업 채광 퍽치기 뒤치기 랫질 앞치기 PVP"
        gamechoice = game.split(" ")
        gamenumber = random.randint(1, len(gamechoice))
        gameresult = gamechoice[gamenumber-1]
        await message.channel.send(gameresult + " 어떠세요?")

    if message.content.startswith("!대화"):
        chat = "이브를접으시는게..? 할말이없어요.. 안녕하세요. 좋은하루!되세요. 네에에..? 호에에에에에에!!! 저리가요! 안놀아줄거임ㅡㅡ 왜여어; ;;; 대화안할거에요; 왜자꾸말걸어여;;"
        chatchoice = chat.split(" ")
        chatnumber = random.randint(1, len(chatchoice))
        chatresult = chatchoice[chatnumber-1]
        await message.channel.send(chatresult)

    if message.content.startswith("!군스"):
        goons = "어?_다른벌한테**고백**했는데_차인_그_벌아닌가요? 어..말을아끼겠습니다. ㅎ 와!_군스_아시는구나! ㅎㅎㅎㅋㅋ 와!벌! 엌ㅋㅋㅋㅋㅋㅋㅋ 우욱.. 말벌! 소난다... 넣을게.. 핡짝핡짝 이후_~~메차쿠차~~_범해버렸다.."
        goonschoice = goons.split(" ")
        goonsnumber = random.randint(1, len(goonschoice))
        goonsresult = goonschoice[goonsnumber-1]
        await message.channel.send(goonsresult + " ㅋ")

    if message.content.startswith("!남의쟁기 잡는법"):
        janggi = "몰라요.. 음..미사일_갈기면되는ㄱ.. 전_간디_이기때문에그런거몰라오 알아서잡아요! 왜그런걸_저한테_물어보시는거죠..?"
        janggichoice = janggi.split(" ")
        jangginumber = random.randint(1, len(janggichoice))
        janggiresult = janggichoice[jangginumber-1]
        await message.channel.send(janggiresult)

    if message.content.startswith("!뭐먹지"):
        Food = "삽겹살 차돌박이 갈비 고등어 카레 육개장 국밥 김치찌개 된장찌개 계란말이 냉면 김치볶음밥 짜장밥 짜장면 짬뽕 계란볶음밥 회 고추장 된장 밥 라면 햄버거 치킨 닭꼬치 김치"
        Foodchoice = Food.split(" ")
        Foodnumber = random.randint(1, len(Foodchoice))
        Foodresult = Foodchoice[Foodnumber-1]
        await message.channel.send(Foodresult + " 어떠세요?")

    if message.content.startswith("!야"):
        hey = "?? 네? 그만불러요ㅡㅡ ;; 그만해요 봇도_인내심이_있습니다. 부르셨나요? 저도_사생활이_있습니다.. 제발그만.. 저리가아아!!!!! 그만좀하라고요! 아몰라.. 제발가!!!!!!!!!!!!!!!!!!!!!! 아니**하지**말라니까요! 아..좀.. 예? 뭐요 ........ 아니적당히해요.. 선넘지마세요ㅡㅡ 안놀거야! 우리사장님한테이를꺼야!!!!!!!! 저리가라구요!!! 빼ㅇ애애애애애애애액ㄱㄱ!!!! 그만해여... (ㅌㅌ) 그만말걸어요... 아..;;;;; ㅠㅠ.. ㅇㅅㅇ..;"
        heychoice = hey.split(" ")
        heynumber = random.randint(1, len(heychoice))
        heyresult = heychoice[heynumber-1]
        await message.channel.send(heyresult)

    if message.content.startswith("!퍽치기"):
        puck = "무엇? ???????? 뭔데요? 에반데;; 퍽치기당하실? 빼애애애애애액 사탄도_울고갈_휴먼;; 미쵸미쵸.. 빠만데.."
        puckchoice = puck.split(" ")
        pucknumber = random.randint(1, len(puckchoice))
        puckresult = puckchoice[pucknumber-1]
        await message.channel.send(puckresult)

    if message.content.startswith("!이번주로또번호"):
        roto = "그런거몰라요 ?????? 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 20 75 23 19 33 85 4 52 43 98 32 18 29 35 74 39 28 99 92 98 82 85 "
        rotochoice = roto.split(" ")
        rotonumber = random.randint(1, len(rotochoice))
        rotoresult = rotochoice[rotonumber-1]
        await message.channel.send(rotoresult)

    if message.content.startswith("!출근"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 라떼 봇 출근하였습니다!")

    if message.content.startswith("!퇴근"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 라떼 봇 퇴근하였습니다!")

    if message.content.startswith("!골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)

    if message.content.startswith("!펀즈위키"):
        await message.channel.send("https://www.funzinnu.com/EVEwiki/FrontPage")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[2]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[3]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[4]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[5]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[6]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[7]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[8]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[9]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[10]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[11]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[12]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[13]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[14]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[15]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[16]
        await message.channel.send(file=discord.File(pic))

client.run("NjYxMTkyMjMxNTIwMDQzMDM3.XrAUMA.Ki4lNLDfjdUmb3UyNvL1OBJYpC0")
