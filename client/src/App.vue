<template>
  <div id="app">
    <div class="buttons">
      <button @click="openTutorial">tutorial</button>
      <button @click="sendDataToBackend">send data to backend</button>
      <button @click="confirm">confirm</button>
      <button @click="cancel" :disabled="this.playedCells.length == 0">cancel</button>
      <BoardRenderer
        v-if="!showTutorial"
        @cellClicked="cellClicked"
        :selectedCells="this.playedCells"
        :board="this.board"
      />
      <Tutorial v-else />
    </div>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
import BoardRenderer from "./components/BoardRenderer.vue";
import Tutorial from "./components/Tutorial.vue";

import io from "socket.io-client";

export default {
  name: "app",
  components: {
    BoardRenderer,
    Tutorial
  },
  methods: {
    /* eslint-disable no-console */
    confirm() {
      console.log("confirm with values", this.playedCells);
      this.playedCells = [];
    },
    openTutorial() {
      this.showTutorial = !this.showTutorial;
    },
    sendDataToBackend() {
      // console.log("sending", this.getDataToSendToBackend());
      // const socket = io("http://localhost:8000");
      // socket.emit("message", this.getDataToSendToBackend());
      // socket.on("message", function() {});
      this.receiveNewDataFromBackend(this.getTestBoard());
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
    receiveNewDataFromBackend(dataFromBackend) {
      this.board = dataFromBackend.board;
      this.playerTurn = dataFromBackend.playerTurn;
      this.measurementTurn = dataFromBackend.measurementTurn;
      this.winner = dataFromBackend.winner;
      this.invalid = dataFromBackend.invalid;
      this.invalidMessage = dataFromBackend.invalidMessage;
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
      board: this.makeBoard(19, 19),
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
html {
  background-image: url("assets/bg.png");
  background-size: cover;
  background-repeat: no-repeat;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
  display: block;

  width: 219px;
  height: 47px;

  background: url("assets/button_2.gif") 0 0 no-repeat;

  border-style: none;
  font-family: sans-serif;
  margin: 0 3px;
}

button .mouseover {
  background: url("assets/button_2.gif") 0 -49 no-repeat;
}

.buttons {
  display: flex;
  justify-content: center;
}
</style>
