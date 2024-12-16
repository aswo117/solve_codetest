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
        sleep, 101
        Sendinput, {i} ; yello item
        sleep, 102
    }
    else
    {
        Sendinput, {shift down} ; press shift
        sleep, 61
        Sendinput, {z} ; use magic
        sleep, 62
        Sendinput, {shift up} ; release shift
        sleep, 60
        Sendinput, {z} ; release 비영
        sleep, 59
        Sendinput {1}
        sleep, 58
        Sendinput {Enter}
        sleep, 53
    }
    Sendinput, {shift down} ; press shift
    sleep, 101
    Sendinput, {z} ; use magic
    sleep, 99
    Sendinput, {shift up} ; release shift
    sleep, 100
    Sendinput, {x} ; release chuldoo
    sleep, 103
    Sendinput, %name% ;출두 name?
    sleep, 101
    Sendinput, {enter}
    sleep, 100
    return
}

`:: ; 저중마헬
Sendinput, {5} ;
sleep, 80
Sendinput, {Enter} ;
sleep, 80
Sendinput, {6} ;
sleep, 80
Sendinput, {Enter} ;
sleep, 80
;Sendinput, {7} ;
;sleep, 80
;Sendinput, {Enter} ;
;sleep, 80
Sendinput, {1} ;
sleep, 80
Sendinput, {Enter} ;
sleep, 80
Sendinput, {w} ;
sleep, 80
Sendinput, {w} ;
sleep, 80
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
sleep, 100
Sendinput, {u} ; item use
sleep, 100
Sendinput, {3} ;
sleep, 100
return

del:: ;생존힐
Sendinput, {4} ;
sleep, 50
Sendinput, {Home} ;
sleep, 50
Sendinput, {Enter} ;
sleep, 50
Sendinput, {4} ;
sleep, 50
Sendinput, {Enter} ;;
return

End:: ;보무
Sendinput, {9} ;
sleep, 100
Sendinput, {Home} ;
sleep, 100
Sendinput, {Enter} ;
sleep, 100
Sendinput, {0} ;
sleep, 100
Sendinput, {Enter} ;
sleep, 100
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
    click 736 76 ; click king
    sleep, 121
    click 736 76 ; click king
    sleep, 120
    ;Space
    Sendinput, {Space}
    sleep, 171 ; delay 0.1s
    ;Space
    Sendinput, {Space}
    sleep, 172
    ;??
/*
    ;본궁 출두 후 처리시 케릭 아래로 이동 방지
    if (global clear_flag == 1)
    {
        ;MsgBox, %clear_flag%
        global clear_flag = 0
        sleep, 300
        return
    }
*/
    ;MsgBox, %clear_flag%
;    Sendinput, {Down}
;    sleep, 100
    click 900 385 ; click king
    sleep, 101
    click 900 385 ; click king
    sleep, 100
    ;Space
    Sendinput, {Space}
    sleep, 103
;    Sendinput, {Down}
;    sleep, 100
    click 900 385 ; click king
    sleep, 101
    click 900 385 ; click king
    sleep, 103
    ;Space
    Sendinput, {Space}
    sleep, 102
    ;Space
    Sendinput, {Space}
    sleep, 100
    ;Space
    Sendinput, {Space}
    sleep, 104
    ;Space
    Sendinput, {Space}
    sleep, 102
    ;s
    Sendinput, {s} ; item s
    sleep, 101
    ;pd
    Sendinput, {PgDn}
    sleep, 100
    Sendinput, {PgDn}
    sleep, 103
    Sendinput, {PgDn}
    sleep, 102
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
