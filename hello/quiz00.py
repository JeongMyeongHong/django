import random
from domains import my100, my_random, member_choice

from hello import Member


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
    return account


def withdraw(account, withdraw):
    account = account - withdraw
    print(f'{withdraw}원을 출금하였습니다. 잔고는 {account} 입니다')
    return account


def chkaccount(name, account):
    print(f'{name} 님의 현재 잔액은 {account}원 입니다.')


class Quiz00:
    def __init__(self):
        pass

    def quiz00calculator(self):
        num1 = my100()
        num2 = my100()
        opcode_num = my_random(0, 4)
        opcode_symbol = ['+', '-', '*', '/', '%']
        opcode = opcode_symbol[opcode_num]
        print(f'{num1} {opcode} {num2} = {calculator(num1, opcode, num2): .1f}')
        return None

    def quiz01bmi(self):
        this = Member()
        this.name = member_choice()
        this.height = my_random(160, 190)
        this.weight = my_random(50, 100)
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
        print(my_random(1, 6))
        return None

    def quiz03rps(self):
        user = random.randint(1, 3)
        com = random.randint(1, 3)
        rps = ['가위', '바위', '보']
        res = 'Draw' if user == com else 'Win' if (user - 1) == com % 3 else 'Lose'
        print(f'User : {rps[user - 1]}\nCom : {rps[com - 1]}\n{res}')

        return None

    def quiz04leap(self):
        '''
        In Java
        String res = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) ? '윤년': '평년'
        '''
        year = my_random(1000, 2022)
        res = '윤년' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '평년'
        print(f'{year}년은 {res}입니다.')
        return None

    def quiz05grade(self):
        name = member_choice()
        kr = my100()
        en = my100()
        math = my100()
        avg = (kr + en + math) / 3
        res = '합격' if avg >= 60 else '불합격'
        print(f'{name}의 성적표\n국어: {kr} 영어: {en} 수학: {math}\n평균: {avg:.1f}\n결과: {res}')
        return None

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        print(members[my_random(0, len(members) - 1)])
        return None

    def quiz07lotto(self):
        sel_num = random.sample(range(1, 46), 6)
        sel_num.sort()
        prize_num = random.sample(range(1, 46), 7)
        bonus_num = prize_num[6]
        del prize_num[6]
        print(len(prize_num))
        prize_num.sort()

        cnt = 0
        res = ''
        rank = '꽝'
        print('내가 고른 번호')
        print(sel_num)
        print('당첨 번호')
        print(f'{prize_num} + {bonus_num}')

        for i in prize_num:
            for j in sel_num:
                if i == j:
                    cnt += 1
                    res += f'{i} '
                    break

        if cnt == 6:
            rank = '1등'
        elif cnt == 5:
            if bonus_num in sel_num:
                rank = '2등'
                res += f'{bonus_num} '
            else:
                rank = '3등'
        elif cnt == 4:
            rank = '4등'
        elif cnt == 3:
            rank = '5등'
        elif cnt == 0:
            res = '없음'

        print(f'맞은 번호는 {res}이며 {rank}입니다.')
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        """
        name = member_choice()
        account = my_random(0, 1000) * 10  # 최초 잔액 설정
        deposit_money = my_random(0, 1000) * 10
        withdraw_money = my_random(0, 1000) * 10
        while 1:
            sel = input('0. Exit 1. 입금 2. 출금 3. 잔고 확인')
            if sel == '1':
                account = deposit(account, deposit_money)
            elif sel == '2':
                if account >= withdraw_money:
                    account = withdraw(account, withdraw_money)
                else:
                    print('잔액이 부족 합니다.')
            elif sel == '3':
                chkaccount(name, account)
            else:
                break
        """
        Account.main()
        return None

    def quiz09gugudan(self):  # 책받침 구구단
        for i in (2, 6):
            for j in range(1, 10):
                for k in range(0, 4):
                    print(f'{i + k} * {j} = {(i + k) * j}\t', end=' ')
                print()
            print()
        return None


'''
08번 문제 해결을 위한 클래슨느 다음과 같다.
[요구사항(RFP)]
은행 이름은 : 비트은행
입금자 이름, 계좌번호, 금액 속성값으로 계좌를 생성한다.
계좌번호는 xxx-xx-xxxxxx 형태로 랜덤하게 생성된다.(comprehension)으로 생성
금액은 100~999 사이로 랜덤하게 입금된다.(단위는 만단위로 암묵적으로 판단한다)
'''


class Account:
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = member_choice() if name is None else name
        self.account_number = self.creat_account_number() if account_number is None else account_number
        self.money = my_random(100, 999) if money is None else money
        print(f'{self.to_string()}...개설 되었습니다.')

    def to_string(self) -> str:
        return f'은행 : {self.BANK_NAME}\t' \
               f'입금주 : {self.name}\t' \
               f'계좌번호 : {self.account_number}\t' \
               f'잔고 : {self.money}만원'

    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    '''def deposit(self, account_number, deposit_money):
        money += deposit_money
        print(f'{deposit_money}원을 입금하였습니다. 잔고는 {account} 입니다')
        return account'''

    def withdraw(self, account, withdraw):
        '''account = account - withdraw
        if account >= withdraw_money:
            account = withdraw(account, withdraw_money)
            print(f'{withdraw}원을 출금하였습니다. 잔고는 {account} 입니다')

        else:
            print('잔액이 부족 합니다.')
        return account'''

    @staticmethod
    def creat_account_number():
        account_number = f'{str(my_random(0, 999)).zfill(3)}-' \
                         f'{str(my_random(0, 99)).zfill(2)}-' \
                         f'{str(my_random(0, 999999)).zfill(6)}'
        account_number2 = "".join(['-' if i == 3 or i == 6 else str(my_random(0, 9)) for i in range(13)])
        account_number3 = [str(my_random(0, 9)) for i in range(11)]
        account_number4 = [str(my_random(0, 9)) for i in range(11)]
        account_number4.insert(3, '-')
        account_number4.insert(6, '-')
        return account_number2

    @staticmethod
    def main():
        ls = []
        res = ''
        res2 = ''
        while 1:
            menu = input('0. 종료 1. 계좌개설 2. 계좌목록 3. 입금 4. 출금 5. 계좌해지')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(None, None, None))
            elif menu == '2':
                res = '\n'.join([i.to_string() for i in ls])
            elif menu == '3':
                account_number = input('입금할 계좌번호')
                deposit_money = input('입금액')
            elif menu == '4':
                account_number = input('입금할 계좌번호')
                withdraw_money = input('출금액')
            elif menu == '5':
                pass
            print(res)


