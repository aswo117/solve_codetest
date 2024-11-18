;Todo > imagesearch > check ghost house(완) > go to person (완) > pause resume 구현

#NoEnv
#Singleinstance Force ;

Kingdom_name = 추억보정바람 ;왕국 아이디
gosthouse_name = 홈령짬뽕 ;흉출 아이디

global clear_flag = 0

teleport(name)
{
	global clear_flag = 0
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

o:: ; 출두 본궁
teleport(Kingdom_name)
return

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

w:: ; 동동-공증
Sendinput, {u} ; item use
sleep, 100
Sendinput, {u} ; item use
sleep, 100
Sendinput, {3} ;
sleep, 100
return

e:: ;마비 돌리기
Sendinput, {6} ; 
sleep, 50
Sendinput, {Right} ;
sleep, 50
Sendinput, {Enter} ;
sleep, 50
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

F5:: ; 메크로 잠시 멈춤
Suspend
return

\:: ; 왕퀘용
Loop
{
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
	
	;본궁 출두 후 처리시 케릭 아래로 이동 방지
	if (global clear_flag == 0)
	{
		global clear_flag = 1
		continue
	}
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
    sleep, 250
    ;pd
    Sendinput, {PgDn}
    sleep, 250
    ;1.5s delay
    sleep, 1500

    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Bitch.png
    if (ErrorLevel = 0)
    {
        teleport(gosthouse_name)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Fire.png
    if (ErrorLevel = 0)
    {
        teleport(gosthouse_name)
        break
    }
    ImageSearch, vx, vy, 0, 0, 1920, 1080, *30 Egg.png
    if (ErrorLevel = 0)
    {
        teleport(gosthouse_name)
        break
    }
	;Todo) 국내성 이미지 추가 필요
	;독충, 몽달, 빗자루
}
