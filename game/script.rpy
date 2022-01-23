﻿
#또 다른 함수를 정의합니다.
label inter:
    c "아니야, 나의 오랜 장난감 가게 경영 안목으로 볼때,\n
      음 아무래도 둘이 커플 같아 보이는데\n
      묘한 취미를 공통적으로 가진 커플같아 보이는 구려. 그러지 말고 내 이야기 좀 들어보게나."
    "우리들은 눈빛으로 살짝 이상한 것 같다는 사인을 보냈다.\n
    그렇지만, 이렇게 끈질기게 달라 붙는 영감님을 어떻게 돌려보내기 
     힘들기도 하고,"
    "앞서 말한대로 우리둘 모두 신기한 거에 어느정도 관심이 있기에,\n
    (또한 그것을 할배가 맞춘게 기분이 이상하긴 했지만)\n
     한 번 이야기 정도는 들어보는
     것도 괜찮을 거라고 생각했다."
    return
    
label outer:
    c "하하... 과연 내 직감이 맞았어. 그렇다면 내 이야기를 한 번 들어보게.\n
       이 가게에서 가장 신기하다고 장담할 수 있는 신비한 장난감에 대해서 말이야."
    "나와 남친은 살짝 이상하다고는 생각했지만, 이런 거에 흥미가 있긴 있기에 눈빛으로 '한번 들어보자고' 사인했다."
    return
  
#파일 경로명을 확장합니다.
init python:
    config.searchpath.extend(['game\music'])
    config.searchpath.extend(['game\images'])

#변수를 선언합니다.
init:
    $ input2_order = 'none'
    $ Anagram_order = 'OnREFNI'

#그림 파일들을 정의합니다.
init:
    image black = "black.png"
    image bg toystore all = "toystoreall.png"
    image bg toystore part = "toysotrepart.png"
    image bg toystore one = "toysotreone.png"
    image bg room = "Room.png"
    image bg noise = "noise.png"
    image bg muhan = "muhan.png"
    image bg bathroom = "bathroom.png"
    image bg livingroom = "livingroom.png"
    image bg fire = "rawrfire.png"
    image bg final = "fire.png"
    image bg beach = "beach.png"
    image Alice = "Alice.png"
    
#등장인물들을 정의합니다.
init python:
    a = Character('나')
    b = Character('남친', show_two_window = True)
    c = Character('할아버지', show_two_window = True)
    d = Character('우리', show_two_window = True)
    F = Character('프레딕', show_two_window = True)
    e1 = Character('다희', show_two_window = True)
    e2 = Character('???', show_two_window = True)

#첫번째 함수를 정의합니다.
label start:
    scene black
    "이 이야기는 작년 여름 나와 내 남친이 겪었던 기묘한 이야기이다."
    "둘 다 '장난감' 이라는 다소 키덜트한 요소를 좋아했기에\n
    우리는 거리를 거닐다가 엄청 낡은 장난감 가게안으로 들어갔다."
    show bg toystore all with dissolve 
    
    "그리고 왜인지,우리 둘다 미스터리라던가 오컬트 같은데 취미가 있었다."
    play music "18. Suteki Meppou.mp3"
    b "오, 저게 뭐지?"
    a "??? 뭐말이야 뭐"
    b " 저기 테이브가 덕지덕지 붙어있는, 아니다 자세히 보니 거의 칭칭 감겨있네.\n
        여튼 저기 박스 안보여?\n
        음 빨간색 페인트로 뭐라고 적혀는데... NE..RF... ???"
    b "음...잘 안보이는데 가까이서 볼까..."
    show bg toystore part with dissolve
    "왜 인지, 그것에 끌리긴 했지만 알 수없게 음산한 느낌이 들었다. 살짝 두리번 거리다가 우리들은 곧바로 그 박스앞에 다가갔다."
    a "그게 뭔 뜻이냐면..."
    show bg toystore one with dissolve
    c "오오오.... 얼마나 기다린 순간인가!"
    d "??? 네?"
    c "나는 지금까지 자네들 같은 사람들을 기다리고 있었다네.\n
        혹시 이 장난감에 흥미있는가?"
        
    menu : 
        "흥미가 있습니다":
            call inter from _call_inter
            jump S1
            
        "그런거 없어요...":
            call outer from _call_outer
            jump S1
    return

# 두번째, S1함수를 정의합니다.
# 내용이 길어 자르기 위하여 사용합니다.

