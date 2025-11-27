# PROYECTO-DEEP-Q-LEARNING

Este proyecto implementa un agente basado en Deep Q-Learning para el entorno `ALE/Alien-v5`

## Requisitos

- Python 3.8 o superior
- Virtualenv (opcional pero recomendado)
- GPU compatible con CUDA (opcional, mejora el rendimiento)

  ## Instalaciones
  ENTORNO VIRTUAL:
  
    -     python -m venv nombre_del_entorno
    -     nombre_del_entorno\Scripts\activate.bat

  GPU:

       pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  
  RL-Baselines3 Zoo:
  
       pip install git+https://github.com/DLR-RM/rl-baselines3-zoo

  Gymnasium:

      pip install gymnasium[atari]
      pip install gymnasium[accept-rom-license]

## Creación

A conuación descargar el acrhivo dqn.yml y la carpeta logs\dqn

## Entrenamiento

    python -m rl_zoo3.train --algo dqn --env ALE/Alien-v5 -f logs/ -c dqn.yml

## Visualizar

    python -m rl_zoo3.enjoy --algo dqn --env ALE/Alien-v5  -f logs/ 








  
