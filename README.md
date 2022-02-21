# JAVA_PS
## 프로그래머스(Level1 30/59)
### Methods...
+ 수학
```
Math.sqrt(double num) // (double > double) : num의 제곱근
```
+ 형변환
> String <-> Array
```
String[] strArr = str.split("");   // String to Array : 문자열을 배열로 변환

String str = Arrays.toString(arr); //  (arr > str) : 배열을 문자열로 변환
String str = String.join("-",arr); //  (arr > str) : 배열을 문자열로 변환("-"를 넣어서...)
String str = String.valueOf(ch[]); //  (ch[] > str) : char형 배열을 
```
> String <-> Number
```
Integer.parseInt("1004"); // ("1004" > 1004) : 문자열을 int로 변환
Integer.valueOf(str 또는 int); // 문자열(또는 int)를 Integer객체로 변환
// int num = Integer.valueOf(str) : 자동 unboxing해주는 

String str = Integer.toString(10) // (int > str) : int를 문자열로 변환
String str = String.valueOf(10) // (int > str) : int를 문자열로 변환 
```
+ 기타
```
str.indexOf("가나다") // "가나다"의 index , 없으면 -1 return
```
