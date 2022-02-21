# JAVA_PS
## 프로그래머스(Level1 41/59)
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
> List <--> Array
```
String[] arr = arr.toArray(new String[list.size()]) // (list > arr) : 리스트를 배열로 // 배열길이는 0 또는 list의 크기만큼 

list = Arrays.asList(arr) // (arr > list) : 배열을 리스트로
list = new ArrayList<>(Arrays.asList(arr)); //(arr > ArrayList) : 배열을 ArrayList로
list = Stream.of(arr).collect(Colletors.toList()); // (ara > list) : 스트림을 이용
```
+ 기타
```
str.indexOf("가나다") // "가나다"의 index , 없으면 -1 return
ArrayList.get(i) // i번째 인덱스 값 가져오기
```