label  S1:
    c "하하... 이 장난감은 말이지. 자네들이 이 장난감을 어떻게 조작하느냐에 따라... "
    "할아버지가 장난감 박스옆에 달려있는 조그마한 간이 상자에서 종이같은걸 꺼냈다."    
    c "바로 이 종이에 무언가 쓰이기 시작한다네."
    d "네?"
    c "나도 어처구니 없는 소리라는 것을 안다네.\n
     그런데 분명한 사실은 이 장난감을 가지고 놀았던, 사람들 대다수가 그 경험을 했어.\n
     비과학적이고, 이해할 수 없는 현상이라는건 알지만, 일단 현실에서 그렇게 했다는 사람이 많은 걸 어쩌겠는가."
    c "조작자가 어떻게 하느냐에 따라, 장난감의 미래와 이 종이에 쓰일 미래가 바뀌는 거지."
    "흐음... 생각보다 흥미롭고 신기했기에 우리는 잠자코 계속 그 장난감에 대해 들었다."
    c "그런 장난감이라네. 자, 어떤가 흥미가 생기면 한 번 해보는 게 어떤가?"
    b "얼마에 파나요?"
    c "오우 이런이런... 이건 파는게 아니라네.
        정확히 말하자면 빌리는 거겠지."
    d "빌린다구요?"
    stop music fadeout 0.8
    c "그래, 무료로 빌려준다네. 만약, 장난감이 마음에 들고 괜찮다고\n생각되면 돌려주지 않아도 된다네.
     그런데 무슨 이유에서인지, \n이때까지 이걸 빌려간 대다수의 사람들은 얼마 안 있어서\n다시 돌려주러 오더군.\n그때 반응 모두 한결 같았다네."
    c " '제발 맡아 달라고' 하더군."
    c "마치 저 장난감에 저주라도 걸린 마냥 공포에 질린 표정으로..."
    play music "Dead silence ost.mp3" fadein 0.5
    d "ㄷㄷㄷ"
    c "늙은이 얘기를 잘 들어줘서 고맙다네.\n
      가끔씩 자네들처럼 영기가 보이는 사람들한테는\n
     이런, 신기한 장난감도 있다는 걸 한 번 알려주고 싶었거든."
    "우리는 고민했다. 확실히 신기하고 특이하고 재밌을 것 같은 장난감이긴 한데,
     왠지 뒷이야기도 찝찝하고 음산하기 짝이 없었기 때문이다."
    b " 좋아요, 할아버지. 빌려주신 다면 정말 재밌게 가지고 놀게요. 그런데..."
    "갑자기 승낙해버려서 당황스러웠는데, 그 다음에 하는 남친 말에 나는 더 크게 놀랐다."
    b "할아버지 말대로, 사실 저한테는 집안 대대로 조상님으로부터 내려오는 영기 같은게 있어요.
     그러니 이런 저주받은 장난감 같은거 따위는 그렇게 신경 쓸만한게 아니거든요."
    b "저랑 내기 하시지 않을래요?"
    c "허어?"
    "할배의 넉살 좋은 표정이 갑자기 확 바뀌면서 눈이 번뜩하기 시작했다."
    c "내기라... 뭐 어떤거 말하는가?"
    b "뻔한 거 아니겠어요? 내가 이 장난감을 가지고 놀면서 얼마나 버티냐에 따라서 말입니다."
    c "하하. 오랜만에 재밌는 친구를 만난 것 같군."
    b "일단 이 부분은 솔직하게 말씀해주세요. 보통 사람들이 얼마만에 이 장난감을 돌려주러 오나요?"
    c "하.룻.밤 이라네.
       아 물론 장난감 사기만 해놓고 하지도 않는 썩을 놈들이 있어서\n
       최장 3일까지는 가던데, 여튼 그러하다네."
    b "아, 그렇다면 저는 일주일간 이 장난감을 가지고 놀고 있겠습니다."
    c "껄껄껄껄!!!"
    "갑자기 할배가 호탕하게 웃기 시작했다."
    c "그레, 패기는 좋군. 좋아, 만약에 자네가 내기에 이긴다면 뭘 갖고 싶은가?"
    "남친은 망설임도 없이 예전에 내가 갖고 싶었던 이 가게 장난감을 가리켰다."
    c "허... 그 속내를 알겠구만, 그래 그렇다면 보자... 내가 이기면..."
    "할배는 잠깐 고민하다가 말했다."
    c "숄을 주게 숄."
    d "숄요?"
    c "얼마전에 내 손녀가 태어났거든."
    c "그 아이가 좀 크면, 해줄 예쁜 숄이 갖고 싶어."
    b "네, 좋습니다."
    c "그럼 여기서 잠깐 기다리게."
    "할배가 그 장난감을 들고가서 포장을 한 뒤, 우리에게 건네주었다."
    c "자, 그럼 삼일 뒤에 보세. 껄껄껄!"
    b "으으... 부들부들 저 장난감은 이제 제껍니다."
    "묘한 신경전을 벌이고 그 골동품점 같은 장난감 가게의 출구로 발길을 돌리는 순간"
    
    "그 순간, 할아버지가 우리를 불러세웠다."
    c "아, 주의할 점을 한 가지 빼 먹어버렸군."
    c "일주일간 장난감을 꺼내지도, 하지도 않으려는, 얍삽한 생각하거들랑 빨리 접게나."
    c "그거, 가만히 들고 있는 것이 더 무서운 일을 불러올 수도 있다네."
    b "하하... 영감님도. 그런건 아무래도 좋으니까, 그런 비겁한 짓은 안 한다고 약속하지요."
    "할배가 쓸데없이 겁 준다고 생각하며, 문을 열고 나왔다."
    "물론 그때까지는 그렇다고 생각했다."
    stop music fadeout 0.8
    
    hide bg with dissolve
    play music "10. Hanekawa Tsubasa no Baai.mp3" fadein 0.8
    e2 "영감!! 다희 안보고 약이나 팔고 있지요!!!"
    c "아 뭐라노. 지금 다희한테 신화 들려주고 잘 있거든."
    e2 "절레절레"
    c "맞제 다희야."
    c "근데... 네 생각에는 이 내기 누가 이길것 같노?"
    e1 "꺄르륵 꺄르륵!"
    c "맞제! 할배다 할배! 니 좀 있으면, 예쁜 숄하나 선물해 주꾸마."
    e1 "후후후후"
    stop music fadeout 0.8
    
    jump S2
    return

