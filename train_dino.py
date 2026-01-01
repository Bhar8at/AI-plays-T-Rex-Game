from stable_baselines3 import PPO
from game.dinogame import DinoGame
def train_dino(timesteps = 100000, render = True):
    """Training Dino AI with PPO"""


    env = DinoGame()

    # Create PPO model
    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64,
        gamma=0.99,
    )

    # Train the model
    print("Starting training...")
    model.learn(total_timesteps=timesteps)

    # Save the model
    model.save("snake_model")
    print("Model saved as 'snake_model'")

    env.close()
    return model

def play_trained_model(model_path = "Dino_model", episodes=5):
    """Watch the trained model play"""

    env = DinoGame()

    model = PPO.load(model_path, env = env)

    scores = []

    for episode in range(episodes):
        obs, info = env.reset()
        done = False

        while not done:
            action,_ = model.predict(obs, deterministic=True)

            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated


        score = info.get('score', 0)
        scores.append(score)
    
    env.close()
    print(f"\nResults:")
    print(f"Average Score: {sum(scores)/len(scores):.2f}")
    print(f"Best Score: {max(scores)}")

    return scores

def main():
    """CLI interface"""

    import sys

    if len(sys.argv) == 1:
        train_dino()
    elif sys.argv[1] == "train":
        timesteps = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
        render = True
        train_dino(timesteps, render)
    elif sys.argv[1] == "play":
        model_path = sys.argv[2] if len(sys.argv) > 2 else "dino_model"
        episodes = int(sys.argv[3]) if len(sys.argv) > 3 else 5

        play_trained_model(model_path, episodes)
    else:
        print("Usage:")
        print("  python train_dino.py                    # Train with defaults")
        print("  python train_dino.py train 200000       # Train for 200k steps")
        print("  python train_dino.py train 50000 --render # Train with rendering")
        print("  python train_dino.py play               # Watch trained model")
        print("  python train_dino.py play dino_model 3 # Watch model play 3 games")

if __name__ == "__main__":
    main()