;Todo > imagesearch > check ghost house(완) > go to person (완) > pause resume 구현
;춫츷춫춫줓즟

/*
춫킃뿢씇훛퉂
춫츷춫춫줓즟
쭟끛쁯씇춫즟
1595456348
*/

#NoEnv
#Singleinstance Force ;1567 1764 ;1840 - 135개
#IfWinActive, ahk_class UnityWndClass ;바람 타이 변경

Kingdom_name = 죠르르 ;
gosthouse_name = 쭟끛쁯씇춫즟 ;
gosthouse_name2 = 춫츷춫춫줓즟 ;
gosthouse_name3 = 죠르르 ;

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

=::
SetTimer, PlaySound, -59000 ; 59초 후에 PlaySound 실행 (음수 사용)
Return
PlaySound:
    SoundPlay, pika.mp3
Return
return

[::
SetTimer, PlaySound2, -7000 ; 7초 후에 PlaySound 실행 (음수 사용)
Return
PlaySound2:
    SoundPlay, duck.mp3
Return
return


]:: ; 출두 본궁
teleport(Kingdom_name, false)
return

/*
[:: ; 흉 출두
teleport(gosthouse_name, false)
return

p:: ; 흉 출두2
teleport(gosthouse_name2, false)
return

o:: ; 흉 출두3
teleport(gosthouse_name3, false)
return
*/

/*
q:: ; 저중마헬
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
Random, var_80, 80,5555555555555555 85
sleep, %var_80%

Sendinput, {w} ;
Random, var_80, 80, 85
sleep, %var_80%
Sendinput, {w} ;
Random, var_80, 80, 85
sleep, %var_80%
return
*/

w:: ; 동동-공증
Sendinput, {u} ; item use
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {a} ; item use
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {3} ;
Random, var_100, 100, 105
sleep, %var_100%
return

/*
e:: ;디버프(저중마) 걸기
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
*/

;사자후
/::
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
Sendinput, ★☆흉가4지 중 입니다☆★ ;
Random, var_100, 100, 105
sleep, %var_100%
Sendinput, {enter}
Random, var_100, 100, 105
sleep, %var_100%
return

del:: ;생존힐
Sendinput, {4} ;
Random, var_40, 40, 45
sleep, %var_40%
Sendinput, {Home} ;
Random, var_40, 40, 45
sleep, %var_40%
Sendinput, {Enter} ;
Random, var_40, 40, 45
sleep, %var_40%
Sendinput, {4} ;
Random, var_40, 40, 45
sleep, %var_40%
Sendinput, {Enter} ;;
Random, var_40, 40, 45
sleep, %var_40%
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

/*
\:: ; 왕퀘용
Loop
{
    click 667 79 ; click king
    sleep, 65
    click 736 79 ; click king
    sleep, 67


    Random, var_60, 65, 67
    sleep, %var_60%
    Sendinput, {Space}
    Random, var_60, 65, 67
    sleep, %var_60%
    Sendinput, {Space}
    Random, var_60, 65, 67
    sleep, %var_60%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_60, 65, 67
    sleep, %var_60%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_60, 65, 67
    sleep, %var_60%
    ;Space
    Sendinput, {Space}
    Random, var_60, 65, 67
    sleep, %var_60%
    Sendinput, {Space}
    Random, var_60, 65, 67
    sleep, %var_60%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_60, 65, 67
    sleep, %var_60%
    Random, x_boxpoint, 890, 900
    Random, y_boxpoint, 380, 385
    click %x_boxpoint% %y_boxpoint% ; click king
    Random, var_60, 65, 67
    sleep, %var_60%
    ;Space
    Sendinput, {Space}
    Random, var_80, 85, 87
    sleep, %var_80%
    ;Space
    Sendinput, {Space}
    Random, var_80, 85, 87
    sleep, %var_80%
    ;Space
    Sendinput, {Space}
    Random, var_80, 85, 87
    sleep, %var_80%
    ;Space
    Sendinput, {Space}
    Random, var_80, 85, 87
    sleep, %var_80%
    ;s
    Sendinput, {s} ; item s
    Random, var_80, 85, 87
    sleep, %var_80%
    Sendinput, {s} ; item s
    Random, var_80, 85, 87
    sleep, %var_80%
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
    Sendinput, {PgDn}
    Random, var_100, 100, 105
    sleep, %var_100%

    Random, var_250, 250, 260
    sleep, %var_250%

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
        teleport(gosthouse_name2, true)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Mong.png
    if (ErrorLevel = 0)
    {
        SoundPlay, mario.wav
        teleport(gosthouse_name2, true)
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
*/
