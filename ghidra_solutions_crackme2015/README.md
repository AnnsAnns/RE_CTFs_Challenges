#### My solutions/ghidra workspace for https://github.com/Maijin/radare2-workshop-2015

I forgot to write the first 4 passwords down, but honestly, those are so easy, that I doubt anyone even cares about them. You shouldn't look at the passwords anyways :P.
0x01: Just search for strings and you'll find the password in some statement.
0x01: 5274 was the answer
0x02: Mostly string searching.
0x03: 5274, once again.
0x04: 555, or any combinations of numbers that total 15 (Could probably be 1^15 too). It iterates through the string and adds each letter to a var. If the var ends up at 15 you solved it.
0x05: 880, it starts the same way 0x04 does but the it checks if the total is 16 (0x10). If it is 16, it calls _parell which adds AND 1. Lastly it checks if the number equals 0 when doing that.
0x06: 880 and $ENV:LOLO=1. This one added a level ob obscurity and now checks for the env. variable LOLO.
0x07: 88F and $ENV:LOLO=1. Honestly, this was a lot more confusing that 0x08 but it's just extremely obfuscated.
0x08: 880 and $ENV:LOLO=1. A lot more obfuscation but that's mostly it. As long as you don't fall into the traps, it's as hard as 0x06.
0x09: 880 and $ENV:LOLO=1. Once again, just more obfuscated.