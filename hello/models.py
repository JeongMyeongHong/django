import random


def main():
    while 1:
        menu = input('0.Exit 1. Calc 2. BMI 3. Grade 4. GradeAuto 5. DICE 6. RandomGenerator 7. RandomChoice '
                     '8. RPS 9. GetPrime 10. LeapYear 11. NumberGolf 12. Lotto 13. Bank 14. Gugudan')
        if menu == '0':
            break

        elif menu == '1':
            q1 = Quiz01Calc(int(input('첫번째 수')), input('연산자'), int(input('두번째 수')))
            res = f'{q1.num1} {q1.opcode} {q1.num2} = {q1.calculator()}'

        elif menu == '2':
            q2 = Quiz02Bmi(input('이름 입력'), int(input('키 입력')), int(input('몸무게 입력')))
            res = f'{q2.name} 님은 키 : {q2.height} 몸무게 : {q2.weight} 결과 : {q2.get_bmi()}'

        elif menu == '3':
            q3 = Quiz03Grade(input('이름 입력'), int(input('국어점수 입력')), int(input('영어점수 입력')), int(input('수학점수 입력')))
            res = f'{q3.name} 님은 {q3.chk_pass()}입니다.'

        elif menu == '4':
            for i in []:
                pass
            q4 = Quiz04GradeAuto(input('이름 입력'), int(input('국어점수 입력')), int(input('영어점수 입력')), int(input('수학점수 입력')))
        elif menu == '5':
            res = Quiz05Dice.cast()
        elif menu == '6':
            q6 = Quiz06RandomGenerator(int(input('시작값 입력.')), int(input('끝값 입력.')))
            res = f'선택된 값은 {q6.cast()} 입니다.'

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            res = q7.extract()

        elif menu == '8':
            q8 = Quiz08Rps(int(input('1.가위 2.바위 3.보')))
            res = f'User : {q8.rsp[q8.user - 1]}\tCom : {q8.rsp[q8.com - 1]} \t 결과 : {q8.battle()}'

        elif menu == '9':
            q9 = Quiz09GetPrime(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
            res = f'{q9.no1}과 {q9.no2}의 사이의 소수는 {q9.get_prime()} 입니다.'


        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('확인하고 싶은 년도를 입력하세요.')))
            res = q10.get_leapyear()

        elif menu == '11':
            q11 = Quiz11NumberGolf()
            while q11.goal(int(input('1~10000 사이의 숫자를 입력하세요'))):
                pass
            res = f'축하합니다 정답입니다.'

        elif menu == '12':
            q12 = Quiz12Lotto()
            q12.print_lotto()
            res = ''

        elif menu == '13':
            q13 = Quiz13Bank(input('이름을 입력해주세요'), int(input('최초 입금액을 입력해주세요')))
            while 1:
                menu = input('0.Exit 1. 입금 2. 출금 3.잔고확인')
                if menu == '0':
                    break
                elif menu == '1':
                    q13.deposit(int(input('입금 금액 입력')))
                elif menu == '2':
                    q13.withdraw(int(input('출금 금액 입력')))
                elif menu == '3':
                    print(f'잔액은 {q13.get_account()}입니다')
            res = '은행어플 종료'

        elif menu == '14':
            Quiz14Gugudan.googoo()
            res = '구구단 끝'

        else:
            res = f'잘못된 선택입니다.'

        print(res)


class Quiz01Calc:

    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2

    def calculator(self):
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()
        elif self.opcode == '%':
            return self.mod()
        else:
            return f'error (opcode is not valid)'


class Quiz02Bmi:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def get_bmi(self):
        bmi_res = self.weight * 10000 / self.height / self.height
        if bmi_res > 25:
            return '비만'
        elif bmi_res > 23:
            return '과체중'
        elif bmi_res > 18.5:
            return '정상'
        else:
            return '저체중'


class Quiz03Grade:
    def __init__(self, name, kr, en, math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math

    def sum(self):
        return self.kr + self.en + self.math

    def avg(self):
        return self.sum() / 3

    def chk_pass(self):
        if self.avg() >= 180:
            return '합격'
        else:
            return '불합격'


class Quiz04GradeAuto:
    def __init__(self, name, kr, en, math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math

    def sum(self):
        return self.kr + self.en + self.math

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        pass

    def chk_pass(self):
        if self.avg() >= 180:
            return '합격'
        else:
            return '불합격'


def my_random(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return my_random(1, 6)


class Quiz06RandomGenerator:
    def __init__(self, start, end):  # 원하는 범위의 정수에서 랜덤값 1개 추출
        self.start = start
        self.end = end

    def cast(self):
        return my_random(self.start, self.end)


class Quiz07RandomChoice:
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def extract(self):
        return self.members[my_random(0, len(self.members) - 1)]


class Quiz08Rps:
    def __init__(self, user):
        self.user = user
        self.rsp = ['가위', '바위', '보']
        self.com = random.randint(1, 3)

    def battle(self):
        if self.user == self.com:
            return f'Draw'
        elif (self.user - 1) % 3 == self.com % 3:
            return f'Win'
        else:
            return f'Lose'


class Quiz09GetPrime:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def get_prime(self):
        res = ''
        for i in range(self.no1, self.no2):
            for j in range(2, i + 1):
                if i == j:
                    res += f'{i} '
                elif i % j == 0:
                    break
        return res


class Quiz10LeapYear:
    def __init__(self, year):
        self.year = year

    def get_leapyear(self):
        if self.year % 4 == 0 & self.year % 100 != 0 | self.year % 400 == 0:
            return '윤년'
        else:
            return '평년'


class Quiz11NumberGolf:
    def __init__(self):
        self.r_num = random.randint(1, 10000)

    def goal(self, num):
        if num == self.r_num:
            return 0
        elif num > self.r_num:
            print(f'{num}보다 작은 숫자 입니다.')
            return 1
        else:
            print(f'{num}보다 큰 숫자 입니다.')
            return 1


class Quiz12Lotto:
    @staticmethod
    def creat_lotto():
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        return lotto

    def print_lotto(self):
        for i in self.creat_lotto():
            print(f'{i}\t', end='')


class Quiz13Bank:  # 이름, 입금, 출금만 구현
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def deposit(self, deposit):
        self.account = self.account + deposit
        print(f'{deposit}원을 입금하였습니다. 잔고는 {self.account} 입니다')

    def withdraw(self, withdraw):
        self.account = self.account - withdraw
        print(f'{withdraw}원을 출금하였습니다. 잔고는 {self.account} 입니다')

    def get_account(self):
        return self.account


class Quiz14Gugudan:  # 책받침구구단
    @staticmethod
    def googoo():
        for i in (2, 6):
            for j in range(1, 10):
                for k in range(0, 4):
                    print(f'{i + k} * {j} = {(i + k) * j}\t', end=' ')
                print()
            print()


if __name__ == '__main__':
    main()
