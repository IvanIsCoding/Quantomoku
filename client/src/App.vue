<template>
  <div id="app">
    <div class="buttons">
      <div class="pt-x" v-if="!showTutorial" :class="playerTurn == 'x'? 'player-turn pt-active' : 'player-turn'">
        <img class="player-hl" src="./assets/P1.png" width="45px" height="45px" />
      </div>
      <button v-if="!showTutorial" @click="openTutorial">Tutorial</button>
      <div class="pt-o" v-if="!showTutorial" :class="playerTurn == 'o'? 'player-turn pt-active' : 'player-turn'">
        <img class="player-hl" src="./assets/P2.png" width="45px" height="45px" />
      </div>
      <button v-if="showTutorial" @click="openTutorial">Play Game</button>
    </div>
    Turns left before automatic measurement: {{5 - measurementTurn}}
    <div v-if="measurementTurn == 5">Measured at this turn</div>

    <BoardRenderer
      v-if="!showTutorial"
      @cellClicked="cellClicked"
      :selectedCells="this.playedCells"
      :board="this.board"
      :playerTurn="playerTurn"
    />
    <Tutorial v-else />
    <div class="buttons">
      <button
        :disabled="showTutorial"
        @click="sendDataToBackend"
        :class="showTutorial? 'forceNoHoverAnimation': ''"
      >Confirm</button>
      <button
        @click="cancel"
        :disabled="this.playedCells.length == 0"
        :class="this.playedCells.length == 0? 'forceNoHoverAnimation': ''"
      >Cancel</button>
    </div>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
import BoardRenderer from "./components/BoardRenderer.vue";
import Tutorial from "./components/Tutorial.vue";

import io from "socket.io-client";
var socket = io("http://localhost:8000");

export default {
  name: "app",
  components: {
    BoardRenderer,
    Tutorial
  },
  created() {
    var __self = this;
    socket.on("message", function(data) {
      __self.receiveNewDataFromBackend(data);
    });
  },
  methods: {
    /* eslint-disable no-console */
    openTutorial() {
      this.showTutorial = !this.showTutorial;
    },

    sendDataToBackend() {
      socket.emit("message", this.getDataToSendToBackend());
    },
    cancel() {
      this.playedCells = [];
    },
    getTestBoard() {
      return {
        board: [
          [{ id: "0,0", value: "o" }, { id: "1,0", value: "x" }],
          [{ id: "0,1", value: "n" }, { id: "1,1", value: "n" }]
        ],
        playerTurn: "x",
        measurementTurn: 0,
        winner: "o",
        invalid: false,
        invalidMessage: ""
      };
    },
    print2dArray(matrix) {
      for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix[0].length; j++) {
          console.log(matrix[i][j]);
        }
      }
    },
    receiveNewDataFromBackend(dataFromBackend) {
      this.board = dataFromBackend.board;
      this.playerTurn = dataFromBackend.playerTurn;
      this.measurementTurn = dataFromBackend.measurementTurn;
      this.winner = dataFromBackend.winner;
      this.invalid = dataFromBackend.invalid;
      this.invalidMessage = dataFromBackend.invalidMessage;
      this.playedCells = [];
    },
    myFun() {
      alert("hey");
    },
    cellClicked(id) {
      if (!this.playedCells.includes(id)) {
        if (this.playedCells.length < 2) {
          this.playedCells.push(id);
        } else {
          alert(
            "You can't play more than 2 cells. Click cancel to play other cells."
          );
        }
      }
    },
    makeBoard(rows, columns) {
      var result = [];
      for (var i = 0; i < rows; i++) {
        var row = [];
        for (var j = 0; j < columns; j++) {
          row.push({ id: i + "," + j, value: "n" });
        }
        result.push(row);
      }
      return result;
    },
    getDataToSendToBackend() {
      return {
        board: this.board,
        playerTurn: this.playerTurn,
        selectedCells: this.getNumberRespresentationOfPlayedCells(),
        measurementTurn: this.measurementTurn
      };
    },
    getNumberRespresentationOfPlayedCells() {
      var result = [];
      for (var i = 0; i < this.playedCells.length; i++) {
        var coordinates = [];
        var splittingIndex = this.playedCells[i].indexOf(",");
        coordinates.push(
          Number(this.playedCells[i].substring(0, splittingIndex))
        );
        coordinates.push(
          Number(
            this.playedCells[i].substring(
              splittingIndex + 1,
              this.playedCells[i].length
            )
          )
        );
        result.push(coordinates);
      }
      return result;
    }
  },
  data() {
    return {
      board: this.makeBoard(15, 15),
      playerTurn: "x",
      playedCells: [],
      measurementTurn: 0,
      winner: "none",
      invalid: false,
      invalidMessage: "",
      showTutorial: false
    };
  },
  watch: {
    invalid() {
      if (this.invalid) {
        alert(this.invalidMessage);
        this.invalid = false;
        this.invalidMessage = "";
      }
    },
    winner() {
      if (this.winner == "x") {
        alert("X WINS!");
      } else if (this.winner == "o") {
        alert("O WINS!");
      }
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Sniglet&display=swap");

html {
  background-image: url("assets/bg.png");
  background-size: cover;
  background-repeat: no-repeat;
}

#app {
  font-family: "Sniglet", sans-serif;
  font-size: 16pt;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.buttons {
  margin: 10px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  display: block;

  width: 219px;
  height: 47px;

  background: url("assets/button_2.gif") 0 0 no-repeat;

  border-style: none;
  margin: 0 3px;

  font-size: 15pt;
  font-family: "Sniglet", sans-serif;
}

.player-turn {
  background-color: rgba(100, 46, 25, 0.5);
  border-radius: 15px;
  max-height: 45px;
  padding: 2px;
  opacity: 0.25;
}

.pt-x{
  background: salmon;
}

.pt-o{
  background: skyblue;
}

.pt-active {
  opacity: 1;
}

button:hover {
  background-image: url("assets/button_2.gif");
  background-position: 0px -47px;
  background-repeat: no-repeat;
}

.forceNoHoverAnimation {
  background: url("assets/button_2.gif") 0 0 no-repeat !important;
}
</style>