#세번째, S3함수를 정의합니다.

label S2:
    "일주일 버티기. 할아버지 말이 뻥카인지 아닌지는 알 수 없으나,
    만약 이때까지의 자료치로 볼때, 이 장난감을 약속한 기한인 일주일 전날 밤에 까보는게
    가장 유리하다는 건 알 수 있다."
    "아니면 빨리 까보고, 정말 며칠간 아무일도 없었다는 걸 증명해도 좋다."
    "역시나 상식적으로 전자가 영악하긴 해도 절대적으로 유리한 건 사실인데,
    무슨 이유에서인지 남친이 끝까지 아무일도 없다는 걸 증명하고 싶어해서, 우린 결국 곧바로 장난감을
    열어서 해보기로 했다."
    "이런 상의를 마친 뒤, 우리는 먼저 가게를 나와서 시간을 봤다."
    "오후 2시..."
    "바로 남친집에 쳐들어가서 장난감을 만져보기로 했다."
    show bg room with dissolve
    "'일단 장난감이니까 그렇게 오래 걸리지 않겠지.' 하는 마음에 '켠김에 왕까지'를 하기로 마음먹었다."
    b "덜덜덜덜.... 타케시... 이 아니라,
       나는 못 무서워!"
    a "야... '안이랑 못'부정이 햇갈릴 정도면 얼마나 무서운거냐..."
    " 내가 한심하게 쳐다보며, 남친의 진동모드부터 해제시켜 준 다음 
       우리들은 두근 거리며 장난감을 꺼냈다."

    "상자밖에는 'NERF ION'이라고 빨간색 페인트로 덧칠 되어있었다.
     분명 무언가 쓰여져 있었는데, 상자색과 유사한 무언가를 발라 덧씌워 놓은 것 같다."
    "이 장난감에는 실제로는 뭐라고 적혀있었을까?"
    "아무 말없이 상자를 열어 장난감을 꺼내보았다."
    "안에 나온 것은 마치 가상 현실 게임기 같은 HMD 고글."
    "그리고 고글과 선으로 연결 된, 직육면체 모양의 게임 플랫폼같은게 있었다."
    " 그 플랫폼에는 알파벳이 박혀있는 버튼과 약간의 영문타자, 그리고 액정화면이 있었다."
    "그리고 왜인지는 몰라도 전기배합과 버튼조작 같은게 좀 복잡해서 키는데 시간이 좀 걸렸다."
    "그래도, 나름 전기/컴퓨터공학을 전공했던 남친이었기에 뭔가 만지작 거리더니..."
    "털컹!"
    play music "Brave+Heart+8-Bit.mp3" fadein 0.8
    b "오오오 이 친숙한 멜로디는!!"
    b "동심을 울리는 1990년대 초 명 브금, Brave Heart!"
    a "... 설명충 개극혐"
    "남친의 요란한 함성과 멜로디가 어우러지며, 장난감이 켜졌다."
    "그런데 할아버지 말대로 사용설명서에는 정말 아무것도 적혀져 있지 않았다.\n
    결국 끙끙거리며 조작법을 알아내야만 했다."
    "그 순간..."
    stop music fadeout 0.8
    play music "[NES - 8bit] Hacking_to_the_Gate.mp3" fadein 0.8
    e2 "짜잔~ NERF ION을 이용해주셔서 감사합니다."
    "장난감에서 녹음된 목소리가 나왔다."
    e2 "저는 여러분들에게 이 장난감을 가지고 어떻게 노는지 가르쳐줄\n'프레딕'이라는 사람이랍니다.\n전문 과학자, 혹은 매드사이언티스트로 유명하답니다. 음하하!"
    a "뭐지, 이 옛날 구닥다리 교육용 과학비디오에나 나올 멘트는..."
    F "네! 맞습니다. 이 장난감은 바로 교육용 장난감이에요!"
    F "여러분들은 이제 순서맞추기 놀이를 할 겁니다."
    d "순서 맞추기?"
    F "아 먼저 장난감 HMD 고글을 봐주세요.\n 그 부분이 바로 여러분들이 장난감에 일어나는 신기한 영상을 보는 곳입니다.\n
    그리고 고글 알 위에 버튼이 보이지요?"
    "각각 N, E, R, F, I, O, N 이라는 알파벳 대문자가 나열 되어있었다."
    F "그걸 누르면 각 알파벳 마다 영상들이 달라진답니다! \n 쉽게 말해 리모컨 채널을 바꾸는 거에요!"
    F "각 알파벳은 특정한 시간의 흐름대로 흘러가는 하나의 사건을 보여줍니다."
    F "여러분이 할 일은 그 사건을 올바른 순서로 한 다음..."
    F "고글밑에 타자기에 올바른 순서의 알파벳을 입력해주세요!"
    F "어때요, 굉장히 쉽죠?"
    "이거 정녕... 교육용 장난감이 맞을까... 굉장히 난이도 높아 보인다."
    F "그럼... 전 이만, 벚나무 근처로 가볼게요!"
    "벚나무?"
    stop music fadeout 0.6
    "정체불명의 말을 하더니.. 이윽고 잡음과 함께 멜로디가 뚝 끊겼다."
    "뭔가 어리둥절 하는 사이에 설명이 슥 지나가버렸다."
    a"정리하자면, 고글에 붙어 있는 특정 알파벳 버튼대로 누르면, 영상이 보여지고\n그 영상의 올바른 순서를 
    여기 밑에 있는 타자에 치면 된다는 게임."
    b "뭔, 가수 타블*씨가 했다던 맨사 테스트냐..."
    a "몰러... 일단 모든 알파벳을 봐야하니까 한 명이 붙잡고 하는게 좋겠는데..."
    play music "05 Bestest Detectives in the World.mp3" fadein 0.8
    "갑자기 먼 산을 보는 한심한 남자가 여기있다."
    a "어휴... 미스터리를 좋아하느니 하면서 겁은 많아요."
    a "그래, 내가 해볼게."
    b "흐...흠... 괜찮겠니?"
    a "응, 너보고 하라는 것보다는 훨씬 괜찮을 것 같다."
    "약간 자존심 상하면서도 겸연쩍은듯한 표정을 짓더니 뭔가 결연한 듯 말했다."
    b "아냐. 아무래도 이건 남자들의 싸움이다."
    a "뭔..."
    b "할배와 나만의 내기!\n 그러니 내가 직접 하겠어!"
    "뭔가 쓸데 없긴하지만, 뭔가 지켜주고 싶었다."
    a "그럼, 서로 알파벳 번갈아가면서 보고 뭐 봤는지 얘기해주고 그러자.\n
    혼자만 보면 다른 한 사람은 심심하잖아."
    b "굿굿"
    "그래서 각 알파벳에 나오는 영상을 돌아가면서 보고 서로 본걸 얘기해주는 형식으로 하기로 했다."
    hide bg with dissolve
    stop music fadeout 0.8
    "그리고 본격적으로"
    "지금까지도 나의 모든 신경을 곤두세우게 만드는 경험이"
    "시작 되었다."
    
    "띨깍"
    "※ 지금부터 여러분은 NERFIOn 장난감을 직접 만지게됩니다. \n
    선택지를 눌러 이야기를 모두 읽어보시고, \n
    모든 이야기를 읽으면 이야기의 올바른 순서를 입력할 수 있게 됩니다. \n"
    "생각이 나지 않으면 여러번 읽을 수도 있으니 걱정마세요."
    "N과 n은 대소문자를 구별하기 위한 것입니다. 이야기의 내용이 다를 뿐,
    큰 의미는 없다는 것에 유의하세요."
    jump Alice
    return
    
    #이후 스크립트 파일 Alice.rpy에 있는 Alice label로 이동합니다.
    #Alice.rpy와 이 함수의 이동은 유동적이며, 순차적이지는 않습니다.
    #아래 코드는 '나와 남친'이 나오는 이야기가 필요할 때 호출 됩니다.
    
