import curses
def prwin(n, window):
    space,cordinate_y,i,re = "",0,0,""
    while i < len(n):
        if n[i] == " ":
            i += 1
            continue
        if (n[i] == "[" or n[i] == "{") and (n[i + 1] != "]" and n[i + 1] != "}"):
            window.addstr(n[i])
            cordinate_y+=1
            window.move(cordinate_y, 0)
            space += "  "
            window.addstr(space)
            re += n[i] + "/" + space
            i += 1
        elif (n[i] == "[" or n[i] == "{") and (n[i + 1] == "]" or n[i + 1] == "}"):
            window.addstr(n[i])
            window.addstr(n[i + 1])
            re += n[i] + n[i + 1]
            i += 2
        elif n[i] == ",":
            window.addstr(n[i])
            cordinate_y += 1
            window.move(cordinate_y, 0)
            window.addstr(space)
            re += n[i] + "/" + space
            i += 1
        elif n[i] == "]" or n[i] == "}":
            cordinate_y += 1
            window.move(cordinate_y, 0)
            space = space.replace(" ", "", 2)
            window.addstr(space)
            window.addstr(n[i])
            re += "/" + space + n[i]
            i += 1
        elif n[i] == '"':
            window.addstr(n[i])
            t = 0
            re += n[i]
            i += 1
            while n[i + t] != '"':
                window.addstr(n[i + t])
                re += n[i + t]
                t += 1
            re += n[i + t]
            window.addstr(n[i + t])
            i += t + 1
            if i >= len(n):
                i += 1
                continue
            if n[i] == ":":
                window.addstr(n[i])
                re += ":"
                i += 1
        elif n[i] in "-0123456789.":
            p = 0
            while n[i + p] in "-0123456789.":
                window.addstr(n[i + p])
                re += n[i + p]
                p += 1
            i += p
        elif n[i] == "f":
            window.addstr("False")
            re += "False"
            i += 5
        elif n[i] == "t":
            window.addstr("True")
            re += "True"
            i += 4
        elif n[i] == "n":
            window.addstr("None")
            re += "None"
            i += 4
    return re
def beautifie(mystring, window):
    i=0
    window.clear()
    newstring=""
    while i<len(mystring):
        if mystring[i]== "/":
            newstring+="\n"
        else:
            newstring+=mystring[i]
        i+=1
    window.addstr(newstring)
def inline(line, mystring):
    j,i=0,1
    while i!=line:
        j+=1
        if mystring[j]== "/":
            i+=1
    j+=1
    p=0
    while mystring[j + p]== " ":
        p+=1
    return (p,p+j)
def save(mystring):
    i,saved=0,[]
    while i<len(mystring):
        if mystring[i]== "[" and mystring[i + 1]!= "]":
            c=1
            j=0
            s="["
            while c!=0:
                j+=1
                if mystring[i + j]== "[":
                    c+=1
                elif mystring[i + j]== "]":
                    c-=1
                s+=mystring[i + j]
            saved.extend([[1,s]])
        elif mystring[i]== "{" and mystring[i + 1]!= "}":
            c=1
            j=0
            s="{"
            while c!=0:
                j+=1
                if mystring[i + j]== "{":
                    c+=1
                elif mystring[i + j]== "}":
                    c-=1
                s+=mystring[i + j]
            saved.extend([[1,s]])
        i+=1
    return saved
def pr(saved, window):
    i=0
    re=""
    counter = -1
    while i<len(saved[0][1]):
        if (saved[0][1][i]=="[" and saved[0][1][i+1]!="]"):
            counter+=1
            if saved[counter][0]==0:
                re += "[...]"
                c = 1
                while c != 0:
                    i += 1
                    if saved[0][1][i] == "[":
                        c += 1
                    elif saved[0][1][i] == "]":
                        c -= 1
            else:
                re += saved[0][1][i]
        elif (saved[0][1][i]=="{" and saved[0][1][i+1]!="}"):
            counter += 1
            if saved[counter][0] == 0:
                re += "{...}"
                c = 1
                while c != 0:
                    i += 1
                    if saved[0][1][i] == "{":
                        c += 1
                    elif saved[0][1][i] == "}":
                        c -= 1
            else:
                re += saved[0][1][i]
        else:
            re+=saved[0][1][i]
        i+=1
    beautifie(re, window)
    return re
