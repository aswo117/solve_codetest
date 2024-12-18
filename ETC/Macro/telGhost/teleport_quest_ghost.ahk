;Todo > imagesearch > check ghost house(완) > go to person (완) > pause resume 구현

#NoEnv
#Singleinstance Force ;이률 크차

Kingdom_name = 죠르르 ;오도출
gosthouse_name2 = 바스출 ;
gosthouse_name = 죠르르죠르르 ;진흥도사

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

`:: ; 저중마헬
;Sendinput, {5} ;
;Random, var_80, 80, 85
;sleep, %var_80%
;Sendinput, {Enter} ;
;Random, var_80, 80, 85
;sleep, %var_80%
;Sendinput, {6} ;
;Random, var_80, 80, 85
;sleep, %var_80%
;Sendinput, {Enter} ;
;Random, var_80, 80, 85
;sleep, %var_80%
;Sendinput, {7} ;
;sleep, 80
;Sendinput, {Enter} ;
;sleep, 80
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

q:: ; 출두 본궁
teleport(Kingdom_name, false)
return

e:: ; 흉 출두
teleport(gosthouse_name, false)
return

r:: ; 흉 출두2
teleport(gosthouse_name2, false)
return

/*
q:: ;디버프(저중마) 걸기
Sendinput, {5} ;
sleep, 100
Sendinput, {Right} ;
sleep, 100
Sendinput, {Enter} ;
sleep, 100
Sendinput, {6} ;
sleep, 100
Sendinput, {Enter} ;
sleep, 100
Sendinput, {7} ;
sleep, 100
Sendinput, {Enter} ;
sleep, 100
return
*/

w:: ; 동동-공증
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
    Random, x_kingpoint, 730, 735
    Random, y_kingpoint, 70, 76
    click %x_kingpoint% %y_kingpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    Random, x_kingpoint, 730, 735
    Random, y_kingpoint, 70, 76
    click %x_kingpoint% %y_kingpoint% ; click king
    Random, var_100, 100, 105
    sleep, %var_100%
    ;Space
    Sendinput, {Space}
    Random, var_150, 150, 155
    sleep, %var_150%
    ;Space
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
}