label S3:
    "INFERnO?...."
    "나와 남친은 그 자리에서 얼어붙었다."
    "inferno..."
    "그것은 바로, '무한지옥'을 뜻했기 때문이다."
    
    "그런데 그 순간..."
    play music "SH2_Radio_02.mp3" fadein 0.9
    "잡음이 들리기 시작하더니"
    "장난감의 화면이 갑자기 노이즈로 바뀌었다."
    show bg noise with fade
    stop music fadeout 0.8
    "그리고 알 수 없는 브금이 노이즈에 섞여 천천히 들려왔다."
    play music "Ortsen-13-Fleur+Blanche-128.mp3" fadein 0.9
    "..."
    "화면이 곧 흐릿흐릿 하더니 무언가 보이기 시작했다."
    a "... 뭔가 기분이 이상해."
    a "화면에 노이즈가 섞이더니, 뭔가 이상한게 보이기 시작했어."
    b "? 뭔데 뭔데?"
    show bg muhan with fade
    a ".... 모래사장?"
    "뭔가 이상했다. 그러나 화면이 너무 파래서, 잘 보이지 않았기에 그게 정확히 무엇인지 보이지 않았다."
    stop music fadeout 0.7
    hide bg muhan with fade
    
    show I sea with fade
    play music "lost_memory.mp3"
    "....."
    "안녕, 내 이름은 앨리스."
    "내가 처음 눈을 떴을 때, 나는 고운 유리조각을 빻은 것 같이
    하얀 백사장 위에 아무렇게나 누워 있었어요."
    "나는 서서히 몸을 일으키자마자, 곧바로 생각했지요."
    "'나의 소중한 친구들 샌디, 브래드는 어디 있지?' 라고요."
    
    hide I sea with fade
    "이후 나오는 건 장난감의 첫번째 이야기 그대로였다."
    "계속해서 나오는 영상은 모두 우리가 봤던 영상 그대로..."
    "I.N.F.E.R.n.O 순서대로 진행되는 이야기를 앨리스는 무한 반복하고 있었다."
    ".... 나와 남친은 그 자리에서 아무 말도 할 수 없었다."
    "또 다른 세계가 펼쳐질 것을 기대하며 구덩이로 몸을 던진 앨리스는"
    "끝 없이 같은 세계의 모래사장에 떨어져, 기억을 잃은채로 같은 행위를 계속하고 있었다."
    "우리는 그 괴악함에, 그리고 이 끔찍한 무한 굴레를 만들어 놓은 제작자에 대한 공포와."
    "앨리스에 대한 안타까움으로 정말 아무것도, 아무말도 할 수 없었다."
    "..."
    "침묵을 깨고 남친이 무언가를 말했다."
    
    stop music fadeout 0.8
    show bg room with dissolve
    b "아, 설명서!"
    a "그래, 설명서에 뭔가 쓰여졌겠지?"
    "장난감 가게의 할아버지 말대로, 게임을 다 했으니, 설명서에 무언가 쓰여져 있을 것이다."
    "급하게 저 멀리 던져놓은 종이를 들어보았으나..."
    "거기에는 아무것도 적혀있지 않았다."
    b "음... 일단"
    "평소와 다르게 진지한 표정을 지으며 남친은"
    b "벌써 날도 늦고, 우리 둘다 너무 힘드니까, 오늘은 각자 집에서 쉬자."
    "라고 말하고 우리는 헤어졌다."
    
    hide bg room with dissolve
    show bg livingroom with dissolve
    "집에와서도 나는 그 장난감 생각에 편히 쉴 수 없었다."
    "소파에 앉아도 전혀 편하지 않았다."
    "그리고 할아버지 말한대로, 왜 설명서에 아무 글자도 떠오르지 않았는지 의아스러웠다."
    a "음... 신경쓰여. 일단 샤워나 해야지."
    hide bg livingroom with dissolve
    "그 순간 전화벨이 울렸지만, 무시하고 욕실로 들어갔다."
    show bg bathroom with dissolve
    "상의를 벗고 등 뒤를 살짝 거울에 비춰 본 순간..."
    play music "11. Kannen.mp3" fadein 0.8
    "나는 경악하고 말았다."
    "내 등에는 빨간 생채기와 피로 무언가 글자 같은게 떠올라 있었다."
    
    jump S4
    return

