import sqlite3;import random;from pathlib import Path;h=0;K=Path('./U.db')
if K.is_file()==False:
    N=sqlite3.connect('U.db');Q=N.cursor();Q.execute("CREATE TABLE U(\
pn TEXT,\
password TEXT,\
P INT NOT NULL,\
PRIMARY KEY(pn))");N.commit()
while h==0:
    SL=input('Sign Up Or Login: ');SL=SL.upper()
    if SL=='LOGIN':
        i=0
        while i==0:
            N=sqlite3.connect('U.db');Q=N.cursor();U=input('Enter Username: ');Q.execute('SELECT*from U where pn="'+U+'"');R=Q.fetchall()
            if bool(R)==False:print('Wrong Username Or You Did Not Create Your Account.')
            else:i+=1
        P=R[0];P=P[2]
        if len(R)>0:
            UI=R[0];T=UI[1];E=input('Enter Password: ')
            while(E!=T):E=input('Password Is Wrong Please Try Again: ')
            print('Points: ',P);h+=1
    elif SL=='SIGN UP':
        N=sqlite3.connect('U.db');Q=N.cursor();U=input('Enter Username: ');E=input('Welcome, Please Create Your Password: ');P=1000;Q.execute('INSERT INTO U VALUES(?,?,?)',(U,E,P));N.commit();R=Q.fetchall();h+=1
    else:print('Enter A Proper Command')