with open("name.json") as file:
    mystring = file.read()
mystring = mystring[:len(mystring) - 1]
window = curses.initscr()
window.keypad(True)
curses.noecho()
mystring = prwin(mystring, window)
saved = save(mystring)
curses.curs_set(2)
window.move(0, 0)
cordinate_y,cordinate_x,line=0,0,1
while True:
    c = window.getch()
    try:
        if c == 27:
            break
        elif c == 258:
            cordinate_y += 1
            line += 1
            cordinate_x, o = inline(line, mystring)
        elif c == 259:
            cordinate_y -= 1
            line -= 1
            cordinate_x, o = inline(line, mystring)
        elif c == 260:
            o, where = inline(line, mystring)
            if where == 1:
                where = 0
            if mystring[where] == "[" and mystring[where + 1] != "]" and mystring[where + 1] != ".":
                i, counter = 0, -1
                newstate = ""
                while i < len(mystring):
                    if (mystring[i] == "[" and mystring[i + 1] != "]") or (
                            mystring[i] == "{" and mystring[i + 1] != "}") and i <= where:
                        counter += 1
                    newstate += mystring[i]
                    if i == where:
                        newstate += "...]"
                        t = 1
                        while t != 0:
                            i += 1
                            if mystring[i] == "[":
                                t += 1
                            elif mystring[i] == "]":
                                t -= 1
                    i += 1
                saved[counter][0] = 0
                mystring = newstate
                beautifie(mystring, window)
            elif mystring[where] == "{" and mystring[where + 1] != "}" and mystring[where + 1] != ".":
                i, counter = 0, -1
                newstate = ""
                while i < len(mystring):
                    if (mystring[i] == "[" and mystring[i + 1] != "]") or (
                            mystring[i] == "{" and mystring[i + 1] != "}") and i <= where:
                        counter += 1
                    newstate += mystring[i]
                    if i == where:
                        newstate += "...}"
                        t = 1
                        while t != 0:
                            i += 1
                            if mystring[i] == "{":
                                t += 1
                            elif mystring[i] == "}":
                                t -= 1
                    i += 1
                saved[counter][0] = 0
                mystring = newstate
                beautifie(mystring, window)
            else:
                t = 1
                k = 0
                while t != 0:
                    k += 1
                    if mystring[where - k] == "[" or mystring[where - k] == "{":
                        t -= 1
                    elif mystring[where - k] == "]" or mystring[where - k] == "}":
                        t += 1
                    elif mystring[where - k] == "/":
                        cordinate_y -= 1
                        line -= 1
                cordinate_x, o = inline(line, mystring)
        elif c == 261:
            o, where = inline(line, mystring)
            if where == 1:
                where = 0
            if mystring[where] == "[" and mystring[where + 1] == ".":
                i, counter = 0, -1
                while i <= where:
                    if (mystring[i] == "[" and mystring[i + 1] != "]") or (mystring[i] == "{" and mystring[i + 1] != "}"):
                        counter += 1
                    i += 1
                saved[counter][0] = 1
                mystring = pr(saved, window)
            elif mystring[where] == "{" and mystring[where + 1] == ".":
                i, counter = 0, -1
                while i <= where:
                    if (mystring[i] == "[" and mystring[i + 1] != "]") or (mystring[i] == "{" and mystring[i + 1] != "}"):
                        counter += 1
                    i += 1
                saved[counter][0] = 1
                mystring = pr(saved, window)
            else:
                t, k = 1, 0
                if mystring[where + 1] == "]":
                    k += 1
                while t != 0:
                    k += 1
                    if mystring[where + k] == "]":
                        t -= 1
                    elif mystring[where + k] == "[":
                        t += 1
                    elif mystring[where + k] == "/":
                        cordinate_y += 1
                        line += 1
                cordinate_x, o = inline(line, mystring)
        window.move(cordinate_y, cordinate_x)
    except:
        continue
curses.endwin()