#네 번째 함수 S4에 대해 정의 합니다.
label S4:
    "나는 깜짝 놀라 등전체에 거울을 비추어 보았다."
    "확실히 글자였다."
    hide bg bathroom with dissolve
    "나는 먼저, 소스라치게 놀랐기에 곧바로 욕실을 나와 불을 키고, 거실에 갔다."
    "여전히 전화벨일 울리고 있었다."
    "안 좋은 예감이 들었지만, 빨리 받았다."
    b "...헉헉... 나 ... 등뒤에 빨갛게 이상한 글자들이 새겨져 있었어."
    a "응, 나도 방금 샤워하려다가 봤어."
    b "너도?"
    a "아무래도, 지금 바로 만나는게 좋을 것 같아."
    b "응... 아무래도 제작자가 여자 방 사진 찾기 귀찮으니까 니가 왔으면 좋겠어."
    a "..."
    "전화를 끊고 곧바로 남친집으로 다시 달려갔다."
    
    stop music fadeout 0.8
    show bg room with dissolve
    "우리는 여전히 흥분과 공포에 빠져 진정하지 못하고 있었다."
    "조금 진정이 되고, 우리는 먼저 등 뒤에 쓰여진 내용이 같은지 알아보았다."
    "결과는 일치."
    "고로 한명의 등에 내용이 무엇인지만 봐도 된다는 결론."
    b "아... 그렇다고, 내 등짝을 계속 보이기는 싫은데."
    play music "05 Bestest Detectives in the World.mp3" fadein 0.8
    a "찰싹! 등짝... 등짝을 보자."
    b "안돼요... 싫어요!!"
    "라며 바보같이 소리지르는 남친 벅지를 때리며,\n나는 침대 바닥 옆에 떨어져 있는
    설명서 종이를 들고 왔다."
    b "응???..."
    a "이거 종이 크기를 잘봐바."
    "등에 쓰여져 있는 글씨가 담겨진 폭과 정확히 일치했다.\n마치, 여기에 그 글씨를 탁본이라도 해라는 것 처럼."
    a "잠깐 등좀 빌리겠습니다."
    "나는 남친 상의를 훌떡 벗긴 뒤에,
    광개토대왕릉비를 탁본하는 학자 처럼 조심스럽게 등의 글자를 떴다."
    stop music fadeout 0.8
    hide bg room with dissolve
    
    "종이에 피로 쓰인 글자가 무섭게 다가왔다."
    "그리고 우리는 거기에 쓰인 글을 읽으므로써,"
    "이 모든 일들의 진상을 알게 되었다."
    "소설보다 무서운 현실에 소름이 돋지 않을 수 없었다."
    jump Big
    return

