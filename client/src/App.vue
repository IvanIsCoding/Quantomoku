<template>
  <div id="app">
    <button @click="sendDataToBackend">send data to backend</button>
    <button @click="confirm">confirm</button>
    <button @click="cancel" :disabled="this.playedCells.length == 0">cancel</button>
    <Board @cellClicked="cellClicked" :selectedCells="this.playedCells" />
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
import Board from "./components/Board.vue";

import io from "socket.io-client";

export default {
  name: "app",
  components: {
    Board
  },
  methods: {
    /* eslint-disable no-console */
    confirm() {
      console.log("confirm with values", this.playedCells);
      this.playedCells = [];
    },
    sendDataToBackend() {
      const socket = io("http://localhost:8000");
      alert("sending data to backend");
      var myObject = {
        message: "Hello World!"
      };
      socket.emit("message", myObject);
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
    }
  },
  data() {
    return {
      playedCells: [],
      selectedCells: []
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
  background-color: bisque;
  border-style: dashed;
  border-color: black;
  border-radius: 15px;
  font-family: 'Times New Roman', Times, serif;
}
</style>
