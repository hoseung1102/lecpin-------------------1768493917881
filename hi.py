import random 

successful = False
for i in range(3):
    print("메시지 전송 시도 중")
    random_number = random.randint(1,10)
    print(f'{i+1}번 째 시도 중')
    for j in range(3):
        random_number += 1
    if random_number < 5:
        successful = True
    if successful:
        break

if successful:    
    print("메시지 전송 성공!")
else:
    print(f'세 번 시도했으나 실패했습니다')