;Todo > imagesearch > check ghost house(완) > go to person (완) > pause resume 구현
;춫츷춫춫줓즟

/*

}::
SetTimer, PlaySound, -10000 ; 10초 후에 PlaySound 실행 (음수 사용)
Return
PlaySound:
    SoundPlay, mario.wav ;https://freesori.tistory.com/m/2
Return
return

}::
SetTimer, PlaySound, -60000 ; 60초 후에 PlaySound 실행 (음수 사용)
Return
PlaySound:
    SoundPlay, mario.wav ;https://freesori.tistory.com/m/2
Return
return

1.
일단 시냅스에서 프로필을 각각 만들어주셔야 합니다.
그 후에 상단탭에 프로필탭으로 가시면 각각의 프로필마다 게임을 지정해줄수가 있어요.
여기서 원하는 게임을 지정해주시면 해당 게임이 실행될때 그 프로필로 자동으로 전환됩니다.
로지텍에서는 설치된 게임을 자동으로 읽고 각각의 프로필이 자동으로 디폴트값으로 생성되어서
원하는대로 바꿔주기만 하면 됐지만. 시냅스는 일단 먼저 새로운 프로필을 만들어준다음에
그 프로필에 게임을 수동으로 지정해줘야합니다.

Synapse 실행: Razer Synapse 소프트웨어를 실행합니다.
마우스 선택: 소프트웨어에서 사용 중인 마우스 모델을 선택합니다.
"매크로" 또는 "키보드 기능" 탭 이동: "매크로" 또는 "키보드 기능" 탭을 찾습니다. (Synapse 버전에 따라 명칭이 조금씩 다를 수 있습니다.)
매크로 활성화/비활성화: 해당 탭에서 모든 매크로를 한 번에 활성화/비활성화하는 옵션을 찾습니다. 일반적으로 토글 스위치나 체크박스 형태로 제공됩니다. 만약 개별 매크로만 On/Off 할 수 있는 옵션만 있다면, 모든 매크로를 하나씩 비활성화해야 합니다.
프로필 사용: Synapse는 여러 프로필을 지원합니다. 매크로가 활성화된 프로필과 비활성화된 프로필을 만들어 프로필 전환을 통해 매크로를 On/Off 할 수 있습니다. Synapse에서 프로필을 전환하는 단축키를 지정할 수도 있습니다.

2. 바람 ahk_class 로 변경
3. 왕퀘 이미지 따고 설정
*/

#NoEnv
#Singleinstance Force ;1567 1764 ;1840 - 135개
#IfWinActive, ahk_class Notepad ;바람 타이틀로 변경

Kingdom_name = 죠르르 ;돈딩이
gosthouse_name = 춫츷춫춫줓즟 ;춫츷춫춫줓즟
gosthouse_name2 = 죠르르죠르르 ;단설화 미미걸

global clear_flag = 0

teleport(name, item)
{
    if (item = true)
    {
        Sendinput, {u} ; item use
        Random, var_100, 100, 105
        sleep, %var_100%
        Sendinput, {i} ; yello item
        Random, var_100, 100, 105
        sleep, %var_100%
    }
    else
    {
        Sendinput, {shift down} ; press shift
        Random, var_50, 50, 55
        sleep, %var_50%
        Sendinput, {z} ; use magic
        Random, var_50, 50, 55
        sleep, %var_50%
        Sendinput, {shift up} ; release shift
        Random, var_50, 50, 55
        sleep, %var_50%
        Sendinput, {z} ; release 비영
        Random, var_50, 50, 55
        sleep, %var_50%
        Random, doorway, 1, 4
        Sendinput {%doorway%}
        Random, var_50, 50, 55
        sleep, %var_50%
        Sendinput {Enter}
        Random, var_50, 50, 55
        sleep, %var_50%
    }
    Sendinput, {shift down} ; press shift
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {z} ; use magic
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {shift up} ; release shift
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {x} ; release chuldoo
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, %name% ;출두 name?
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {enter}
    Random, var_100, 100, 105
    sleep, %var_100%
    return
}

]:: ; 출두 본궁
teleport(Kingdom_name, false)
return

