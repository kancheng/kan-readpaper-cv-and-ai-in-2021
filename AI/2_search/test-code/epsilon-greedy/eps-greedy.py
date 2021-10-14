import numpy as np
T = 10000 # 學生數量 T
N = 20 # 顧問數 N
true_rewards = np.random.uniform( low = 0, high = 1, size = N) # 被評好顧問的機率
estimated_rewards = np.zeros(N)
number_of_trials = np.zeros(N)
total_reward = 0 
def alpha_greedy( N, alpha = 0.1):
    item = 0
    if np.random.random() < alpha:
        item = np.random.randint( low = 0, high = N)
    else:
        item = np.argmax(estimated_rewards)
    reward = np.random.binomial( n = 1, p = true_rewards[item])
    return item, reward
for t in range(1, T): # T個學生逐一進入中心諮詢
   # 從 N 個顧問中推薦一位，reward = 1 表示學生接受，reward = 0 表示學拒絕並離開。
   item, reward = alpha_greedy(N)
   total_reward += reward # 一共有多少學生接受(也就是願意請顧問申請學校)

   # 更新成功機率
   number_of_trials[item] += 1
   estimated_rewards[item] = ((number_of_trials[item] - 1) * estimated_rewards[item] + reward) / number_of_trials[item]

print("total_reward=" + str(total_reward))