import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import gymnasium as gym
import numpy as np
from collections import deque
import pylab

# 정책 신경망 (Actor) 정의
class PolicyNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, action_size)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        return F.softmax(self.fc2(x), dim=1)

# 가치 신경망 (Critic / Baseline) 정의
class ValueNetwork(nn.Module):
    def __init__(self, state_size):
        super(ValueNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 1)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        return self.fc2(x)

# REINFORCE with Baseline 알고리즘 구현
def train_reinforce_with_baseline(env, policy_net, value_net, policy_optimizer, value_optimizer, num_episodes, gamma=0.99):
    """
    REINFORCE with Baseline 알고리즘을 사용하여 정책과 가치 함수를 훈련합니다.
    """
    
    scores = []
    episodes = []

    for episode in range(num_episodes):
        state, _ = env.reset()
        done = False
        rewards = []
        states = []
        log_probs = []

        # 한 에피소드 진행
        while not done:
            state_tensor = torch.from_numpy(state).float().unsqueeze(0)
            
            # 행동 선택 (정책 신경망)
            action_probs = policy_net(state_tensor)
            action_dist = torch.distributions.Categorical(action_probs)
            action = action_dist.sample()
            
            # TODO
            log_prob = "".log_prob("")
            
            # 환경에서 행동 수행
            next_state, reward, terminated, truncated, _ = env.step(action.item())
            done = terminated or truncated
            
            # 데이터 저장
            rewards.append(reward)
            states.append(state_tensor)
            log_probs.append(log_prob)
            
            state = next_state

        # 에피소드 종료 후 학습
        # 누적 할인 보상 (G_t) 계산
        returns = deque()
        discounted_return = 0
        for reward in reversed(rewards):
            discounted_return = ""
            returns.appendleft(discounted_return)
        
        returns = torch.tensor(list(returns)).float().unsqueeze(1)
        
        # 가치 예측 (# TODO !!Value Network!!)
        states_tensor = torch.cat(states)

        # TODO 
        predicted_values = ""
        
        # 어드밴티지 (Advantage) 계산 G_t - V(s)
        # TODO
        advantage = ""
        
        # 손실 계산
        # 정책 손실
        policy_loss = []
        
        for log_prob, A_t in zip(log_probs, advantage):
            policy_loss.append(-"" * A_t.detach()) #detach()는 gradient 전파를 막음

        # 가치 손실 (MSE)
        # TODO
        value_loss = F.mse_loss("", "")
        
        # 옵티마이저를 통해 경사 하강 수행
        # 정책 신경망 업데이트
        policy_optimizer.zero_grad()
        total_policy_loss = torch.sum(torch.stack(policy_loss))
        total_policy_loss.backward()
        policy_optimizer.step()
        
        # 가치 신경망 업데이트
        value_optimizer.zero_grad()
        value_loss.backward()
        value_optimizer.step()
        
        # 에피소드 결과 출력
        total_reward = sum(rewards)
        scores.append(total_reward)
        episodes.append(episode)

        print(f"Episode: {episode+1}, Total Reward: {total_reward:.2f}, Policy Loss: {total_policy_loss.item():.2f}, Value Loss: {value_loss.item():.2f}")

    # 학습 완료 후 그래프 생성
    pylab.plot(episodes, scores, 'b')
    pylab.xlabel('Episode')
    pylab.ylabel('Total Reward')
    pylab.title('REINFORCE with Baseline on CartPole-v1')
    pylab.grid(True)
    pylab.show('reinforce_with_baseline_rewards.png')

# 메인 함수
if __name__ == "__main__":
    env = gym.make('CartPole-v1', render_mode = "human")
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    
    # 모델 및 옵티마이저 초기화

    # TODO
    policy_net = PolicyNetwork("", "")

    # TODO
    value_net = ValueNetwork("")
    
    policy_optimizer = optim.Adam(policy_net.parameters(), lr=1e-2)
    value_optimizer = optim.Adam(value_net.parameters(), lr=1e-2)
        
    num_episodes = 1000
    
    train_reinforce_with_baseline(env, policy_net, value_net, policy_optimizer, value_optimizer, num_episodes)

    env.close()