label NormalAS:
    play music "black wizard.mp3" fadein 0.8
    F "... 여러분... 결국 여러분도 이 무한 굴레에 빠지지 못했군요."
    F "괜찮습니다. 저는... 누군가가, 또다른 누군가가 이 일을 해결해 줄 거라고 믿기 때문입니다."
    F "왜냐하면, 저는 장난감이니깐요."
    stop music fadeout 0.8
    
    show bg fire with dissolve
    play music "seo jang.mp3"
    "그 말을 끝으로 갑자기... 종이가 타오르고, 장난감에 불이 붙기 시작했다."
    b "빨리, 집 밖으로 나가자!"
    "남친은 내 손을 와락 잡고, 곧바로 집 밖에 나갔다."
    "순식간에 집에 불이 붙기 시작하더니 활활 타버렸다."
    "그런데 신기한 것은 그 불이 다른 집으로 전혀 옮겨 붙지도 않았다."
    "곧바로 119에 전화하려고 했는데..."
    
    hide bg fire with dissolve
    stop music fadeout 0.8
    "놀랍게도 불이 꺼져버렸다."
    "집에 탄건 전혀 없었다."
    "모든 것이 깔끔했고, 그대로였다."
    "다만 한가지 다른 것은"
    "그 장난감과 상자, 그리고 설명서는 어디로 갔는지 감쪽같이 사라져 버렸다."
    "우리는 어안이 벙벙해져서,"
    "이 끔찍하면서도, 기묘한 일을"
    "그저 '괴이'라고 밖에 말할 수 없었다."
    "그리고 장난감과 설명서, 이 모든 것이 사라졌으니 굳이 장난감을 돌려주러 장난감가게에 갈 필요 없다고 결론 내렸다."
    "물론 찝찝한 건 사실이지만, 표면상 해결된 것도 사실이었기 때문이다."
    "우리는 그렇게 한 동안, 그 장난감 가게를 가지 않았는데..."
    "그로부터 1년 뒤인 오늘... 우리는 그 가게에 다시 들어가게 되었다."
    
    show bg toystore all with dissolve
    play music "18. Suteki Meppou.mp3"
    "1년 전과 별 다를 바 없는 풍경."
    "새로운 장난감들이 진열장에 몇개 생긴 것 말고는 크게 다를 바가 없었다."
    stop music fadeout 0.8
    "여전히... 모든게... 똑같앗..."
    "잠깐?"
    hide bg toystore all with dissolve

    
    show bg toystore one with dissolve
    c "오오오.... 얼마나 기다린 순간인가!"
    c "나는 지금까지 자네들 같은 사람들을 기다리고 있었다네.\n
        혹시 이 장난감에 흥미있는가?"
    "데자뷰..."
    "아니야, 이건 데자뷰 따위가 아니었다."
    
    play music "Miller_house.mp3" fadein 0.8
    "똑같은... 1년전과 똑같은 경험이었다."
    "그 자리에는 똑같이 NERFIOn이 있었으니까."
    c "응...? 자네들 왜 그러나... 표정이 잔뜩 굳어있어서는..."
    "우리는 뒤도 돌아보지 않고, 도망치듯 가게를 나왔다."
    hide bg toystore one with dissolve
    
    "그리고 생각했다."
    "1년전 할배가 말한대로 NERFIOn으로 미래가 바뀐 것은"
    "설명서나, 게임의 인물들 뿐만 아니라"
    "우리들이 아닐까라고..."
    "그리고 우리또한 이 세계를 조작하고 있는 누군가에 의해"
    "마치 게임을 하고 있는 플레이어 같은 누군가에 의해,"
    "끝없이 반복되는 세계에 빠진 건 아닐까?"
    "라고 생각했다."
    "끊임 없는 무한 지옥."
    "인페르노의 굴레속에서."
    "<NORMAL END. 또 다른 무한 굴레>"
    stop music fadeout 0.8
    return
    
