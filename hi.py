import random 

successful = False
for i in range(3):
    print("메시지 전송 시도 중")
    random_number = random.randint(1,10)
    if random_number < 3:
        successful = True
    if successful:
        break
    else:
        print("세 번 시도했으나 실패했습니다")
    