// 백준 - 실버2 - 교수님 계산기가 고장났어요! - 22937 - 수학, 문자열, 사칙연산, 파싱, 큰 수 연산 문제
/*
수학, 문자열, 사칙연산, 파싱, 큰 수 연산 문제

핵심 아이디어
   - double 타입으로는 소수점 18자리의 정밀도를 보장할 수 없음
   - 문자열로 입력을 받아 직접 큰 수 곱셈 알고리즘 구현
   - 소수점 위치를 추적하여 정확한 자릿수 계산
   - 부호 처리를 위한 별도 로직 구현
   - vector를 사용하여 각 자리 수 계산 결과 저장

풀이 과정
   1. 문자열로 입력 받기
   2. 부호 처리
       - 음수 개수에 따라 최종 부호 결정
   3. 소수점 처리
       - 소수점 위치 저장
       - 소수점 제거하여 정수로 변환
   4. 곱셈 수행
       - 각 자리수별 곱셈
       - 올림수(carry) 처리
   5. 결과 문자열 생성
       - 부호 추가
       - 소수점 위치 계산하여 삽입
       - 18자리 맞추기 위해 필요시 0 추가
*/

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

// 문자열로 된 두 수를 곱하는 함수
string multiply(string num1, string num2) {
   // 부호 처리
   bool isNegative = false;
   if (num1[0] == '-') {
       isNegative = !isNegative;
       num1 = num1.substr(1);
   }
   if (num2[0] == '-') {
       isNegative = !isNegative;
       num2 = num2.substr(1);
   }

   // 소수점 위치 찾기
   int point1 = num1.find('.');
   int point2 = num2.find('.');

   // 소수점 제거
   num1.erase(point1, 1);
   num2.erase(point2, 1);

   // 소수점 이하 자릿수 계산
   int decimal = (num1.length() - point1) + (num2.length() - point2);

   vector<int> result(num1.length() + num2.length(), 0);

   // 곱셈 실행
   for(int i = num1.length()-1; i >= 0; i--) {
       for(int j = num2.length()-1; j >= 0; j--) {
           result[i + j + 1] += (num1[i] - '0') * (num2[j] - '0');
       }
   }

   // 올림수 처리
   for(int i = result.size()-1; i > 0; i--) {
       result[i-1] += result[i] / 10;
       result[i] %= 10;
   }

   // 결과 문자열 생성
   string ans;
   if (isNegative) ans += "-";

   bool leadingZero = true;
   int resSize = result.size();
   int pointPos = resSize - decimal;

   for(int i = 0; i < resSize; i++) {
       if (i == pointPos) ans += ".";
       if (leadingZero && result[i] == 0 && i < pointPos-1) continue;
       leadingZero = false;
       ans += result[i] + '0';
   }

   // 소수점 18자리로 맞추기
   while (ans.length() - ans.find('.') - 1 < 18) ans += "0";

   return ans;
}

int main() {
   ios_base::sync_with_stdio(false);
   cin.tie(nullptr);

   int n;
   cin >> n;

   while(n--) {
       string a, b;
       cin >> a >> b;
       cout << multiply(a, b) << '\n';
   }

   return 0;
}

/*
주의사항
   - 0E-18과 같은 지수 표기법 사용 금지
   - 항상 소수점 18자리까지 출력해야 함
   - -4 ≤ A, B ≤ 4 범위 내의 입력만 주어짐
   - 입력은 소수점 9자리까지만 주어짐
*/