label TrueAS:
    play music "SH2_Radio_02.mp3" fadein 0.8
    show bg noise with dissolve
    "갑자기 장난감에서 노이즈가 일더니... 모든 글자들이 사라져버렸다."
    hide bg noise with fade
    stop music fadeout 0.8
    "... 더욱 잔혹하고, 무서운 현실의 이야기를 접하고, 우리는 얼어붙어버렸다."
    "그리고, 오늘밤이 지나고 내일 아침이 되면, 바로 이 장난감을 가게에 돌려주러 가자고 약속했다."
    "..."
    "그 다음날"
    "누가 먼저라 할 세 없이 우리는 일찍 일어나 가게에 갔다."
    
    show bg toystore one with dissolve
    c "음... 예상대로, 문을 열자마자 왔군."
    d "할아버지... 저 장난감에 나오는 이야기 사실인가요?"
    c "그렇다네, 실제로 십년도 더 된 옛날, 미국의 어느 마을에 모자가 창고에서 둔기로 살해된 채 발견되었지."
    c "용의자가 '프레딕' 이라는 인물로 거의 확실시 되었는데..."
    c "'프레딕'이라는 심리학의 최고봉에 있는 인물이 그럴 일을 할리 없는데 무언가 이상했지."
    c "그리고 일주일뒤, 한국의 바로 이 마을에, 프레딕의 옛 고향이라고 불리는 이 곳의"
    c "뒷산 벚나무 숲에서 그는 목을 매고 자살했었다네."
    a "그때 이후로... 수십년간 이 장난감이 사람들 사이에 떠돌아 다닌 거에요?"
    c "그렇다네."
    c "개중에는 내가 이야기를 떠보기도 전에 소스라치게 놀라 도망치는 사람들도 있고."
    c "자네들 처럼 관심 있어하며, 이 장난감을 하겠다는 사람들도 있고... 그렇게 수없이 손길을 닿았지."
    c "내가 이렇게 까지 하는 이유는, 자네들도 알고 있겠지만,\n내가 프레딕으로 부터 받은 부탁때문이야."
    c "나는 앨리스와 프레딕, 그리고 이 일에 얽힌 모든 이들의\n영원한 고통으로부터 해방시켜줄 사람을 찾고 있었다네."
    c "그러나 대다수의 사람들이 지레 공포를 먹고는 장난감만 던지고 가버리더군."
    c "아니, 그게 가장 정상적인 반응이겠지."
    c "그래... 여기까지 알았다면, 자네들도 빨리 자리를 뜨게나..."
    play music "18 Overflowing Emotion.mp3" fadein 0.8
    b "아뇨, 저는, 아니 우리는 그러지 않을 겁니다."
    c "? 뭐라고?"
    b "내기 조건을 살짝 바꿀까 합니다. 영감님."
    c "허어?"
    b "제가 진건 인정하지만 말이죠.\n숄은, 저 장난감에 얽힌 저주를 풀고 드려도 되겠습니까?"
    c "자... 자네들..."
    "할아버지는 눈시울이 약간 붉어지더니, 고개를 살짝 돌리고 말을 이어나가셨다."
    c "좋아, 그렇다면, 내가 그 방법을 알려주겠네.\n 먼저, 이 사실 하나는 안타깝게 여기게나.\n오늘로 이 가게는 폐업일세."
    d "네?"
    c "나는 인생의 반을 오컬트와 영적의식에 대해 보낸 사람일세."
    c "저주를 푸는 의식을 하기 위해서는 안타깝게도, 가장 오랫동안 장난감의 영기가 머무른 이곳이 되어야 해."
    c "의식에 필요한 것은, 프레딕이 매었던 밧줄,\n그리고 가장 최근에 이 장난감을 만진 사람들,\n그리고 의식을 수행할 '의식자'라네."
    c "의식의 방법은 간단하네."
    c "프레딕이 맨 밧줄을 INFERnO의 HMD 고글로 본 다음, INFERnO의 순서를 거꾸로 치게나."
    c "그렇게 하면, 그 장난감을 나에게 바로 주게."
    c "나는 그것을 가게에 나두고 안에 있는 모든 사람들을 밖으로 불러내고..."
    "할아버지가 살짝 뜸을 들이더니 말했다."
    c "가게를 불태울 걸세."
    a "... 불태운다구요?"
    c "그래, 끝을 못 맺고, 끝없이 방랑하는 그들에게."
    c "마침내 '끝'이라는 영원한 안식을 주는거지."
    c "모든 영기서린 물건, 혹은 사람조차도, 불로서 모든 걸 깨끗이 없애고 자연으로 돌아갈 수 있다네."
    b "... 그런데 프레딕이 맨 밧줄 같은 건 어떻게 구하나요?"
    c "여기있지."
    "할배가 주머니에서 밧줄을 이루고 있었던 새끼줄을 꺼냈다."
    c "프레딕이 자살하고 나서, 곧바로 경찰에서 몰래 밧줄의 일부를 빼왔었다네."
    c "자, 그럼 시작해보세나."
    
    stop music fadeout 0.8
    "밧줄을 INFERnO의 고글로 봤다."
    jump Finalinput
    return
    
label Finalinput:
    "INFERnO 알파벳의 역순으로 장난감 자판에 쳐보자."
    $ input2_order = renpy.input('N과 n의 순서에 유의해서, INFERnO의 역 순서는 바로...')
    if input2_order == Anagram_order:
        "딸깍!"
        "무언가 장난감에서 소리가 들렸다."
        jump Final
        
    else:
        "... 아무 반응이 없다. 아무래도 틀리게 입력한 것 같다."
        jump Finalinput
        
    return
    
