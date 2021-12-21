# :star2: 25
 얼마 남지 않은 2021, 내 마지막 25살을 기념하기 위해 만든 게임.  

#### :small_orange_diamond: 25 이야기 
> 이 게임을 고안하게 된 이유는,
> https://www.youtube.com/watch?v=JkNV0rSndJ0&feature=emb_imp_woyt  
> 이 영상 속 침팬치가 게임하는 모습을 보며  
> 정말 게임을 잘한다고 생각했고, 사람보다 더 잘하는 것 같다고 생각했다.  
> 그래서 침팬치들이 못하도록 게임 난이도를 좀 더 높이고 싶었다.  

>그렇게 해서 만들어진 녀석이 바로 이 25라는 게임이다.  
>1부터 25까지 누르면 되는 간단한 게임이지만,  
>레벨이 오를수록 숫자가 없어지는 속도가 점점 빨라지게 되어  
>내가 침팬치인가 하는 생각이 들 수 있다,,,  


#### :small_orange_diamond: 게임 세줄 요약 :+1:
> - 💡 1부터 25까지의 숫자를 순서대로 입력한다.
> - 💡 시간이 지남에 따라 25부터 숫자가 가려진다.
> - 💡 레벨이 오를수록 가려지는 속도가 빨라진다.   
   
     


#### :small_orange_diamond:  만들면서 제일 힘들었던 점
       * 제일 힘들었던 부분은 숫자가 사라지게 하는 부분이었다.  
       * 코드를 보면 number_buttons라는 list가 있는데,  
       * 숫자를 클릭하게 되면, list에 저장된 숫자가 앞에서부터 하나씩 지워지게 된다.  
       * 하지만 숫자는 list의 idx를 불러오기 때문에, 1을 지우고 나면 다음숫자가 1이 되는 신기하고도 화가나는 상황이 만들어진다.  
       * 이 문제점은 enumerate에서 발견되었는데, 편리하자고 쓴 함수 덕분에 몇 시간을 고생하게 만들어줬다.   
       * 그리고 이 문제는 idx 값을 거꾸로 만들어주면서 해결이 되었다.    
  
    
  
## 게임 속 장면
![image](https://user-images.githubusercontent.com/76839243/146950079-a76d693a-65e7-4899-b2c2-a136f4e5a557.png)


