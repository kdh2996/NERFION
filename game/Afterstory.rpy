
#인물을 정의합니다.
init python:
    S = Character('샌디', show_two_window = True)
    BR = Character('브레드', show_two_window = True)

#애프터 스토리 함수를 정의합니다.
label Afterstory:
    "<Afterstory>"
    show I sea with dissolve
    play music "08. Shinsou no Reijou.mp3" fadein 0.8
    "안녕, 내 이름은 앨리스."
    "내가 눈을 떴을 때, 나는 고운 유리조각을 빻은 것 같이
    하얀 백사장 위에 아무렇게나 누워 있었어요."
    
    stop music fadeout 0.8
    hide I sea with dissolve
    
    show bg beach with dissolve
    play music "Gao - sosil.mp3" fadein 0.8
    S "야... 쟤 또 저기서 자고 있냐."
    BR "그러게..."
    S "앨리스!! 점시에 바베큐하게 거기서 잠이나 자지말고 와서 일 좀 도와!"
    A "아함... 잠 와. 걍 좀 놀다가 하면 안돼?"
    BR " 안돼 "
    S "음... 해수욕장에 온지 얼마 안 됬으니까, 좀 놀다가 하는것도 괜찮을 것 같은데."
    BR "정신차려요 샌디님. 앨리스의 농땡이에 같이 놀아나면 안된다고."
    S "에이 몰라. 앨리스!! 같이 물에 들어가서 좀 놀자."
    A "해헤... 역시 샌디는 내 편이야. 좋아해!"
    BR "저 시붐년들..."
    A "조금만 놀다 도와줄게, 브래드."
    BR "부들부들... 또 나는 고기나 굽고 있겠지 (눈물을 닦는다.)"
    hide bg beach with dissolve
    
    "후후... 이제 일기는 밤에 쓰도록 할게요."
    "안녕."
    show Alice with fade
    "<앨리스 이야기 끝.>"
    "FIN"
    stop music fadeout 0.8
    return
    