label Final:
    c "좋아, 이제 모든게 완료되었다네."
    c "일단, 안에 있는 사람은... 아직 아침이라 아무도 없고, 내 손녀 다희 뿐이군."
    c "저기 계산대 의자옆 아기간이침대에 누워있는 다희를 안고 조심히 이 건물을 빨리 나가게나."
    c "어서!!"
    "할아버지는 그렇게 말하고, 이상한 주문과 손동작을 하기 시작했다."
    show bg fire with fade
    "장난감은 벌겋게 달아오르더니, 곧이어 불길 같은게 생기기 시작했다."
    
    hide bg fire with fade
    "우리는 잠깐 넋놓고 있다가, 곧바로 다희를 안고, 장난감 가게를 빠져나왔다."
    "..."
    
    show bg final with dissolve
    
    play music "19 Rising Courage.mp3" fadein 0.8
    c "후후.. 프레딕, 오랜만이구만."
    c "그런데, 이제 끝을 맺을 시간이라네."
    c "나나... 자네나... 모든 걸..."
    c "아, 물론 나도 불타죽을 생각은 추후에도 없으니 길동무로 삼을 생각은 말게나."
    F "...... 원룡이.... 정말 고맙다네..."
    c "후후 별 말을... 이제 그만 편히 쉬게. 나의 첫번째 친구여."
    "할배는 초에 불을 붙이더니 천천히 특정 패턴으로 돌리고,"
    "가게와 장난감 주위에 불을 지르기 시작했다."
    "그렇게 하면 할 수록 더욱 장난감에서 나오는 불길이 거세졌다."
    "마지막으로, 장난감 가게 입구쪽에 불을 붙이고는\n할아버지는 뒤도 안돌아보고 빠르게 가게를 빠져나왔다."
    "화르르르륵...."
    "불길이 곧바로 거세지더니, 가게 전체를 집어삼켜 버렸다."
    b "119... 119..."
    "남친은 그제서야 119를 눌렀다."
    "그러자, 할배는 휴대폰을 누르는 남친 손을 붙잡더니."
    c "걱정말게. 다른 건물까지 번지지는 않으니."
    "라고 말했다... 근데 그래봤자, 가게 근처 지나가던 사람들이 모두 불구경 하며 이미 신고한지 오래..."
    "조금 있다가 소방차가 왔지만"
    
    hide bg final with fade
    a "어라?"
    "정말 할배 말대로, 장난감 가게만 전소되고 끝이 났다."
    "굳이 소방차가 불을 끄지 않았어도, 불길은 잠잠해진 상태."
    c "음... 며칠간 귀찮은 관공서 놈들이 괴롭히겠군."
    "할아버지의 그 말을 마지막으로, 화재에 대한 사건은 완료되었다."
    "멍하니 있는 남친에게 할아버지는"
    c "정말 고맙다네... 수십년간 마음속에 쌓아놓은 일을 마무리 할 수 있었어."
    "라며 웃으며 말했다."
    b "아닙니다. 찝찝하게 있으면, 내버려두는 스타일도 아닌지라."
    "남친은 그렇게 말하고, 왼손에 있던 쇼핑백을 할아버지에게 전달했다."
    "할아버지는 곧바로 쇼핑백을 뜯어서 내용물을 꺼냈다."
    c "음, 좋구만, 좋아... 끝 부분에 별이 달린 예쁜 하늘색 숄이구만."
    c "나중에 손녀가 보면 좋아하겠어."
    "그리고는 방금 모두 타버린 장난감 건물 안으로 들어가더니,"
    c "자, 아직 마무리는 이르다네. 앨리스를 구해줘야지."
    "INFERnO의 껍데기가 모두 부서지고, 안에 숨겨져있던, VRW의 모습이 드러났다."
    c "이제, 그냥 평범한 가상 현실 게임기에 불가하다네."
    c "그러니 가지고 있어도 괜찮을테니, 걱정이들랑 말게나."
    c "그러면 여기서 우린 작별을 하지."
    a "저기, 할아버지. 새로 장난감가게 안 여실거에요?"
    c "어... 장난감 가게 옆에 있는 빵집 보이지?"
    b "드래곤 베이커리요?"
    c "응, 그거 사실 내가 경영하는데야."
    c "이제 빵집이나 열심히 하면서 살아야지."
    c "빵 먹고 싶으면 놀러와서 빵이나 사가던지 하게나."
    c "그럼!"
    "할아버지는 그 말을 끝으로 건물 너머로 보이는 호수쪽으로 사라졌다."
    b "좋으신 분이야."
    a "응..."

    "그렇게 나와 남친이 여름에 겪었던 기묘한 경험은 끝이났다."
    "후에 있는 이야기이지만,"
    "설명충인 남친에 의하면... 그때 할아버지가 한 행동은 과학적으로도 맞는 행동이었다고."
    "우리 등에 있는 생채기나, 글자들이 보이고 우리만이 그 장난감에 글을 입력할 수 있었던 이유는"
    "VRW의 동공인식 기능 때문이라고 한다."
    "즉, 전에 봤던 장난감의 사람들의 동공을 인식하여 접속자체를 차단한 게임이라는 것."
    "오직 새로운 사람들만이 의식을 할 수 있었던 것은 그런 이유였겠지."
    "그리고 상처, 생채기, 글자 따위가 보인 것은 프레딕이 가상현실을 이용한 환시를 프로그래밍 했기 때문이라고 한다."
    "자신이 죽은 밧줄을 VRW로 보고 글자를 입력하게 한 것 조차도..."
    "뭐, 자세한 건 잘 모르겠고, 남친은 혼자 들떠서 말하고 있는데 그냥 무시하고 나는 창밖을 바라보았다."
    "너무 기묘해서, 그러나 그 만큼 왠지 모르게 무언가 마음 속에 배운 듯한 느낌이 드는 경험이었다."
    "끝없는 무한 지옥에 고통받는 사람들..."
    "어쩌면, 우리에게 아름답게 '끝' 을 맺을 수 있다는 것 자체가"
    "아름답고, 축복받은게 아닐까? 라고 생각하게 하는 경험이었다."
    "인간은 무한한 존재가 아닌"
    "한 없이 유한한 존재니까..."
    
    "<TrueEND. 유한세계>"
    stop music fadeout 0.8
    jump Afterstory
    return
    