def G():
    Q.execute('SELECT pn,P FROM U ORDER BY P');R2=Q.fetchall();a=len(R2);a-=1
    while (a<=len(R2) and a>=0):
        R3=R2[a];print(R3[0],'-',R3[1]);a-=1
    Q.execute('SELECT*from U where pn="'+U+'"');R=Q.fetchall();P=R[0];P=P[2];k=0
    while k==0:
        try:B=eval((input('Enter Bet: ')))
        except NameError:print('Enter A Proper Number')
        else:
            if B>P:print('Bet Too High')
            elif B<=0:print("Hey,You Can't Bet Less Than 0 Points")
            elif B<=P:P-=B;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));k+=1
    D=('A','2','3','4','5','6','7','8','9','10','J','Q','K');C=''.join(random.sample(D,1));C2=''.join(random.sample(D,1));Y=''.join(random.sample(D,1));Y2=''.join(random.sample(D,1));O=Y;O2=Y2;R=C;R2=C2;l=0
    if O=='A':
        while l==0:
            O=eval(input('Enter Value For Ace Card (1 or 11) (This Is Your First Card): '))
            if O==1 or O==11:l+=1
            else:print('Invalid Number')
    elif O=='2':O=2
    elif O=='3':O=3
    elif O=='4':O=4
    elif O=='5':O=5
    elif O=='6':O=6
    elif O=='7':O=7
    elif O=='8':O=8
    elif O=='9':O=9
    else:O=10
    if O2=='A':
        l=0
        while l==0:
            print('Your First Card Is '+ Y);O2=eval(input('Enter Value For Ace Card (1 or 11): '))
            if O2==1 or O2==11:l+=1
            else:print('Invalid Number')
    elif O2=='2':O2=2
    elif O2=='3':O2=3
    elif O2=='4':O2=4
    elif O2=='5':O2=5
    elif O2=='6':O2=6
    elif O2=='7':O2=7
    elif O2=='8':O2=8
    elif O2=='9':O2=9
    else:O2=10
    X=O+O2;print('You: ',Y,Y2,'Sum =',X)
    if X==21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Got To 21 First.');G()
    if R=='A':R=11
    elif R=='2':R=2
    elif R=='3':R=3
    elif R=='4':R=4
    elif R=='5':R=5
    elif R=='6':R=6
    elif R=='7':R=7
    elif R=='8':R=8
    elif R=='9':R=9
    else:R=10
    W=R;print('Computer: ',C,'Sum =',W)
    if R2=='A':
        if W+11<=21:R2=11
        else:R2=1
    elif R2=='2':R2=2
    elif R2=='3':R2=3
    elif R2=='4':R2=4
    elif R2=='5':R2=5
    elif R2=='6':R2=6
    elif R2=='7':R2=7
    elif R2=='8':R2=8
    elif R2=='9':R2=9
    else:R2=10
    W+=R2
    if W==21:
        print('Computer: ',C,C2,'Sum =',W);print('The Computer Won On Its First Hand')
        if P==0:P+=1
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();G()
    if X<21:
        Z=input('Hit, Stand Or Double: ');UC0=Z.upper();j=0
        while j==0:
            if UC0!='HIT' and UC0!='STAND' and UC0!='DOUBLE':print('Enter A Proper Command: ');Z=input('Hit, Stand or Double: ');UC0=Z.upper()
            elif UC0=='DOUBLE':
                if B>P:print('You Do Not Have Enough Points To Double');Z=input('Hit or Stand: ');UC0=Z.upper()
                else:P-=B;B*=2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));j+=1;UC0='HIT'
            else:j+=1
    if UC0=='HIT':
        Y3=''.join(random.sample(D,1));O=Y3;l=0
        if O=='A':
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:l+=1
                else:print('Invalid Number')
        elif O=='2':O=2
        elif O=='3':O=3
        elif O=='4':O=4
        elif O=='5':O=5
        elif O=='6':O=6
        elif O=='7':O=7
        elif O=='8':O=8
        elif O=='9':O=9
        else:O=10
        X+=O;I1='i';print('You: ',Y,Y2,Y3,'Sum =',X)
        if X==21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Got To 21 First.');G()
        if X>21:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As You Got Over 21 And Busted.');G()
            if X==21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Got To 21 First.');G()
    else:print('You: ',Y,Y2,'Sum =',X)
    if W<=15:Z2='Hit'
    if X>W and UC0=='STAND':Z2='Hit'
    else:Z2='Stand'
    if Z2=='Hit':
        C3=''.join(random.sample(D,1));R=C3
        if R=='A':
            if W+11<=21:R=11
            else:R=1
        elif R=='2':R=2
        elif R=='3':R=3
        elif R=='4':R=4
        elif R=='5':R=5
        elif R=='6':R=6
        elif R=='7':R=7
        elif R=='8':R=8
        elif R=='9':R=9
        else:R=10
        W+=R;J1='i';print('Computer: ',C,C2,C3,'Sum =',W)
        if W==21:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As The Computer Got To 21 First.');G()
        if W>21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As The Computer Got Over 21 And Busted.');G()
    elif Z2=='Stand':print('Computer: ',C,C2,'Sum =',W)
    Z5=input('Hit, Stand or Double: ');UC=Z5.upper();j=0
    while j==0:
        if UC!='HIT' and UC!='STAND' and UC!='DOUBLE':print('Enter A Proper Command: ');Z5=input('Hit, Stand or Double: ');UC=Z5.upper()
        elif UC=='DOUBLE':
            if B>P:print('You Do Not Have Enough Points To Double');Z5=input('Hit or Stand: ');UC=Z5.upper()
            else:P-=B;B*=2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));j+=1;UC='HIT'
        else:j+=1
    if UC=='HIT':
        Y4=''.join(random.sample(D,1));O=Y4
        if O=='A':
            l=0
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:l+=1
                else:print('Invalid input')
        elif O=='2':O=2
        elif O=='3':O=3
        elif O=='4':O=4
        elif O=='5':O=5
        elif O=='6':O=6
        elif O=='7':O=7
        elif O=='8':O=8
        elif O=='9':O=9
        else:O=10
        X+=O
        try:I1
        except NameError:I2='i';print('You: ',Y,Y2,Y4,'Sum =',X)
        else:I2='i';print('You: ',Y,Y2,Y3,Y4,'Sum =',X)
        if X==21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Got To 21 First.');G()
        if X>21:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As You Got Over 21 And Busted.');G()
    if UC=='STAND':
        try:I1
        except NameError:print('You: ',Y,Y2,'Sum =',X)
        else:print('You: ',Y,Y2,Y3,'Sum =',X)
    if W<=15:Z4='Hit'
    if X>W and UC=='STAND':Z4='Hit'
    else:Z4='Stand'
    if Z4=='Hit':
        C4=''.join(random.sample(D,1));R=C4
        if R=='A':
            if W+11<=21:R=11
            else:R=1
        elif R=='2':R=2
        elif R=='3':R=3
        elif R=='4':R=4
        elif R=='5':R=5
        elif R=='6':R=6
        elif R=='7':R=7
        elif R=='8':R=8
        elif R=='9':R=9
        else:R=10
        W+=R
        try:J1
        except NameError:J2='i';print('Computer: ',C,C2,C4,'Sum =',W)
        else:J2='i';print('Computer: ',C,C2,C3,C4,'Sum =',W)
        if W==21:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As The Computer Got To 21 First.');G()
        if W>21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As The Computer Got Over 21 And Busted.');G()
    else:
        try:J1
        except NameError:print('Computer: ',C,C2,'Sum =',W)
        else:print('Computer: ',C,C2,C3,'Sum =',W)
    Z5=input('Hit, Stand or Double: ');UC2=Z5.upper();j=0
    while j==0:
        if UC2!='HIT' and UC2!='STAND' and UC2!='DOUBLE':print('Enter A Proper Command: ');Z5=input('Hit, Stand or Double: ');UC2=Z5.upper()
        elif UC2=='DOUBLE':
            if B>P:print('You Do Not Have Enough Points To Double');Z5=input('Hit or Stand: ');UC0=Z5.upper()
            else:P-=B;B*=2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));j+=1;UC2='HIT'
        else:j+=1
    if UC2=='HIT':
        Y5=''.join(random.sample(D,1));O=Y5
        if O=='A':
            l=0
            while l==0:
                O=eval(input('Enter Value For Ace Card (1 or 11): '))
                if O==1 or O==11:l+=1
                else:print('Invalid number')
        elif O=='2':O=2
        elif O=='3':O=3
        elif O=='4':O=4
        elif O=='5':O=5
        elif O=='6':O=6
        elif O=='7':O=7
        elif O=='8':O=8
        elif O=='9':O=9
        else:O=10
        X+=O
        try:I1
        except NameError:
            try:I2
            except NameError:print('You: ',Y,Y2,Y5,'Sum =',X)
            else:print('You: ',Y,Y2,Y4,Y5,'Sum =',X)
        else:
            try:I2
            except NameError:print('You: ',Y,Y2,Y3,Y5,'Sum =',X)
            else:print('You: ',Y,Y2,Y3,Y4,Y5,'Sum =',X)
        if X==21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Got To 21 First.');G()
        if X>21:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As You Got Over 21 And Busted.');G()
    else:
        try:I1
        except NameError:
            try:I2
            except NameError:print('You: ',Y,Y2,'Sum =',X)
            else:print('You: ',Y,Y2,Y4,'Sum =',X)
        else:
            try:I2
            except NameError:print('You: ',Y,Y2,Y3,'Sum =',X)
            else:print('You: ',Y,Y2,Y3,Y4,'Sum =',X)
    if W<=15:Z6='Hit'
    elif X>W and UC2=='STAND':Z6='Hit'
    else:Z6='Stand'
    if Z6=='Hit':
        C5=''.join(random.sample(D,1));R=C5
        if R=='A':
            if W+11<=21:R=11
            else:R=1
        elif R=='2':R=2
        elif R=='3':R=3
        elif R=='4':R=4
        elif R=='5':R=5
        elif R=='6':R=6
        elif R=='7':R=7
        elif R=='8':R=8
        elif R=='9':R=9
        else:R=10
        W+=R
        try:J1
        except NameError:
            try:J2
            except NameError:print('Computer: ',C,C2,C5,'Sum =',W)
            else:print('Computer: ',C,C2,C4,C5,'Sum =',W)
        else:
            try:J2
            except NameError:print('Computer: ',C,C2,C3,C5,'Sum =',W)
            else:print('Computer: ',C,C2,C3,C4,C5,'Sum =',W)
    else:
        try:J1
        except NameError:
            try:J2
            except NameError:print('Computer: ',C,C2,'Sum =',W)
            else:print('Computer: ',C,C2,C4,'Sum =',W)
        else:
            try:J2
            except NameError:print('Computer: ',C,C2,C3,'Sum =',W)
            else:print('Computer: ',C,C2,C3,C4,'Sum =',W)
    if W>21:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As The Computer Got Over 21 And Busted.');G()
    if X>21:
        if P==0:P+=1
        Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As You Got Over 21 And Busted.');G()
    else:
        if X>W:P+=B*2;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Won As You Stood With A Higher Score Than The Computer.');G()
        if W>X:
            if P==0:P+=1
            Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('You Lost As You Stood With A Lower Score Than The Computer.');G()
        if W==X:P+=B;Q.execute('REPLACE INTO U VALUES(?,?,?)',(U,E,P));N.commit();print('Points: ',P);print('It was a draw!');G()
G()