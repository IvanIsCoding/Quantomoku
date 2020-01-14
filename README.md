# Quantomoku [![Vue.js](https://img.shields.io/badge/-Vue.js-41b883)](https://github.com/topics/vuejs) [![Python](https://img.shields.io/badge/-Python-blue)](https://github.com/topics/python) [![Qiskit](https://img.shields.io/badge/-Qiskit-blueviolet)](https://github.com/topics/qiskit) [![Socket.IO](https://img.shields.io/badge/-Socket.IO-green)](https://github.com/topics/socketio)

<p align="center"> 
<img width="360" height="414" src="client/src/assets/Quat.png">
</p>

Quantomoku is an educational quantum game aimed at children. The game is inspired by the traditional Connect 5 game: two players alternate putting pieces on a board, and the first one to line up 5 pieces wins. However, there is a twist: in addition to the normal Connect 5 moves, players can play two new quantum moves: superpositions and entanglements!

Moreover, the game is truly quantum: as the players play, a quantum circuit is built in the backend. Hence, quantum computers can be used to decide the result of the game.

## Setting up

### Javascript dependencies

Javascript dependencies are managed by `npm`. To install them, run on the root directory:

```
cd client && npm install
```

### Python dependencies

Python dependencies are managed by `pip`. To install them, run on the root directory:

```
pip3 install -r requirements.txt
```

### Using the quantum cloud in the game

By default, the game runs the quantum circuits locally in a simulator. If you wish to run them on the quantum cloud on a real quantum computer, create an environment variable called `IBM_Q` set to your IBM Q API Token. Then, run:

```
python3 setup_ibmq.py
```

Notice that depending on the queue on the quantum cloud, this might make the game have delays that will affect gameplay.

## Playing the game

For the game to work, both the server and the client need to be running on the same time. You may launch both together by running:

```
python3 server.py & cd client && npm run serve
```

After executing the command, the game will be now running. You can access it by going into a web browser and visiting `https://localhost:8080`. 

### Tutorial

To discover more about the mechanics of the game, there is an in game tutorial: just click on the Tutorial button on the main page. Quat, the Quantum Cat will explain how the game works for you.

## Built With

* [Vue.js](https://vuejs.org/) - Front end
* [Python](https://www.python.org/) - Back end
* [Qiskit](https://qiskit.org/) - Used for building quantum circuits and executing them on real quantum computers at IBM Quantum Experience
* [Socket.IO](https://rometools.github.io/rome/) - Used to communicate between the front end and the back end

## Authors

* [**Jean-Philippe Abadir**](https://github.com/jpabadir)
* [**Ivan Carvalho**](https://github.com/ivaniscoding)
* [**Devina Jaiswal**](https://github.com/devinapj)
* [**Kathryn Ng**](https://github.com/kathrynng)