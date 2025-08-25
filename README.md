# REINFORCE
```bash
conda create -n reinforce python==3.10
git clone https://github.com/Hands-on-study/REINFORCE.git
git checkout "change your branch name!!"
pip install -r requirements.txt
``` 
REIN FORCE 

![image.png](attachment:a05c345a-f3c5-477b-8911-7102e31e76d3:image.png)

## Quiz

REINFOECE는 Policy Gradient의 대표적인 알고리즘이다.

Q1. REINFORCE와 DQN의 차이점은 무엇인가?

1. REINFORCE는 **policy-based 방법**이고, DQN은 **value-based 방법**이다.
2. REINFORCE는 경험을 **리플레이 메모리**에 저장해 학습하고, DQN은 샘플 효율성을 위해 **에피소드 전체 리턴**을 이용한다.
3. REINFORCE는 action-value 함수 Q(s,a)를 근사하고, DQN은 policy \pi(a|s)를 직접 근사한다.
4. REINFORCE는 deterministic policy를 학습하고, DQN은 stochastic policy를 학습한다.
5. REINFORCE와 DQN은 모두 on-policy 방법이므로, 경험 재사용은 불가능하다.


Q2. Policy gradient 관점에서 바라보았을 때 아래 수식의 성립 여부에 대해
 성립/불성립을 선택하고 선택에 대한 이유를 한 줄로 간략히 설명하시오.

<aside>
💡

$\pi_{\theta_1}$ ≠ $\pi_{\theta_2}$

</aside>


Q3. REINFORCE 알고리즘은 에피소드가 **끝난 후**에 파라미터를 업데이트한다.
이로 인해 발생하는 주요 단점은 무엇인가?

![image.png](attachment:a05c345a-f3c5-477b-8911-7102e31e76d3:image.png)

Q4. quiz_Cartpole-REINFORCE.py 코드를 실행시키시오.

## git push
```bash
git checkout -b your-branch-name
# 예: git checkout -b pan

git add .
git commit -m "message"
# 예: git commit -m "Add solution by pan"

git push origin your-branch-name
# 예: git push origin pan
```
