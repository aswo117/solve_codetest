;SciTE4AutoHotkey + autohotkey 1.1 설치 필요
;좌표는 window spy 참고
;op[], exit = F4

#NoEnv
#Singleinstance Force ; 스크립트 꺼지고 새로 켜짐

$o:: ; 출두 본궁
Sendinput, {u} ; item use
sleep, 80
Sendinput, {i} ; yello item
sleep, 80
Sendinput, {shift down} ; press shift
sleep, 80
Sendinput, {z} ; press use magic
sleep, 80
Sendinput, {shift up} ; release shift
sleep, 80
Sendinput, {x} ; release chuldoo
sleep, 80
Sendinput, 죠르르 ;출두 name?
sleep, 80
Sendinput, {enter}
sleep, 80
return

$p:: ; 출두 해골
Sendinput, {u} ; item use
sleep, 80
Sendinput, {i} ; yello item
sleep, 80
Sendinput, {shift down} ; press shift
sleep, 80
Sendinput, {z} ; use magic
sleep, 80
Sendinput, {shift up} ; release shift
sleep, 80
Sendinput, {x} ; release chuldoo
sleep, 80
Sendinput, 죠르르 ;출두 name?
sleep, 80
Sendinput, {enter}
sleep, 80
return

$[:: ; 출두 사마귀
Sendinput, {u} ; item use
sleep, 80
Sendinput, {i} ; yello item
sleep, 80
Sendinput, {shift down} ; press shift
sleep, 80
Sendinput, {z} ; use magic
sleep, 80
Sendinput, {shift up} ; release shift
sleep, 80
Sendinput, {x} ; chuldoo
sleep, 80
Sendinput, 죠르르 ;출두 name?
sleep, 80
Sendinput, {enter}
sleep, 80
return

$]:: ; 출두 흑해
Sendinput, {u} ; item use
sleep, 80
Sendinput, {i} ; yello item
sleep, 80
Sendinput, {shift down} ; press shift
sleep, 80
Sendinput, {z} ; use magic
sleep, 80
Sendinput, {shift up} ; release shift
sleep, 80
Sendinput, {x} ; chuldoo
sleep, 80
Sendinput, 죠르르 ;출두 name?
sleep, 80
Sendinput, {enter}
sleep, 80
return

F4:: ;hotkey exit
exitapp
