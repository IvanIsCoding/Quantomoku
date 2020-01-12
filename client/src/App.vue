<template>
  <div id="app">
    <div class="buttons">
    <button @click="sendDataToBackend">send data to backend</button>
    <button @click="confirm">confirm</button>
    <button @click="cancel" :disabled="this.playedCells.length == 0">cancel</button>
    <BoardRenderer
      @cellClicked="cellClicked"
      :selectedCells="this.playedCells"
      :board="this.board"
    />
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
import BoardRenderer from "./components/BoardRenderer.vue";

import io from "socket.io-client";

export default {
  name: "app",
  components: {
    BoardRenderer
  },
  methods: {
    /* eslint-disable no-console */
    confirm() {
      console.log("confirm with values", this.playedCells);
      this.playedCells = [];
    },
    sendDataToBackend() {
      // console.log("sending", this.getDataToSendToBackend());
      const socket = io("http://localhost:8000");
      socket.emit("message", this.getDataToSendToBackend());
      socket.on("message", function(data) {
        console.log(data);
      });
    },
    cancel() {
      this.playedCells = [];
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
      measurementTurn: 0
    };
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

  background: url('assets/button_2.gif') 0 0 no-repeat; 

  border-style: none; 
  font-family:  sans-serif;
  margin: 0 3px;
}

button .mouseover{
  background: url('assets/button_2.gif') 0 -49 no-repeat;
}

.buttons{
  display: flex;
  justify-content: center;
}
</style>
