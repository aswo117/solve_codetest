;Todo > imagesearch(완) > check ghost house(완) > go to person (완) > pause resume 구현

#NoEnv
#Singleinstance Force ;

Kingdom_name = 바이버 ;왕국 아이디
gosthouse_name = 초인 ;흉출 아이디


\::
click 736 76 ; click king
sleep, 150
click 736 76 ; click king
sleep, 150
;Space
Sendinput, {Space}
sleep, 200 ; delay 0.1s
;Space
Sendinput, {Space}
sleep, 200
;??
Sendinput, {Down}
sleep, 200
;Space
Sendinput, {Space}
sleep, 200
Sendinput, {Down}
sleep, 200
;Space
Sendinput, {Space}
sleep, 200
;Space
Sendinput, {Space}
sleep, 200
;Space
Sendinput, {Space}
sleep, 200
;Space
Sendinput, {Space}
sleep, 200
;s
Sendinput, {s} ; item s
sleep, 200
;pd
Sendinput, {PgDn}
sleep, 200
;pd
Sendinput, {PgDn}
sleep, 200
;1.5s delay
sleep, 1500

teleport(name)
{
    Sendinput, {u} ; item use
    sleep, 100
    Sendinput, {i} ; yello item
    sleep, 100
    Sendinput, {shift down} ; press shift
    sleep, 100
    Sendinput, {z} ; use magic
    sleep, 100
    Sendinput, {shift up} ; release shift
    sleep, 100
    Sendinput, {x} ; release chuldoo
    sleep, 100
    Sendinput, %name% ;출두 name?
    sleep, 100
    Sendinput, {enter}
    sleep, 100
    return
}

ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Bitch.png
if (ErrorLevel = 0)
{
    teleport(gosthouse_name)
}
ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Fire.png
if (ErrorLevel = 0)
{
    teleport(gosthouse_name)
}
ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Egg.png
if (ErrorLevel = 0)
{
    teleport(gosthouse_name)
}
return

o:: ; 출두 본궁
teleport(Kingdom_name)
return

F4::
ExitApp