[:: ; 흉 출두
teleport(gosthouse_name, false)
return

p:: ; 흉 출두2
teleport(gosthouse_name2, false)
return

':: ; 저중마헬
Sendinput, {5} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {Enter} ;
Random, var_80, 80, 85
sleep, %var_80%

Sendinput, {6} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {Enter} ;
Random, var_80, 80, 85
sleep, %var_80%

Sendinput, {7} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {Enter} ;
Random, var_80, 80, 85
sleep, %var_80%

Sendinput, {1} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {Enter} ;
Random, var_80, 80, 85
sleep, %var_80%

Sendinput, {w} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {w} ;
Random, var_80, 80, 85
sleep, %var_80%
return

:*:;:: ; 동동-공증
Sendinput, {u} ; item use
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {u} ; item use
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {3} ;
Random, var_100, 100, 105
sleep, %var_100%
return

l:: ;디버프(저중마) 걸기
Sendinput, {5} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Right} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Enter} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {6} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Enter} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {7} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Enter} ;
Random, var_100, 100, 105
sleep, %var_100%
return

;사자후
:*:.::
Sendinput, {shift down} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {z} ; use magic
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {shift up} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {m} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, ★☆ 흉가 중 입니다☆★ ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {enter}
Random, var_100, 100, 105
sleep, %var_100%
return

del:: ;생존힐
Sendinput, {4} ;
Random, var_50, 50, 55
sleep, %var_50%
Sendinput, {Home} ;
Random, var_50, 50, 55
sleep, %var_50%
Sendinput, {Enter} ;
Random, var_50, 50, 55
sleep, %var_50%
Sendinput, {4} ;
Random, var_50, 50, 55
sleep, %var_50%
Sendinput, {Enter} ;;
Random, var_50, 50, 55
sleep, %var_50%
return

End:: ;보무
Sendinput, {9} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Home} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Enter} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {0} ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {Enter} ;
Random, var_100, 100, 105
sleep, %var_100%
return

F4:: ; 종료
ExitApp
return

F5:: ; suspend/resume(왕쿠용중 사용 금지)
Suspend
return

\:: ; 왕퀘용
Loop
{
    ;고구려
    ;415 105
    Random, x_kingpoint, 414, 415
    Random, y_kingpoint, 104, 105
    click %x_kingpoint% %y_kingpoint% ; click king
    ;부여
    ;Random, x_kingpoint, 530, 532
    ;Random, y_kingpoint, 120, 121
    ;click %x_kingpoint% %y_kingpoint% ; click king

    Random, var_100, 100, 105
    sleep, %var_100%

    ;고구려
    Random, x_kingpoint, 414, 415
    Random, y_kingpoint, 104, 105
    click %x_kingpoint% %y_kingpoint% ; click king
    ;부여
    ;Random, x_kingpoint, 530, 532
    ;Random, y_kingpoint, 120, 121
    ;click %x_kingpoint% %y_kingpoint% ; click king


    /*
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 King.png
    if (ErrorLevel = 0)
    {
        ;밑에 왕 메크로 다 넣기
        break
    }
    else{
        ;그냥 종료
        break
    }
    */

    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {Space}
    Random, var_150, 150, 155
    sleep, %var_150%
    Sendinput, {Space}
    Random, var_150, 150, 155
    sleep, %var_150%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_100, 100, 105
    sleep, %var_100%
;    Sendinput, {Down}
;    sleep, 100
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_100, 100, 105
    sleep, %var_100%
    ;s
    Sendinput, {s} ; item s
    Random, var_100, 100, 105
    sleep, %var_100%
    ;pd
    Sendinput, {PgDn}
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {PgDn}
    Random, var_100, 100, 105
    sleep, %var_100%
    Sendinput, {PgDn}
    Random, var_100, 100, 105
    sleep, %var_100%
    ;1.5s delay
    Random, var_300, 300, 320
    sleep, %var_300%

    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Bitch.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav ;소리 바꾸기
        teleport(gosthouse_name, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Fire.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Egg.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Bug.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Mong.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Mop.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name, true)
        break
    }
}
