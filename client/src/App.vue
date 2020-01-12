<template>
  <div id="app">
    <div  class="buttons" >
    <button @click="openTutorial">Tutorial</button></div>
    Turns left before automatic measurement: {{5 - measurementTurn}}
    
    <div v-if="measurementTurn == 5">Measured at this turn</div>
    
    <BoardRenderer
        v-if="!showTutorial"
        @cellClicked="cellClicked"
        :selectedCells="this.playedCells"
        :board="this.board"
      />
      <Tutorial v-else />
      <div class="buttons">
      
      <button class="active" @click="sendDataToBackend">Confirm</button>
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
      showTutorial: false,
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
@import url('https://fonts.googleapis.com/css?family=Sniglet&display=swap');

html {
  background-image: url("assets/bg.png");
  background-size: cover;
  background-repeat: no-repeat;

}

#app {
    font-family: 'Sniglet', sans-serif;
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
    font-family: 'Sniglet', sans-serif;

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
