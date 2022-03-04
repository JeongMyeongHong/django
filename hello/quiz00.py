import random

from hello import Member


def myRandom(start, end):
    return random.randint(start, end)


def my100():
    return myRandom(1, 100)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


def calculator(num1, opcode, num2):
    if opcode == '+':
        return add(num1, num2)
    elif opcode == '-':
        return sub(num1, num2)
    elif opcode == '*':
        return mul(num1, num2)
    elif opcode == '/':
        return div(num1, num2)
    elif opcode == '%':
        return mod(num1, num2)
    else:
        return f'error (opcode is not valid)'


def deposit(account, deposit):
    account = account + deposit
    print(f'{deposit}원을 입금하였습니다. 잔고는 {account} 입니다')
    return None


def withdraw(account, withdraw):
    account = account - withdraw
    print(f'{withdraw}원을 출금하였습니다. 잔고는 {account} 입니다')
    return None


class Quiz00:
    def __init__(self):
        pass

    def quiz00calculator(self):
        num1 = my100()
        num2 = my100()
        opcode_num = myRandom(0, 4)
        opcode_symbol = ['+', '-', '*', '/', '%']
        opcode = opcode_symbol[opcode_num]
        print(f'{num1} {opcode} {num2} = {calculator(num1, opcode, num2): .1f}')
        return None

    def quiz01bmi(self):
        this = Member()
        this.name = self.quiz06memberChoice()
        this.height = myRandom(160, 190)
        this.weight = myRandom(50, 100)
        bmi_res = this.weight * 10000 / this.height / this.height
        if bmi_res > 25.0:
            res = '비만'
        elif bmi_res > 23.0:
            res = '과체중'
        elif bmi_res > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{this.name} 님은 \n키 : {this.height}, 몸무게 : {this.weight}\n결과 : {res}입니다.')

    def quiz02dice(self):
        print(myRandom(1, 6))
        return None

    def quiz03rps(self):
        user = random.randint(1, 3)
        com = random.randint(1, 3)
        rps = ['가위', '바위', '보']
        if user == com:
            res = f'Draw'
        elif (user - 1) == com % 3:
            res = f'Win'
        else:
            res = f'Lose'
        print(f'User : {rps[user - 1]}\nCom : {rps[com - 1]}\n{res}')

        return None

    def quiz04leap(self):
        year = myRandom(0, 3000)
        if year % 4 == 0 & year % 100 != 0 | year % 400 == 0:
            res = '윤년'
        else:
            res = '평년'
        print(f'{year}년은 {res}입니다.')
        return None

    def quiz05grade(self):
        name = self.quiz06memberChoice()
        kr = my100()
        en = my100()
        math = my100()
        avg = (kr + en + math) / 3
        if avg >= 60:
            res = '합격'
        else:
            res = '불합격'
        print(f'{name}의 성적표\n국어: {kr} 영어: {en} 수학: {math}\n평균: {avg:.1f}\n결과: {res}')
        return None

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        print(members[myRandom(0, len(members) - 1)])
        return members[myRandom(0, len(members) - 1)]

    def quiz07lotto(self):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        for i in [lotto]:
            print(f'{i}\t', end='')
            print()
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = '홍길동'
        account = myRandom(0, 1000) * 10
        deposit_money = myRandom(0, 1000) * 10
        withdraw_money = myRandom(0, 1000) * 10
        print(f'{name} 님의 현재 잔액은 {account}원 입니다.')
        print(f'{deposit_money}원을 입금합니다.')
        deposit(account, deposit_money)
        print(f'{withdraw_money}원을 출금합니다.')
        withdraw(account, withdraw_money)
        return None

    def quiz09gugudan(self):  # 책받침구구단
        for i in (2, 6):
            for j in range(1, 10):
                for k in range(0, 4):
                    print(f'{i + k} * {j} = {(i + k) * j}\t', end=' ')
                print()
            print()
        return None
