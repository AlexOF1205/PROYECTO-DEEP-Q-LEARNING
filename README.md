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

## Extra

### logs.zip
    https://drive.google.com/file/d/1nMgWjX5WJfNLg4ZXB7QYEox4VWHHISBq/view?usp=sharing
### entorno virtual
    https://drive.google.com/file/d/1LpaYf1n5RA7UY53mLrHbQWYwaVB-lkdW/view?usp=sharing

## Explicación
dqn.yml: Archivos donde vienen mis hiperparámetros

evaluar_modelo(1).py: Archivo que usé para sacar las grágicas utilizadas para medir el rendimiento

The Arcade Learning Environment.mp4: Video del agente








  
