1. cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -rn | head

-c는 count다

2. cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -rn | head

-c는 count고 sort -rn은 내림차순 정렬이다

3. cat access.log | grep -i get | head

-i 는 '대소문자 구분하지말고 긁어와라'

4. cat access.log | grep "GET " | head

GET 뒤에 공백을 넣는 이유는 GET 메서드만 골라내기 위함

5. cat access.log | grep -v "01/Jan" | head

-v 옵션은 들어내는 옵션임

6. cat access.log | grep -e "01/Jan" -e "02/Jan" | head

-e 옵션은 or 관계로 계속 옵션을 붙여서 검색조건을 붙일수 있다.

7. 파이프 간 관계는 and라고 생각하면된다.

8. cat access.log | sort -t " " -k 10 -rn | head

-t는 공백을 기준으로 10번째다.
-k 는 -f랑 같은 역할이다.
-rn은 내림차순.

9. cat access.log | awk -F " " '$1~/"66.249.77.34/ {print $1,$4}' | head

$1~/"66.249.77.34/  : 이런 문자열을 포함하고 있으면(include)
print문 앞에 조건을 붙일수 있다라고 해석할수 있음.

10. cat access.log | awk -F " " '$1~/14.39.80.163/ {sum+=$10} END{print sum}'

해당 ip가 있다는 가정하에 sum이라는 변수에 10번째에 있는 값을 계속 더해라. 그리고 앞선 과정이 다 끝나면 sum을 print 해라.

11. cat access.log | grep "^157.55" | head

^: 이걸로 시작하는걸 찾아달라~

12. cat bigSize.log | awk -F " " '$1~/175.209.132.54/{sum+=$6} END{print sum}'