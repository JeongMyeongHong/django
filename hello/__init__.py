from hello.domains import Member
from hello.models import Quiz01Calc, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz06RandomGenerator, \
    Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, \
    Quiz14Gugudan


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
            member = Member
            q2 = Quiz02Bmi
            member.name = input('이름 입력 : ')
            member.height = float(input('키 입력 : '))
            member.weight = float(input('몸무게 입력 : '))
            res = f'{member.name} 님은 키 : {member.height} ' \
                  f'몸무게 : {member.weight} 결과 : {q2.get_bmi(member)}'

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


if __name__ == '__main__':
    main()